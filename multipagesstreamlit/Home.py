import streamlit as st

# --- ตั้งค่าหน้าเว็บ (Page Config) ---
# นี่ควรเป็นคำสั่งแรกสุดในสคริปต์ของคุณ
st.set_page_config(
    page_title="My Profile App",
    page_icon="👋", # คุณสามารถใช้ emoji เป็นไอคอนได้
    layout="wide" # ใช้พื้นที่เต็มความกว้าง
)

# --- หน้าหลัก ---
st.title("My Profile App 👋")
st.subheader("ยินดีต้อนรับสู่เว็บแอปแนะนำตัวของผม")

st.write("---")

# แสดงรูปภาพหลักบนหน้า Home
# (ปรับ layout ตามที่คุณต้องการ)
col1, col2, col3 = st.columns([1,2,1]) # แบ่ง 3 คอลัมน์ ให้ตรงกลางกว้างสุด

#... (โค้ดส่วนอื่น) ...
with col2:
    st.image("multipagesstreamlit/images/myprofile.jpg", caption="สุชานันท์ ขันพระแสง", use_container_width=True)



