import streamlit as st
import os
import pickle
from pathlib import Path
from firebase_admin import firestore
from streamlit_option_menu import option_menu
import streamlit_authenticator as stauth

import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt
import pandas as pd

def preprocess_data(df):
    # Example preprocessing steps:
    # Rename columns if needed
    df.replace({'FF': 0, 'AB': 0}, inplace=True)
    # Replace NaN values with 0
    df.fillna(0, inplace=True)
    return df

def upload_files_sem(dept,div):
            uploaded_file_1 = st.file_uploader("upload a file for First semester ",type=["csv"])
            f2= st.session_state.get('username')
            save_directory=f"uploads/{f2}"
            if uploaded_file_1 is not None:
             os.makedirs(save_directory,exist_ok=True)

             f2= st.session_state.get('username')
             
             new_file_name=f"{f2}_{dept}_{div}_SEM1.csv"
             file_path=os.path.join(save_directory,new_file_name)
             try:
              df = pd.read_csv(uploaded_file_1)

        # Preprocess the data
              df1 = preprocess_data(df)
              df1.to_csv(file_path, index=False)
              st.success(f"File saved ")
             except:
                  st.error(f"please choose a appropriate file or file format")
            

            uploaded_file_2 = st.file_uploader("upload a file for second semester",type=["csv"])
            f2= st.session_state.get('username')
            save_directory=f"uploads/{f2}"
            if uploaded_file_2 is not None:
             os.makedirs(save_directory,exist_ok=True)

             f2= st.session_state.get('username')
             
             new_file_name=f"{f2}_{dept}_{div}_SEM2.csv"
             file_path=os.path.join(save_directory,new_file_name)
             try:
              df = pd.read_csv(uploaded_file_2)

        # Preprocess the data
              df1 = preprocess_data(df)
              df1.to_csv(file_path, index=False)
              st.success(f"File saved ")
             except:
                  st.error(f"please choose a appropriate file or file format") 

def app():
     try:
        
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.write('Posted by: '+st.session_state['username'] )
        st.title('upload files')

        if st.session_state.get('username'):
          
         
         
         
          selected = option_menu(
           menu_title=None,
           options=["Department","IT","COMP","E&TC","View More"],
           icons=["bookmark-fill","bar-chart-fill","bar-chart-fill","bar-chart-fill","arrow-right-square-fill"],
           menu_icon="cast",
           default_index=0,
           orientation="horizontal",
           )
          
         
