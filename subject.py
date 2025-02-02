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
def graph_class(file1,file2):
 username = st.session_state.get('username')
 df_semester1 = pd.read_csv(f"./uploads/{username}/{file1}")
 df_semester2 = pd.read_csv(f"./uploads/{username}/{file2}")
#  df_combined = pd.concat([df_semester1, df_semester2], ignore_index=True)
#  dfs=[]ś
#  dfs.append(df_semester1,df_semester2)
 concatenated_df = pd.concat([df_semester1, df_semester2], ignore_index=True)
    
 st.header("Line chart for both Sem:")
 fig, ax = plt.subplots()
 for df, semester_name in zip([df_semester1, df_semester2], ['SEM1', 'SEM2']):
       ax.plot(df['RollNo'], df['Total'], label=f'{semester_name} - Total')  # Assuming 'Total' is the column name for marks
 ax.set_xlabel('X-axis Label')
 ax.set_ylabel('Y-axis Label')
 ax.legend()
 fig.set_size_inches(8, 4)
    # Display the plot
 st.pyplot(fig)
 

 st.header("Bar graph :")
 first_roll_no = df_semester1['RollNo'].iloc[0]
 last_roll_no = df_semester1['RollNo'].iloc[-1]
 st.write(f"RollNo range starts from {first_roll_no} - {last_roll_no}")
 
 col21,col22= st.columns(2)
 with col21:
  roll_number1 = st.text_input("Starting Roll Number:")
 with col22:
  roll_number2 = st.text_input("Ending Roll Number:")

 if st.button("Search"):
  try:
    
    roll_number1 = int(roll_number1)
    roll_number2 = int(roll_number2)
    merged_df = pd.merge(df_semester1, df_semester2, on='RollNo', suffixes=('_SEM4', '_SEM5'))

# Filter the DataFrame to include only the rows with 'RollNo' from 20 to 30
    filtered_df = merged_df[(merged_df['RollNo'] >= roll_number1) & (merged_df['RollNo'] <= roll_number2)]

# Plot grouped bar graph
    st.write(f"Grouped bar graph for both semesters (RollNo: {roll_number1}-{roll_number2}):")
    fig, ax = plt.subplots()
    x = filtered_df['RollNo']
    bar_width = 0.3
    bar1=ax.bar(x - bar_width/2, filtered_df['Total_SEM4'], bar_width, label='SEM4')  
    bar2=ax.bar(x + bar_width/2, filtered_df['Total_SEM5'], bar_width, label='SEM5')
    for bar in [bar1, bar2]:
     for rect in bar:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
    ax.set_xlabel('Roll Number')
    ax.set_ylabel('Total Marks')
    ax.set_title('Total Marks Comparison - Semester 4 vs Semester 5 (RollNo: 20-30)')
    ax.set_xticks(x)
    ax.set_xticklabels(x)
    ax.legend()
    fig.set_size_inches(10, 6)
# Display the plot
    st.pyplot(fig)

                      
  except ValueError:
    st.error("Please enter a valid roll number.")
 else:
    st.write("Press the 'Search' button to find results.")




def categorize_students(df,a):
    # Define criteria for each category based on marks
    criteria = {
        'Distinction': (90, 100),
        'First Class': (75, 89),
        'Second Class': (60, 74),
        'Pass': (40, 59),
        'Fail': (0, 39)
    }
    category_count = {category: ((df[a] >= min_mark) & (df[a] <= max_mark)).sum() 
                      for category, (min_mark, max_mark) in criteria.items()}

    return category_count

def plot_distribution(category_count,sub):
    # Plot bar chart
    fig, ax = plt.subplots()
    ax.bar(category_count.keys(), category_count.values(), color=['green', 'blue', 'yellow', 'orange', 'red'])
    ax.set_ylabel('Number of Students')
    ax.set_xlabel('Grade')
    ax.set_title(f' {sub} Grade Analysis')
    ax.grid(axis='y')

    # Display counts on top of each bar
    for i, v in enumerate(category_count.values()):
        ax.text(i, v + 0.1, str(v), ha='center')

    plt.xticks(rotation=45)
    st.pyplot(fig)


