import streamlit as st

st.set_page_config(page_title="My Education", page_icon="🎓")

st.title("ประวัติการศึกษา 🎓")

# --- ส่วนที่ 1: ระดับประถมศึกษา ---
with st.container(border=True):
    col1, col2 = st.columns([1, 4]) # แบ่งคอลัมน์สำหรับรูปและข้อความ
    with col1:
        st.image("multipagesstreamlit/images/perple.png", width=80)
    with col2:
        st.subheader("ระดับประถมศึกษา")
        st.write("โรงเรียนบ้านควนม่วง")

# --- ส่วนที่ 2: ระดับมัธยมศึกษา ---
with st.container(border=True):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image("multipagesstreamlit/images/KP.png", width=80)
    with col2:
        st.subheader("ระดับมัธยมศึกษา ตอนต้น-ตอนปลาย")
        st.write("โรงเรียนเขาดินประชานุกูล")

# --- ส่วนที่ 3: ระดับมหาวิทยาลัย ---
with st.container(border=True):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image("multipagesstreamlit/images/KD.png", width=60)
    with col2:
        st.subheader("ระดับการศึกษา: ปริญญาตรี")
        st.write("มหาวิทยาลัยราชภัฏภูเก็ต")
        st.write("สาขาวิชา: เทคโนโลยีดิจิทัล")
        st.write("วิชาเอก: วิทยาการคอมพิวเตอร์")
