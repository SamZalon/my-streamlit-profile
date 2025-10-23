import streamlit as st

st.set_page_config(page_title="My Profile", page_icon="🧑‍💻")

# --- แสดงรูปโปรไฟล์ ---
# ใช้คอลัมน์เพื่อจัดให้อยู่ตรงกลาง (คล้ายๆ CircleAvatar)
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.image("images/myprofile.jpg", width=200)

st.title("ประวัติส่วนตัว")

# --- กล่องข้อมูล (คล้ายๆ Container ที่มีขอบ) ---
with st.container(border=True):
    st.markdown("**ชื่อ-สกุล:** นายสุชานันท์ ขันพระแสง")
    st.markdown("**รหัสนักศึกษา:** 6610886130")
    st.markdown("**คณะ:** วิทยาศาสตร์และเทคโนโลยี")
    st.markdown("**สาขาวิชา:** เทคโนโลยีดิจิทัล")
    st.markdown("**วิชาเอก:** วิทยาการคอมพิวเตอร์")
    
    st.divider() # เส้นคั่น
    
    st.markdown("**งานอดิเรก:** ดูหนัง, เล่นเกม")
    st.markdown("**อาหารที่ชอบ:** มาม่าผัด, กระเพราไก่")
    st.markdown("**สิ่งที่ชอบ:** AI")