def categorize_students_1(df,a):
    # Define criteria for each category based on marks
    criteria = {
        
        'First Class': (21, 25),

        'Pass': (10, 20),
        'Fail': (0, 9)
    }
    category_count = {category: ((df[a] >= min_mark) & (df[a] <= max_mark)).sum() 
                      for category, (min_mark, max_mark) in criteria.items()}

    return category_count

def plot_distribution_1(category_count,sub):
    # Plot bar chart
    fig, ax = plt.subplots()
    ax.bar(category_count.keys(), category_count.values(), color=['green', 'blue', 'red'])
    ax.set_ylabel('Number of Students')
    ax.set_xlabel('Grade')
    ax.set_title(f' {sub} Grade Analysis')
    ax.grid(axis='y')

    # Display counts on top of each bar
    for i, v in enumerate(category_count.values()):
        ax.text(i, v + 0.1, str(v), ha='center')

    plt.xticks(rotation=45)
    st.pyplot(fig)


def graph_sub(path):
              
              selected2 = option_menu(
               menu_title=None,
               options=["Lab","Subject", "Individual"],
               icons=["bar-chart-fill","bar-chart-fill", "bar-chart-fill"],
               menu_icon="cast",
               default_index=0,
               orientation="horizontal",
               )
              if selected2=="Lab":
                username = st.session_state.get('username')
                df = pd.read_csv(f"./uploads/{username}/{path}")
                column_names = [col for col in df.columns if "PR" in col]
                options = ["None"] + column_names
                choice_sub = st.selectbox('Select class', options)
                if choice_sub== options[1]:
                    col_name=f"{options[1]}"
                    cat1=categorize_students_1(df,col_name) 
                    plot_distribution_1(cat1,choice_sub)
                if choice_sub== options[2]:
                    col_name=f"{options[2]}"
                    cat1=categorize_students_1(df,col_name) 
                    plot_distribution_1(cat1,choice_sub)
                if choice_sub== options[3]:
                    col_name=f"{options[3]}"
                    cat1=categorize_students_1(df,col_name) 
                    plot_distribution_1(cat1,choice_sub)
                if choice_sub== options[4]:
                    col_name=f"{options[4]}"
                    cat1=categorize_students_1(df,col_name) 
                    plot_distribution_1(cat1,choice_sub)

               
              if selected2=="Subject":
                  username = st.session_state.get('username')
                  
                  df = pd.read_csv(f"./uploads/{username}/{path}")
                  column_names = [col for col in df.columns if "TH" in col]
                  options = ["None"] + column_names
                  choice_sub = st.selectbox('Select class', options)
                  if choice_sub== options[1]:
                    col_name=f"{options[1]}"
                    cat1=categorize_students(df,col_name) 
                    plot_distribution(cat1,choice_sub)
                  if choice_sub== options[2]:
                    col_name=f"{options[2]}"
                    cat1=categorize_students(df,col_name) 
                    plot_distribution(cat1,choice_sub)
                  if choice_sub== options[3]:
                    col_name=f"{options[3]}"
                    cat1=categorize_students(df,col_name) 
                    plot_distribution(cat1,choice_sub)
                  if choice_sub== options[4]:
                    col_name=f"{options[4]}"
                    cat1=categorize_students(df,col_name) 
                    plot_distribution(cat1,choice_sub)
                  if choice_sub== options[5]:
                    col_name=f"{options[5]}"
                    cat1=categorize_students(df,col_name) 
                    plot_distribution(cat1,choice_sub)
                  if choice_sub== options[6]:
                    col_name=f"{options[6]}"
                    cat1=categorize_students(df,col_name) 
                    plot_distribution(cat1,choice_sub)
                  if choice_sub== options[7]:
                    col_name=f"{options[7]}"
                    cat1=categorize_students(df,col_name) 
                    plot_distribution(cat1,choice_sub)
                  if choice_sub== options[7]:
                    col_name=f"{options[7]}"
                    cat1=categorize_students(df,col_name) 
                    plot_distribution(cat1,choice_sub)
                  
                  
                  

              if selected2=="Individual":
                 username = st.session_state.get('username')
                 df = pd.read_csv(f"./uploads/{username}/{path}")

 
                 first_roll_no = df['RollNo'].iloc[0]
                 last_roll_no = df['RollNo'].iloc[-1]
                 st.write(f"RollNo range starts from {first_roll_no} - {last_roll_no}")
 
                 string_number = st.text_input("Enter Roll Number:")
                 roll_no = int(string_number)

                 if st.button("Search"):
                  try:

                    roll_data = df[df['RollNo'] == int(roll_no)]
                    if not roll_data.empty:
    # Define colors for the bars
                       colors = ['skyblue', 'lightgreen', 'salmon', 'lightcoral', 'lightskyblue', 'plum','lightcoral', 'lightskyblue', 'plum'] 

    # Plot bar graph for each subject's marks
                       st.write(f"Bar graph for Roll Number {roll_no}:")
                       fig, ax = plt.subplots(figsize=(10, 6))
                       subjects = [col for col in roll_data.columns if any(substring in col for substring in ["PR", "OR", "TW"])]
                       marks = roll_data.iloc[0][subjects]
                       for i, (sub, mark) in enumerate(zip(subjects, marks)):
                         ax.bar(sub, mark, color=colors[i], label=f'{mark}',  edgecolor='black')
                         ax.text(sub, mark + 2, str(mark), ha='center', va='bottom', fontweight='bold')
                       ax.set_xlabel('Subjects')
                       ax.set_ylabel('Marks')
                       ax.set_title(f'Marks for Roll Number {roll_no}')
                       ax.grid(axis='y')
                       ax.legend(title='Marks')
                       st.pyplot(fig)


                       colors1 = ['skyblue', 'lightgreen', 'salmon', 'lightcoral', 'lightskyblue', 'plum','lightcoral'] 

    # Plot bar graph for each subject's marks
                       st.write(f"Bar graph for Roll Number {roll_no}:")
                       fig, ax = plt.subplots(figsize=(10, 6))
                       subjects = [col for col in roll_data.columns if any(substring in col for substring in ["TH"])]
                       marks = roll_data.iloc[0][subjects]
                       for i, (sub, mark) in enumerate(zip(subjects, marks)):
                         ax.bar(sub, mark, color=colors1[i], label=f'{mark}',  edgecolor='black')
                         ax.text(sub, mark + 2, str(mark), ha='center', va='bottom', fontweight='bold')
                       ax.set_xlabel('Subjects')
                       ax.set_ylabel('Marks')
                       ax.set_title(f'Marks for Roll Number {roll_no}')
                       ax.grid(axis='y')
                       ax.legend(title='Marks')
                       st.pyplot(fig)


                       col1,col2=st.columns(2)

                       with col1:   
                          st.write(roll_data.iloc[0])

                       with col2:
                           
                           st.write("hello this is where you should improve")
                    else:
                       st.write("No data found for the given roll number.")
                  except ValueError:
                      st.error("Please enter a valid roll number.")
                 else:
                  st.write("Press the 'Search' button to find results.")


