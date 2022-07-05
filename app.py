# Point d'entree application flash
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import shap
import plotly.express as px

# Application
st.title('Application Hello World')


#Customer ID selection
st.sidebar.header("**General Info**")

#Loading selectbox
id_client = [1,2,3]
chk_id = st.sidebar.selectbox("Client ID", id_client)
st.sidebar.markdown("<u>Client courant :</u>" + str(chk_id), unsafe_allow_html=True)
### Display of information in the sidebar ###
#Number of loans in the sample
nb_credits = 30
st.sidebar.markdown("<u>Number of loans in the sample :</u>", unsafe_allow_html=True)
st.sidebar.text(nb_credits)


#PieChart
#st.sidebar.markdown("<u>......</u>", unsafe_allow_html=True)
targets = [0.98, 0.02]
fig, ax = plt.subplots(figsize=(5,5))
plt.pie(targets, explode=[0, 0.1], labels=['No default', 'Default'], autopct='%1.1f%%', startangle=90)
st.sidebar.pyplot(fig)


 #######################################
    # HOME PAGE - MAIN CONTENT
    #######################################
    #Display Customer ID from Sidebar
st.write("Customer ID selection :", chk_id)

if st.checkbox("Show customer information ?"):
    st.write("Affichage client")