import streamlit as st
import pandas as pd
import sqlite3
from datetime import datetime

# --- 1. CONFIGURATION & THEME ---
st.set_page_config(page_title="Justus Feeds Manager", page_icon="🌱", layout="wide")

# White and Green Professional Styling
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    [data-testid="stSidebar"] { background-color: #F1F8E9; border-right: 1px solid #C8E6C9; }
    h1, h2, h3 { color: #2E7D32; font-family: 'Segoe UI', sans-serif; }
    .stMetric { background-color: #F1F8E9; padding: 15px; border-radius: 10px; border: 1px solid #C8E6C9; }
    div.stButton > button { 
        background-color: #4CAF50; color: white; border-radius: 8px; 
        border: none; padding: 10px 24px; font-weight: bold;
    }
    div.stButton > button:hover { background-color: #388E3C; border: none; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. DATABASE & RECIPE SETUP ---
conn = sqlite3.connect('animal_feeds.db', check_same_thread=False)
c = conn.cursor()

# Pre-defined recipes: (Material Name: Kg needed per 1 bag produced)
RECIPES = {
    "Chicken Mash": {"Maize": 30, "Soya": 10, "Fishmeal": 5, "Premix": 2},
    "Growers Mash": {"Maize": 25, "Wheat Bran": 15, "Soya": 8, "Premix": 2},
    "Dairy Meal": {"Maize": 20, "Wheat Bran": 20, "Cotton Seed": 10},
    "Layers Mash": {"Maize": 28, "Soya": 12, "Lime": 6, "Premix": 2}
}

def init_db():
    c.execute('''CREATE TABLE IF NOT EXISTS raw_materials 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, material_name TEXT UNIQUE, quantity_kg REAL)''')
    c.execute('''CREATE TABLE IF NOT EXISTS production_logs 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, feed_type TEXT, bags_produced INTEGER, date_produced DATE)''')
    c.execute('''CREATE TABLE IF NOT EXISTS sales 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, feed_type TEXT, bags_sold INTEGER, total_revenue REAL, sale_date DATE)''')
    
    # Pre-populate materials if empty
    materials = ["Maize", "Soya", "Fishmeal", "Wheat Bran", "Premix", "Lime", "Cotton Seed"]
    for m in materials:
        c.execute("INSERT OR IGNORE INTO raw_materials (material_name, quantity_kg) VALUES (?, 0)", (m,))
    conn.commit()

init_db()

# --- 3. SIDEBAR NAVIGATION ---
st.sidebar.title("🌱 GreenFeed Admin")
menu = ["Inventory Dashboard", "Log Production", "Point of Sale", "Admin Analytics"]
choice = st.sidebar.radio("Go to:", menu)

# --- 4. INVENTORY DASHBOARD ---
if choice == "Inventory Dashboard":
    st.header("Raw Material Inventory")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        with st.form("add_stock"):
            st.subheader("Update Stock")
            mat_to_update = st.selectbox("Select Material", list(RECIPES["Chicken Mash"].keys()) + ["Wheat Bran", "Lime", "Cotton Seed"])
            amt_to_add = st.number_input("Added Quantity (Kg)", min_value=0.0)
            if st.form_submit_button("Add to Inventory"):
                c.execute("UPDATE raw_materials SET quantity_kg = quantity_kg + ? WHERE material_name = ?", (amt_to_add, mat_to_update))
                conn.commit()
                st.success(f"Added {amt_to_add}kg to {mat_to_update}")
                st.rerun()

    with col2:
        st.subheader("Current Levels")
        df_inv = pd.read_sql_query("SELECT material_name as 'Material', quantity_kg as 'Stock (Kg)' FROM raw_materials", conn)
        st.dataframe(df_inv, use_container_width=True, hide_index=True)

# --- 5. PRODUCTION WITH RECIPE LOGIC ---
elif choice == "Log Production":
    st.header("Production Line")
    
    feed_choice = st.selectbox("Select Feed to Produce", list(RECIPES.keys()))
    bags_to_make = st.number_input("Number of Bags (50kg each)", min_value=1, step=1)
    
    recipe = RECIPES[feed_choice]
    st.write("**Required Materials:**")
    for mat, amt in recipe.items():
        st.write(f"- {mat}: {amt * bags_to_make} Kg")

    if st.button("Confirm Production & Deduct Stock"):
        # Check stock first
        can_produce = True
        for mat, amt in recipe.items():
            c.execute("SELECT quantity_kg FROM raw_materials WHERE material_name = ?", (mat,))
            current_stock = c.fetchone()[0]
            if current_stock < (amt * bags_to_make):
                st.error(f"Not enough {mat}! Need {amt * bags_to_make}kg, only have {current_stock}kg.")
                can_produce = False
        
        if can_produce:
            # Deduct Stock
            for mat, amt in recipe.items():
                c.execute("UPDATE raw_materials SET quantity_kg = quantity_kg - ? WHERE material_name = ?", (amt * bags_to_make, mat))
            
            # Log Production
            c.execute("INSERT INTO production_logs (feed_type, bags_produced, date_produced) VALUES (?, ?, ?)", 
                      (feed_choice, bags_to_make, datetime.now().date()))
            conn.commit()
            st.balloons()
            st.success(f"Successfully produced {bags_to_make} bags of {feed_choice}!")

# --- 6. POINT OF SALE ---
# --- 6. POINT OF SALE (With Stock Detection) ---
elif choice == "Point of Sale":
    st.header("Point of Sale")
    
    with st.container(border=True):
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            s_feed = st.selectbox("Select Feed to Sell", list(RECIPES.keys()))
        
        # --- STOCK CALCULATION LOGIC ---
        # 1. Get total produced
        c.execute("SELECT SUM(bags_produced) FROM production_logs WHERE feed_type = ?", (s_feed,))
        total_produced = c.fetchone()[0] or 0
        
        # 2. Get total already sold
        c.execute("SELECT SUM(bags_sold) FROM sales WHERE feed_type = ?", (s_feed,))
        total_sold_already = c.fetchone()[0] or 0
        
        # 3. Calculate current balance
        available_stock = total_produced - total_sold_already
        
        with col_b:
            s_bags = st.number_input("Bags to Sell", min_value=0, step=1)
        with col_c:
            s_price = st.number_input("Total Price (KES)", min_value=0.0)

        # Display Stock Status
        if available_stock <= 0:
            st.error(f"❌ Out of Stock! You have 0 bags of {s_feed} in store.")
        else:
            st.info(f"✅ Available Stock: {available_stock} bags")

        if st.button("Complete Transaction"):
            if available_stock <= 0:
                st.error("Transaction Failed: No bags available in production logs.")
            elif s_bags > available_stock:
                st.error(f"Transaction Failed: You only have {available_stock} bags, but tried to sell {s_bags}.")
            elif s_bags == 0:
                st.warning("Please enter a quantity greater than 0.")
            else:
                # If all checks pass, record the sale
                c.execute("INSERT INTO sales (feed_type, bags_sold, total_revenue, sale_date) VALUES (?, ?, ?, ?)",
                          (s_feed, s_bags, s_price, datetime.now().date()))
                conn.commit()
                st.success(f"Sale Successful! {s_bags} bags of {s_feed} sold.")
                st.rerun() # Refresh to update stock count
# --- 7. ADMIN ANALYTICS ---
elif choice == "Admin Analytics":
    st.header("🔒 Business Intelligence")
    pwd = st.text_input("Admin Password", type="password")
    
    if pwd == "green2026":
        # Metrics
        df_s = pd.read_sql_query("SELECT * FROM sales", conn)
        total_rev = df_s['total_revenue'].sum() if not df_s.empty else 0
        
        m1, m2 = st.columns(2)
        m1.metric("Total Revenue", f"KES {total_rev:,.2f}")
        m2.metric("Total Bags Sold", int(df_s['bags_sold'].sum() if not df_s.empty else 0))
        
        # Editable Logs
        st.subheader("Edit Production Records")
        df_p = pd.read_sql_query("SELECT * FROM production_logs", conn)
        edited_p = st.data_editor(df_p, use_container_width=True, hide_index=True)
        
        if st.button("Save Changes to Logs"):
            # Logic to update database from edited dataframe would go here
            st.info("Log editing feature active. Manual SQL update required for bulk changes.")
            
        st.subheader("Sales Over Time")
        if not df_s.empty:
            df_s['sale_date'] = pd.to_datetime(df_s['sale_date'])
            sales_chart = df_s.groupby('sale_date')['total_revenue'].sum()
            st.line_chart(sales_chart)
    elif pwd:
        st.error("Invalid Credentials")