def file_selection_page():
          col1,col2= st.columns(2)
         
         
         
          with col1:
           choice = st.selectbox('select Department',['None','IT','COMP','E&TC'])
         
#*************************************************IT*******************************************************************         
           if choice == "IT":
               with col2:
                choice1 = st.selectbox('select class',['None','SE','TE','BE']) 
               
                if choice1=="SE":
                    with col1:
                        choice11 = st.selectbox('select Division',['None','DIV A','DIV B','DIV C']) 
                        if choice11 =="DIV A":
                            with col2: 
                                choice111=st.selectbox("select Trerm",['Both Term','First Term','Second Term'])
                        if choice11 =="DIV B":
                            with col2: 
                                choice112=st.selectbox("select Trerm",['Both Term','First Term','Second Term'])
                        if choice11 =="DIV C":
                            with col2: 
                                choice113=st.selectbox("select Trerm",['Both Term','First Term','Second Term'])        
                
                
                
                if choice1=="TE":
                    with col1:
                        choice12 = st.selectbox('select Division',['None','DIV A','DIV B','DIV C']) 
                        if choice12 =="DIV A":
                            with col2: 
                                choice121=st.selectbox("select Trerm",['Both Term','First Term','Second Term'])
                        if choice12 =="DIV B":
                            with col2: 
                                choice122=st.selectbox("select Trerm",['Both Term','First Term','Second Term'])
                        if choice12 =="DIV C":
                            with col2: 
                                choice123=st.selectbox("select Trerm",['Both Term','First Term','Second Term'])        
                                
                if choice1=="BE":
                    with col1:
                        choice13 = st.selectbox('select Division',['None','DIV A','DIV B','DIV C']) 
                        if choice13 =="DIV A":
                            with col2: 
                                choice131=st.selectbox("select Trerm",['Both Term','First Term','Second Term'])
                        if choice13 =="DIV B":
                            with col2: 
                                choice132=st.selectbox("select Trerm",['Both Term','First Term','Second Term'])
                        if choice13 =="DIV C":
                            with col2: 
                                choice133=st.selectbox("select Trerm",['Both Term','First Term','Second Term'])

