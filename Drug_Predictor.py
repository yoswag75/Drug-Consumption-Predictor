import streamlit as st
import pandas as pd

data=pd.read_csv("C:\\Users\\yugra\\OneDrive\\Desktop\\Drug\\Drug_Consumption_Quantified.csv")

st.title('Drug Consumption Predictor')

nav=st.sidebar.radio("Navigation",["Home","Drug Prediction","Our Team"])

if nav=="Home":
    
    st.markdown(""" # """)
    st.header("Registration Page")
    st.image("https://png.pngtree.com/png-vector/20191110/ourmid/pngtree-avatar-icon-profile-icon-member-login-vector-isolated-png-image_1978396.jpg",width=150)
    if st.button("Register",type="primary"):
        name=st.text_input("Name")
        pass1=st.text_input("Password", type="password")
        pass2=st.text_input("Retype your Password", type="password")
        st.button("Submit")
        
    elif st.button("Login"):
        name_l=st.text_input("Name")
        pass_l=st.text_input("Password", type="password")
        st.button("Submit")         
    
elif nav=="Drug Prediction":
    st.markdown(""" # """)
    st.header("Drug Predictor")
    if st.checkbox("Show Drugs DataSet"):
        st.table(data)
    
    st.markdown(""" # """)
    st.markdown(""" # """)
    st.subheader("Enter the Model Details :")
    st.header("")
    st.text_input("Age")
    st.text_input("Gender")
    st.text_input("Education")
    st.text_input("Country")
    st.text_input("Ethnicity")
    st.text_input("Nscore")
    st.text_input("Escore")
    st.text_input("Oscore")
    st.text_input("AScore")
    st.text_input("cscore")
    st.text_input("Impulsive")
    st.text_input("SS")
    st.text_input("Coke")
    st.text_input("Meth")
    st.text_input("Heroin")
    st.text_input("Nicotin")
    st.button("Submit")
    st.markdown(""" # """)
    st.subheader("The Accuracy of Model is 0.99")
    
elif nav=="Our Team":
    st.markdown(""" # """)
    st.image("https://www.businessmanager.in/wp-content/uploads/2022/04/Effective-Team-Work.jpg")
    st.markdown(""" # """)
    st.subheader("Team Lead and Developer:")
    st.markdown(""" ## D Yuva""")
    st.markdown(""" # """)
    st.subheader("Developer:")
    st.markdown(""" ## Nethish Kumar C D""")
    st.markdown(""" # """)
    st.subheader("QA and Front End Designer:")
    st.markdown(""" ## Yug Raithatha""")