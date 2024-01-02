import pickle
import streamlit as st

# membaca model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

# Judul web
st.title('Data Mining Prediksi Diabetes')

# membagi kolom
col1, col2, col3 = st.columns(3)

with col1 :
    Pregnancies = st.text_input ('input nilai Pregnancies')

with col2 :
    Glucose = st.text_input('input nilai Glucose')

with col3 :
    BloodPressure = st.text_input ('input nilai Blood Pressure')

with col1 :
    SkinThickness = st.text_input ('input nilai Skin Thickness')

with col2 :
    Insulin = st.text_input ('input nilai Insulin')

with col3 :
    BMI = st.text_input ('input nilai BMI')

with col1 :
    DiabetesPedigreeFunction = st.text_input ('input nilai Diabetes Pedigree Function')

with col2 :
    Age = st.text_input ('input nilai Age')

# code untuk prediksi 
diab_diagnosis = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi Diabetes') :
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if(diab_prediction[0] == 1):
        diab_diagnosis = 'Pasien Terkena Diabetes'
    else :
        diab_diagnosis = 'Pasien Tidak Terkena Diabetes'
        
    st.success(diab_diagnosis)