#*************************************************COMP*******************************************************************         

           if  choice == "COMP":
               with col2:
                   choice2 = st.selectbox('select class',['None','SE','TE','BE'])   
                   if choice2=="SE":
                    with col1:
                        choice21 = st.selectbox('select Division',['None','DIV A','DIV B','DIV C']) 
                        if choice21 =="DIV A":
                            with col2: 
                                choice211=st.selectbox("select Trerm",['Both Term','First Term','Second Term'])
                        if choice21 =="DIV B":
                            with col2: 
                                choice212=st.selectbox("select Trerm",['Both Term','First Term','Second Term'])
                        if choice21 =="DIV C":
                            with col2: 
                                choice213=st.selectbox("select Trerm",['Both Term','First Term','Second Term'])        

                   if choice2=="TE":
                    with col1:
                        choice22 = st.selectbox('select Division',['None','DIV A','DIV B','DIV C']) 
                        if choice22 =="DIV A":
                            with col2: 
                                choice221=st.selectbox("select Trerm",['Both Term','First Term','Second Term'])
                        if choice22 =="DIV B":
                            with col2: 
                                choice222=st.selectbox("select Trerm",['Both Term','First Term','Second Term'])
                        if choice22 =="DIV C":
                            with col2: 
                                choice223=st.selectbox("select Trerm",['Both Term','First Term','Second Term'])        
                   
                   
                   
                   if choice2=="BE":
                    with col1:
                        choice23 = st.selectbox('select Division',['None','DIV A','DIV B','DIV C']) 
                        if choice23 =="DIV A":
                            with col2: 
                                choice231=st.selectbox("select Trerm",['Both Term','First Term','Second Term'])
                        if choice23 =="DIV B":
                            with col2: 
                                choice232=st.selectbox("select Trerm",['Both Term','First Term','Second Term'])
                        if choice23 =="DIV C":
                            with col2: 
                                choice233=st.selectbox("select Trerm",['Both Term','First Term','Second Term'])
         
