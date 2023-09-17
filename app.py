import streamlit as st

st.header("Hello moi nguoi!")
num = st.text_input("Nhập một con số bạn yêu thích")
don_vi_can_nang = st.radio("chọn đơn vị chiều cao", options=["a","b","c"])
def calculate():
    st.success("Số yêu thích của bạn là số " + "chẵn" if num%2==0 else "lẻ!" + str(don_vi_can_nang))

if st.button("Calculate BMI"):
    calculate()