#*************************************************IT*******************************************************************         
          if selected == 'IT':
           selected1 = option_menu(
           menu_title=None,
           options=["class","SE","TE","BE"],
           menu_icon="cast",
           default_index=0,
           orientation="horizontal",
           )
           if selected1== "SE":
             choice11 = option_menu(
             menu_title=None,
             options=["class",'DIV A','DIV B','DIV C'],
             menu_icon="cast",
             default_index=0,
             orientation="horizontal",
             )
           if selected1== "TE":
             choice12 = option_menu(
             menu_title=None,
             options=["class",'DIV A','DIV B','DIV C'],
             menu_icon="cast",
             default_index=0,
             orientation="horizontal",
             )
           if selected1== "BE":
             choice13 = option_menu(
             menu_title=None,
             options=["class",'DIV A','DIV B','DIV C'],
             menu_icon="cast",
             default_index=0,
             orientation="horizontal",
             )





          if selected == 'COMP':
           selected1 = option_menu(
           menu_title=None,
           options=["class","SE","TE","BE"],
           menu_icon="cast",
           default_index=0,
           orientation="horizontal",
           )
           if selected1== "SE":
             choice21 = option_menu(
             menu_title=None,
             options=["class",'DIV A','DIV B','DIV C'],
             menu_icon="cast",
             default_index=0,
             orientation="horizontal",
             )
           if selected1== "TE":
             choice22 = option_menu(
             menu_title=None,
             options=["class",'DIV A','DIV B','DIV C'],
             menu_icon="cast",
             default_index=0,
             orientation="horizontal",
             )
           if selected1== "BE":
             choice23 = option_menu(
             menu_title=None,
             options=["class",'DIV A','DIV B','DIV C'],
             menu_icon="cast",
             default_index=0,
             orientation="horizontal",
             )







          if selected == 'E&TC':
           selected1 = option_menu(
           menu_title=None,
           options=["class","SE","TE","BE"],
           menu_icon="cast",
           default_index=0,
           orientation="horizontal",
           )
           if selected1== "SE":
             choice31 = option_menu(
             menu_title=None,
             options=["class",'DIV A','DIV B','DIV C'],
             menu_icon="cast",
             default_index=0,
             orientation="horizontal",
             )
           if selected1== "TE":
             choice32 = option_menu(
             menu_title=None,
             options=["class",'DIV A','DIV B','DIV C'],
             menu_icon="cast",
             default_index=0,
             orientation="horizontal",
             )
           if selected1== "BE":
             choice33 = option_menu(
             menu_title=None,
             options=["class",'DIV A','DIV B','DIV C'],
             menu_icon="cast",
             default_index=0,
             orientation="horizontal",
             )











          
 #****************************IT******************
          if "choice11" in locals() and choice11 == "DIV A":
            upload_files_sem('IT','SE9')
          if "choice11" in locals() and choice11 == "DIV B":
            upload_files_sem('IT','SE10')
          if "choice11" in locals() and choice11 == "DIV C":
            upload_files_sem('IT','SE11')
          


          if "choice12" in locals() and choice12 == "DIV A":
            upload_files_sem('IT','TE9')
          if "choice12" in locals() and choice12 == "DIV B":
            upload_files_sem('IT','TE10')
          if "choice12" in locals() and choice12 == "DIV C":
            upload_files_sem('IT','TE11')





          if "choice13" in locals() and choice13 == "DIV A":
            upload_files_sem('IT','BE9')
          if "choice13" in locals() and choice13 == "DIV B":
            upload_files_sem('IT','BE10')
          if "choice13" in locals() and choice13 == "DIV C":
            upload_files_sem('IT','BE11')

          

 #****************************COMP******************
          if "choice21" in locals() and choice21 == "DIV A":
            upload_files_sem('COMP','SE9')
          if "choice21" in locals() and choice21 == "DIV B":
            upload_files_sem('COMP','SE10')
          if "choice21" in locals() and choice21 == "DIV C":
            upload_files_sem('COMP','SE11')


          if "choice22" in locals() and choice22 == "DIV A":
            upload_files_sem('COMP','TE9')
          if "choice22" in locals() and choice22 == "DIV B":
            upload_files_sem('COMP','TE10')
          if "choice22" in locals() and choice22 == "DIV C":
            upload_files_sem('COMP','TE11')

          if "choice23" in locals() and choice23 == "DIV A":
            upload_files_sem('COMP','BE9')
          if "choice23" in locals() and choice23 == "DIV B":
            upload_files_sem('COMP','BE10')
          if "choice23" in locals() and choice23 == "DIV C":
            upload_files_sem('COMP','BE11')


 #****************************E&TC******************

          if "choice31" in locals() and choice31 == "DIV A":
             upload_files_sem('E&TC','SE9')
          if "choice31" in locals() and choice31 == "DIV B":
              upload_files_sem('E&TC','SE10')
          if "choice31" in locals() and choice31 == "DIV C":
              upload_files_sem('E&TC','SE11')


          if "choice32" in locals() and choice32 == "DIV A":
              upload_files_sem('E&TC','TE9')
          if "choice32" in locals() and choice32 == "DIV B":
              upload_files_sem('E&TC','TE10')
          if "choice32" in locals() and choice32 == "DIV C":
              upload_files_sem('E&TC','TE11')


          if "choice33" in locals() and choice33 == "DIV A":
              upload_files_sem('E&TC','BE9')
          if "choice33" in locals() and choice33 == "DIV B":
              upload_files_sem('E&TC','BE10')
          if "choice33" in locals() and choice33 == "DIV C":
              upload_files_sem('E&TC','BE11')




















        else:
             st.write("please login")
     except:
        if st.session_state.username=='':
            st.text('Please Login first')        
    

         
        
   

  
  