#*************************************************E&TC*******************************************************************         
       
           if  choice == "E&TC":
               with col2:
                   choice3 = st.selectbox('select class',['None','SE','TE','BE'])   
                   if choice3=="SE":
                    with col1:
                        choice31 = st.selectbox('select Division',['None','DIV A','DIV B','DIV C']) 
                        if choice31 =="DIV A":
                            with col2: 
                                choice311=st.selectbox("select Trerm",['Both Term','First Term','Second Term'])
                        if choice31 =="DIV B":
                            with col2: 
                                choice312=st.selectbox("select Trerm",['Both Term','First Term','Second Term'])
                        if choice31 =="DIV C":
                            with col2: 
                                choice313=st.selectbox("select Trerm",['Both Term','First Term','Second Term'])        
                   
                   
                   if choice3=="TE":
                    with col1:
                        choice32 = st.selectbox('select Division',['None','DIV A','DIV B','DIV C']) 
                        if choice32 =="DIV A":
                            with col2: 
                                choice321=st.selectbox("select Trerm",['Both Term','First Term','Second Term'])
                        if choice32 =="DIV B":
                            with col2: 
                                choice322=st.selectbox("select Trerm",['Both Term','First Term','Second Term'])
                        if choice32 =="DIV C":
                            with col2: 
                                choice323=st.selectbox("select Trerm",['Both Term','First Term','Second Term'])        
                   
                   if choice3=="BE":
                    with col1:
                        choice33 = st.selectbox('select Division',['None','DIV A','DIV B','DIV C']) 
                        if choice33 =="DIV A":
                            with col2: 
                                choice331=st.selectbox("select Trerm",['Both Term','First Term','Second Term'])
                        if choice33 =="DIV B":
                            with col2: 
                                choice332=st.selectbox("select Trerm",['Both Term','First Term','Second Term'])
                        if choice33 =="DIV C":
                            with col2: 
                                choice333=st.selectbox("select Trerm",['Both Term','First Term','Second Term'])
                            



#*************************************************IT******************************************************************         
          
 

  #****************************SE******************
          if "choice111" in locals() and choice111 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_IT_SE9_SEM1.csv"
              graph_sub(path_sub)
          if "choice111" in locals() and choice111 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_IT_SE9_SEM2.csv"
              graph_sub(path_sub)
          if  "choice111" in locals() and choice111 == "Both Term":
              username = st.session_state.get('username')
              f1=f"{username}_IT_SE9_SEM1.csv" 
              f2=f"{username}_IT_SE9_SEM2.csv" 
              graph_class(f1,f2)



          if "choice112" in locals() and choice112 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_IT_SE10_SEM1.csv"
              graph_sub(path_sub)
          if "choice112" in locals() and choice112 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_IT_SE10_SEM2.csv"
              graph_sub(path_sub)
          if  "choice112" in locals() and choice112 == "Both Term":
              username = st.session_state.get('username')
              f1=f"{username}_IT_SE10_SEM1.csv" 
              f2=f"{username}_IT_SE10_SEM2.csv" 
              graph_class(f1,f2) 


          if "choice113" in locals() and choice113 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_IT_SE11_SEM1.csv"
              graph_sub(path_sub)
          if "choice113" in locals() and choice113 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_IT_SE11_SEM2.csv"
              graph_sub(path_sub)
          if  "choice113" in locals() and choice113 == "Both Term":
              username = st.session_state.get('username')
              f1=f"{username}_IT_SE9_SEM1.csv" 
              f2=f"{username}_IT_SE9_SEM2.csv" 
              graph_class(f1,f2) 


 #****************************TE****************************************************
          if "choice121" in locals() and choice121 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_IT_TE9_SEM1.csv"
              graph_sub(path_sub)
          if "choice121" in locals() and choice121 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_IT_TE9_SEM2.csv"
              graph_sub(path_sub)
          if  "choice121" in locals() and choice121 == "Both Term":
              username = st.session_state.get('username')
              f1=f"{username}_IT_SE9_SEM1.csv" 
              f2=f"{username}_IT_SE9_SEM2.csv" 
              graph_class(f1,f2) 


          if "choice122" in locals() and choice122 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_IT_TE10_SEM1.csv"
              graph_sub(path_sub)
          if "choice122" in locals() and choice122 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_IT_TE10_SEM2.csv"
              graph_sub(path_sub)
          if  "choice122" in locals() and choice122 == "Both Term":
              username = st.session_state.get('username')
              f1=f"{username}_IT_SE9_SEM1.csv" 
              f2=f"{username}_IT_SE9_SEM2.csv" 
              graph_class(f1,f2) 

          if "choice123" in locals() and choice123 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_IT_TE11_SEM1.csv"
              graph_sub(path_sub)
          if "choice123" in locals() and choice123 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_IT_TE11_SEM2.csv"
              graph_sub(path_sub)
          if  "choice123" in locals() and choice123 == "Both Term":
              username = st.session_state.get('username')
              f1=f"{username}_IT_SE9_SEM1.csv" 
              f2=f"{username}_IT_SE9_SEM2.csv" 
              graph_class(f1,f2) 
               
 #****************************BE***********************************************************
          if "choice131" in locals() and choice131 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_IT_BE9_SEM1.csv"
              graph_sub(path_sub)
          if "choice131" in locals() and choice131 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_IT_BE9_SEM2.csv"
              graph_sub(path_sub)
          if  "choice131" in locals() and choice131 == "Both Term":
              username = st.session_state.get('username')
              f1=f"{username}_IT_SE9_SEM1.csv" 
              f2=f"{username}_IT_SE9_SEM2.csv" 
              graph_class(f1,f2) 

          if "choice132" in locals() and choice132 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_IT_BE10_SEM1.csv"
              graph_sub(path_sub)
          if "choice132" in locals() and choice132 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_IT_BE10_SEM2.csv"
              graph_sub(path_sub)
          if  "choice132" in locals() and choice132 == "Both Term":
              username = st.session_state.get('username')
              f1=f"{username}_IT_SE9_SEM1.csv" 
              f2=f"{username}_IT_SE9_SEM2.csv" 
              graph_class(f1,f2) 

          if "choice133" in locals() and choice133 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_IT_BE11_SEM1.csv"
              graph_sub(path_sub)
          if "choice133" in locals() and choice133 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_IT_BE11_SEM2.csv"
              graph_sub(path_sub)
          if  "choice133" in locals() and choice133== "Both Term":
              username = st.session_state.get('username')
              f1=f"{username}_IT_SE9_SEM1.csv" 
              f2=f"{username}_IT_SE9_SEM2.csv" 
              graph_class(f1,f2) 
                


