
import streamlit as st
import datetime

st.set_page_config(page_title="ISP Master Brain", layout="wide")
st.title("🌐 ISP Master Brain - Control Center")
st.sidebar.header("Status: Online")

st.write(f"সর্বশেষ আপডেট: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

col1, col2 = st.columns(2)
with col1:
    st.metric(label="Active Routers", value="5", delta="OK")
with col2:
    st.metric(label="Total Users", value="150", delta="+3 New")

st.subheader("Quick Actions")
if st.button('Run Network Scan'):
    st.info("Scanning network... Please wait.")

if st.button('Backup Config'):
    st.success("Configuration backed up successfully!")
