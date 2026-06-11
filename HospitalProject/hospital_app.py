import streamlit as st
import pandas as pd
import sqlite3

# --- DATABASE CONNECTION ---
conn = sqlite3.connect('hospital_management.db', check_same_thread=False)
c = conn.cursor()

# Initialize all tables
c.execute('CREATE TABLE IF NOT EXISTS Patients (PatientID INTEGER PRIMARY KEY, Name TEXT, Phone TEXT)')
c.execute('CREATE TABLE IF NOT EXISTS Doctors (DoctorID INTEGER PRIMARY KEY, Name TEXT, Specialty TEXT)')
c.execute('CREATE TABLE IF NOT EXISTS Appointments (AppID INTEGER PRIMARY KEY, PatientID INTEGER, DoctorID INTEGER, Date TEXT, Status TEXT)')
c.execute('CREATE TABLE IF NOT EXISTS Billing (BillID INTEGER PRIMARY KEY, AppID INTEGER, Amount REAL, Tax REAL, Total REAL)')
conn.commit()

# --- SIDEBAR BRANDING ---
st.sidebar.title("🏥 MJ Hospital ")
st.sidebar.info("Health is wealth")
menu = ["Dashboard", "Patients", "Doctors", "Book Appointment", "Billing"]
choice = st.sidebar.selectbox("Menu", menu)

# --- 1. DASHBOARD ---
if choice == "Dashboard":
    st.header("Hospital Analytics")
    
    # Fetch real counts from SQL
    patient_count = pd.read_sql_query("SELECT COUNT(*) as count FROM Patients", conn).iloc[0]['count']
    app_count = pd.read_sql_query("SELECT COUNT(*) as count FROM Appointments", conn).iloc[0]['count']
    revenue = pd.read_sql_query("SELECT SUM(Total) as total FROM Billing", conn).fillna(0).iloc[0]['total']
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Patients", patient_count)
    col2.metric("Total Appointments", app_count)
    col3.metric("Total Revenue", f"Ksh{revenue:,.2f}")

    st.subheader("Appointment Trends")
    # Simple query to show activity
    trend_data = pd.read_sql_query("SELECT Date, COUNT(AppID) as Count FROM Appointments GROUP BY Date", conn)
    if not trend_data.empty:
        st.line_chart(trend_data.set_index('Date'))
    else:
        st.write("No appointment data to visualize yet.")

# --- 2. PATIENTS ---
elif choice == "Patients":
    st.header("Patients")
    with st.expander("➕ Register New Patient"):
        name = st.text_input("Full Name")
        phone = st.text_input("Phone Number")
        if st.button("Add Patient"):
            c.execute("INSERT INTO Patients (Name, Phone) VALUES (?,?)", (name, phone))
            conn.commit()
            st.success(f"Registered {name}")
            st.rerun() # Refresh to show new data

    df = pd.read_sql_query("SELECT * FROM Patients", conn)
    st.dataframe(df, use_container_width=True)

# --- 3. DOCTORS ---
elif choice == "Doctors":
    st.header("Staff Management")
    
    # 1. Fetch data
    df_docs = pd.read_sql_query("SELECT * FROM Doctors", conn)
    
    # 2. Display Table with Selection enabled
    st.subheader("Current Staff")
    st.write("Click the checkbox next to a doctor to edit their details.")
    
    # This creates an interactive table where you can select a row
    event = st.dataframe(
        df_docs, 
        use_container_width=True, 
        hide_index=True,
        on_select="rerun",  # This makes the app refresh as soon as you click
        selection_mode="single-row"
    )

    # 3. Logic to show the Edit Form only when a row is selected
    selected_rows = event.selection.rows
    
    if selected_rows:
        # Get the data for the specific row clicked
        row_index = selected_rows[0]
        selected_doc = df_docs.iloc[row_index]
        
        st.markdown(f"### ✏️ Editing: Dr. {selected_doc['Name']}")
        
        with st.container(border=True):
            edit_name = st.text_input("Full Name", value=selected_doc['Name'])
            
            spec_list = ["General Practice", "Cardiology", "Pediatrics", "Orthopedics", "Neurology", "Dermatology","Love"]
            try:
                default_ix = spec_list.index(selected_doc['Specialty'])
            except ValueError:
                default_ix = 0
            
            edit_spec = st.selectbox("Specialty", spec_list, index=default_ix)
            
            col1, col2, col3 = st.columns([1, 1, 2])
            if col1.button("Save Changes", type="primary"):
                c.execute("UPDATE Doctors SET Name = ?, Specialty = ? WHERE DoctorID = ?", 
                          (edit_name, edit_spec, int(selected_doc['DoctorID'])))
                conn.commit()
                st.success("Updated successfully!")
                st.rerun()
            
            if col2.button("Delete"):
                c.execute("DELETE FROM Doctors WHERE DoctorID = ?", (int(selected_doc['DoctorID']),))
                conn.commit()
                st.warning("Doctor removed.")
                st.rerun()
                
            if col3.button("Cancel"):
                st.rerun()
    else:
        # Only show the "Register New Doctor" expander if no one is being edited
        with st.expander("➕ Register New Doctor"):
            with st.form("add_doc"):
                new_name = st.text_input("Doctor Name")
                new_spec = st.selectbox("Specialty", ["General Practice", "Cardiology", "Pediatrics", "Orthopedics","Love"])
                if st.form_submit_button("Add to Staff"):
                    c.execute("INSERT INTO Doctors (Name, Specialty) VALUES (?,?)", (new_name, new_spec))
                    conn.commit()
                    st.rerun()
# --- 4. BOOK APPOINTMENT ---
elif choice == "Book Appointment":
    st.header("Schedule Visit")
    patients_df = pd.read_sql_query("SELECT PatientID, Name FROM Patients", conn)
    doctors_df = pd.read_sql_query("SELECT DoctorID, Name FROM Doctors", conn)
    
    if patients_df.empty or doctors_df.empty:
        st.warning("Ensure Patients and Doctors are registered first.")
    else:
        with st.form("app_form"):
            p_choice = st.selectbox("Select Patient", patients_df['Name'].tolist())
            d_choice = st.selectbox("Select Doctor", doctors_df['Name'].tolist())
            date = st.date_input("Date")
            if st.form_submit_button("Confirm Booking"):
                p_id = int(patients_df[patients_df['Name'] == p_choice]['PatientID'].iloc[0])
                d_id = int(doctors_df[doctors_df['Name'] == d_choice]['DoctorID'].iloc[0])
                c.execute("INSERT INTO Appointments (PatientID, DoctorID, Date, Status) VALUES (?,?,?,?)", 
                          (p_id, d_id, str(date), "Scheduled"))
                conn.commit()
                st.success("Appointment Booked!")

# --- 5. BILLING ---
elif choice == "Billing":
    st.header("Invoicing")
    query = "SELECT AppID FROM Appointments WHERE AppID NOT IN (SELECT AppID FROM Billing)"
    pending = pd.read_sql_query(query, conn)
    
    if not pending.empty:
        app_id = st.selectbox("Select Appointment ID", pending['AppID'].tolist())
        fee = st.number_input("Fee (Ksh)", min_value=0.0, value=100.0)
        tax = fee * 0.15
        total = fee + tax
        
        st.write(f"Total including 15% tax: **Ksh{total:.2f}**")
        if st.button("Save & Print Bill"):
            c.execute("INSERT INTO Billing (AppID, Amount, Tax, Total) VALUES (?,?,?,?)", (app_id, fee, tax, total))
            conn.commit()
            st.success("Bill Paid!")
    else:
        st.write("No pending bills.")