#***************************************COMP***********************************                
          #****************************SE******************
          if "choice211" in locals() and choice211 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_COMP_SE9_SEM1.csv"
              graph_sub(path_sub)
          if "choice211" in locals() and choice211 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_COMP_SE9_SEM2.csv"
              graph_sub(path_sub)
          if  "choice211" in locals() and choice211 == "Both Term":
              username = st.session_state.get('username')
              f1=f"{username}_IT_SE9_SEM1.csv" 
              f2=f"{username}_IT_SE9_SEM2.csv" 
              graph_class(f1,f2) 


          if "choice212" in locals() and choice212 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_COMP_SE10_SEM1.csv"
              graph_sub(path_sub)
          if "choice212" in locals() and choice212 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_COMP_SE10_SEM2.csv"
              graph_sub(path_sub)
          if  "choice212" in locals() and choice212 == "Both Term":
              username = st.session_state.get('username')
              f1=f"{username}_IT_SE9_SEM1.csv" 
              f2=f"{username}_IT_SE9_SEM2.csv" 
              graph_class(f1,f2) 

          if "choice213" in locals() and choice213 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_COMP_SE11_SEM1.csv"
              graph_sub(path_sub)
          if "choice213" in locals() and choice213 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_COMP_SE11_SEM2.csv"
              graph_sub(path_sub)
          if  "choice213" in locals() and choice213 == "Both Term":
              username = st.session_state.get('username')
              f1=f"{username}_IT_SE9_SEM1.csv" 
              f2=f"{username}_IT_SE9_SEM2.csv" 
              graph_class(f1,f2) 

 #****************************TE******************
          if "choice221" in locals() and choice221 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_COMP_TE9_SEM1.csv"
              graph_sub(path_sub)
          if "choice221" in locals() and choice221 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_COMP_TE9_SEM2.csv"
              graph_sub(path_sub)
          if  "choice221" in locals() and choice221 == "Both Term":
              username = st.session_state.get('username')
              f1=f"{username}_IT_SE9_SEM1.csv" 
              f2=f"{username}_IT_SE9_SEM2.csv" 
              graph_class(f1,f2)


          if "choice222" in locals() and choice222 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_COMP_TE10_SEM1.csv"
              graph_sub(path_sub)
          if "choice222" in locals() and choice222 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_COMP_TE10_SEM2.csv"
              graph_sub(path_sub)
          if  "choice222" in locals() and choice222 == "Both Term":
              username = st.session_state.get('username')
              f1=f"{username}_IT_SE9_SEM1.csv" 
              f2=f"{username}_IT_SE9_SEM2.csv" 
              graph_class(f1,f2)


          if "choice223" in locals() and choice223 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_COMP_TE11_SEM1.csv"
              graph_sub(path_sub)
          if "choice223" in locals() and choice223 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_COMP_TE11_SEM2.csv"
              graph_sub(path_sub)
          if  "choice223" in locals() and choice223 == "Both Term":
              username = st.session_state.get('username')
              f1=f"{username}_IT_SE9_SEM1.csv" 
              f2=f"{username}_IT_SE9_SEM2.csv" 
              graph_class(f1,f2)

               
 #****************************BE******************
          if "choice231" in locals() and choice231 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_COMP_BE9_SEM1.csv"
              graph_sub(path_sub)
          if "choice231" in locals() and choice231 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_COMP_BE9_SEM2.csv"
              graph_sub(path_sub)
          if  "choice231" in locals() and choice231 == "Both Term":
              username = st.session_state.get('username')
              f1=f"{username}_IT_SE9_SEM1.csv" 
              f2=f"{username}_IT_SE9_SEM2.csv" 
              graph_class(f1,f2) 


          if "choice232" in locals() and choice232 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_COMP_BE10_SEM1.csv"
              graph_sub(path_sub)
          if "choice232" in locals() and choice232 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_COMP_BE10_SEM2.csv"
              graph_sub(path_sub)
          if  "choice232" in locals() and choice232 == "Both Term":
              username = st.session_state.get('username')
              f1=f"{username}_IT_SE9_SEM1.csv" 
              f2=f"{username}_IT_SE9_SEM2.csv" 
              graph_class(f1,f2) 

          if "choice233" in locals() and choice233 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_COMP_BE11_SEM1.csv"
              graph_sub(path_sub)
          if "choice233" in locals() and choice233 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_COMP_BE11_SEM2.csv"
              graph_sub(path_sub)
          if  "choice233" in locals() and choice233 == "Both Term":
              username = st.session_state.get('username')
              f1=f"{username}_IT_SE9_SEM1.csv" 
              f2=f"{username}_IT_SE9_SEM2.csv" 
              graph_class(f1,f2)                 





