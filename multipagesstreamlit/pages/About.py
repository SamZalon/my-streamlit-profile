import streamlit as st

st.set_page_config(page_title="About", page_icon="ℹ️")

st.title("About ℹ️")

# --- กล่อง App Info ---
with st.container(border=True):
    st.subheader("App Info:")
    st.markdown("**App Name:** My Profile App")
    st.markdown("**Developer:** นายสุชานันท์ ขันพระแสง")
    st.markdown("**Description:** แอพพลิเคชั่นนี้สร้างขึ้นเพื่อแสดงข้อมูลส่วนตัวของข้าพเจ้า รวมถึงประวัติการศึกษา (เวอร์ชัน Streamlit)")

# --- กล่อง Contact ---
with st.container(border=True):
    st.subheader("ช่องทางติดต่อ")
    st.markdown("**Email:** s6610886130@pkru.ac.th")
    st.markdown("**Instagram:** @prw.james")