#***************************************E&TC***********************************                
          #****************************SE******************
          if "choice311" in locals() and choice311 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_E&TC_SE9_SEM1.csv"
              graph_sub(path_sub)
          if "choice311" in locals() and choice311 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_E&TC_SE9_SEM2.csv"
              graph_sub(path_sub)
          if  "choice311" in locals() and choice311 == "Both Term":
              username = st.session_state.get('username')
              f1=f"{username}_IT_SE9_SEM1.csv" 
              f2=f"{username}_IT_SE9_SEM2.csv" 
              graph_class(f1,f2) 


          if "choice312" in locals() and choice312 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_E&TC_SE10_SEM1.csv"
              graph_sub(path_sub)
          if "choice312" in locals() and choice312 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_E&TC_SE10_SEM2.csv"
              graph_sub(path_sub)
          if  "choice312" in locals() and choice312 == "Both Term":
              username = st.session_state.get('username')
              f1=f"{username}_IT_SE9_SEM1.csv" 
              f2=f"{username}_IT_SE9_SEM2.csv" 
              graph_class(f1,f2) 

          if "choice313" in locals() and choice313 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_E&TC_SE11_SEM1.csv"
              graph_sub(path_sub)
          if "choice313" in locals() and choice313 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_E&TC_SE11_SEM2.csv"
              graph_sub(path_sub)
          if  "choice313" in locals() and choice313 == "Both Term":
              username = st.session_state.get('username')
              f1=f"{username}_IT_SE9_SEM1.csv" 
              f2=f"{username}_IT_SE9_SEM2.csv" 
              graph_class(f1,f2)

 #****************************TE**********************************************
          if "choice321" in locals() and choice321 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_E&TC_TE9_SEM1.csv"
              graph_sub(path_sub)
          if "choice321" in locals() and choice321 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_E&TC_TE9_SEM2.csv"
              graph_sub(path_sub)
          if  "choice321" in locals() and choice321 == "Both Term":
              username = st.session_state.get('username')
              f1=f"{username}_IT_SE9_SEM1.csv" 
              f2=f"{username}_IT_SE9_SEM2.csv" 
              graph_class(f1,f2)
         


          if "choice322" in locals() and choice322 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_E&TC_TE10_SEM1.csv"
              graph_sub(path_sub)
          if "choice322" in locals() and choice322 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_E&TC_TE10_SEM2.csv"
              graph_sub(path_sub)
          if  "choice322" in locals() and choice322 == "Both Term":
              username = st.session_state.get('username')
              f1=f"{username}_IT_SE9_SEM1.csv" 
              f2=f"{username}_IT_SE9_SEM2.csv" 
              graph_class(f1,f2) 
 

          if "choice323" in locals() and choice323 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_E&TC_TE11_SEM1.csv"
              graph_sub(path_sub)
          if "choice323" in locals() and choice323 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_E&TC_TE11_SEM2.csv"
              graph_sub(path_sub)
          if  "choice323" in locals() and choice323 == "Both Term":
              username = st.session_state.get('username')
              f1=f"{username}_IT_SE9_SEM1.csv" 
              f2=f"{username}_IT_SE9_SEM2.csv" 
              graph_class(f1,f2)
               
 #****************************BE*********************************************
          if "choice331" in locals() and choice331 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_E&TC_BE9_SEM1.csv"
              graph_sub(path_sub)
          if "choice331" in locals() and choice331 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_E&TC_BE9_SEM2.csv"
              graph_sub(path_sub)
          if  "choice331" in locals() and choice331 == "Both Term":
              username = st.session_state.get('username')
              f1=f"{username}_IT_SE9_SEM1.csv" 
              f2=f"{username}_IT_SE9_SEM2.csv" 
              graph_class(f1,f2) 


          if "choice332" in locals() and choice332 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_E&TC_BE10_SEM1.csv"
              graph_sub(path_sub)
          if "choice332" in locals() and choice332 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_E&TC_BE10_SEM2.csv"
              graph_sub(path_sub)
          if  "choice332" in locals() and choice332 == "Both Term":
              username = st.session_state.get('username')
              f1=f"{username}_IT_SE9_SEM1.csv" 
              f2=f"{username}_IT_SE9_SEM2.csv" 
              graph_class(f1,f2) 

          if "choice333" in locals() and choice333 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_E&TC_BE11_SEM1.csv"
              graph_sub(path_sub)
          if "choice333" in locals() and choice333 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_E&TC_BE11_SEM2.csv"
              graph_sub(path_sub)
          if  "choice333" in locals() and choice333 == "Both Term":
              username = st.session_state.get('username')
              f1=f"{username}_IT_SE9_SEM1.csv" 
              f2=f"{username}_IT_SE9_SEM2.csv" 
              graph_class(f1,f2) 

def app():
     try:
        
     #    st.set_option('deprecation.showPyplotGlobalUse', False)
        st.title('Track Students Progress')

        if st.session_state.get('username'):
          st.caption("Gain insights into student :blue[_achievements_] and areas for :blue[_improvement_] :chart: ")
          file_selection_page() 





        else:
             st.write("Please Login")
     except:
        if st.session_state.username=='':
            st.text('Please Login First')        

















































