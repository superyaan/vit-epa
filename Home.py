import streamlit as st
import os


from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt 
import pandas as pd 
from io import BytesIO




def class_chart(dept,term):
     try:
             username = st.session_state.get('username')
             df1 = pd.read_csv(f"./uploads/{username}/{username}_{dept}_SE9_{term}.csv")
             df2 = pd.read_csv(f"./uploads/{username}/{username}_{dept}_SE10_{term}.csv")
             df3 = pd.read_csv(f"./uploads/{username}/{username}_{dept}_SE11_{term}.csv")
             df4 = pd.read_csv(f"./uploads/{username}/{username}_{dept}_TE9_{term}.csv")
             df5 = pd.read_csv(f"./uploads/{username}/{username}_{dept}_TE10_{term}.csv")
             df6 = pd.read_csv(f"./uploads/{username}/{username}_{dept}_TE11_{term}.csv")
             df7 = pd.read_csv(f"./uploads/{username}/{username}_{dept}_BE9_{term}.csv")
             df8 = pd.read_csv(f"./uploads/{username}/{username}_{dept}_BE10_{term}.csv")
             df9 = pd.read_csv(f"./uploads/{username}/{username}_{dept}_BE11_{term}.csv")

# Calculate the average of the "Total" column for each pair of files
             average1_2 = (df1["Total"].mean() + df2["Total"].mean()+ df3["Total"].mean()) / 3
             average3_4 = (df4["Total"].mean() + df5["Total"].mean()+ df6["Total"].mean()) / 3
             average5_6 = (df7["Total"].mean() + df8["Total"].mean()+ df9["Total"].mean()) / 3

             averages = [int(average1_2), int(average3_4), int(average5_6)]
             labels = ["SE", "TE", "BE"]

             fig, ax = plt.subplots()
             bars = ax.bar(labels, averages, color='skyblue')

# Add count labels on the bars
             for bar in bars:
              height = bar.get_height()
              ax.annotate('{}'.format(height),
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom')

# Customize plot labels and appearance
             ax.set_ylabel('Marks')
             ax.set_title('Average Marks for Each Class')
             ax.grid(axis='y')


             buffer = BytesIO()
             plt.savefig(buffer, format='png')
             buffer.seek(0)


# Show plot  
             st.pyplot(fig)
             st.download_button(label="Download Graph", data=buffer, file_name="averages.png", mime="image/png")
     except FileNotFoundError:
               st.error('CSV files not found. Please check file is uploaded or not if not please upload files.')     



def preprocess_data(df):
    # Example preprocessing steps:
    # Rename columns if needed
    df.replace({'FF': 0, 'AB': 0}, inplace=True)
    # Replace NaN values with 0
    df.fillna(0, inplace=True)
    return df


def chart_div(path1,path2,path3,div1,div2,div3):
    try: 
     dfTE9 = pd.read_csv(path1)
     dfTE10 = pd.read_csv(path2)
     dfTE11 = pd.read_csv(path3)



        # Check if 'Total' column exists in each DataFrame
     if 'Total' not in dfTE9.columns or 'Total' not in dfTE10.columns or 'Total' not in dfTE11.columns:
       st.error('The "Total" column is missing in one or more CSV files.')
     else:
    # Calculate average total marks for each class
      TE9_avg = dfTE9['Total'].mean()
      TE10_avg = dfTE10['Total'].mean()
      TE11_avg = dfTE11['Total'].mean()

    # Plot bar chart
      fig, ax = plt.subplots()
      bar_data = {div1: int(TE9_avg), div2: int(TE10_avg), div3: int(TE11_avg)}
      bars = ax.bar(bar_data.keys(), bar_data.values(), color='skyblue')

    # Add count labels on the bars
      for bar in bars:
        height = bar.get_height()
        ax.annotate('{}'.format(height),
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

    # Customize plot labels and appearance
      ax.set_ylabel('Average Total Marks')
      ax.set_title('Average Marks')
      ax.grid(axis='y')

    # Show plot
      st.pyplot(fig)
    except FileNotFoundError:
               st.error('CSV files not found. Please check file is uploaded or not if not please upload files.')


def attainment(file_path):
     try:
      st.title('Attainment Calculation')

    # Read the CSV file into a DataFrame
      df = pd.read_csv(file_path)

    # Categorize students based on total marks into specified bins
      bins = [0, 240, 360, 396, df['Total'].max()]
      labels = ['Fail', 'Pass', 'First class', 'Distiction Class']
      df['Total Range'] = pd.cut(df['Total'], bins=bins, labels=labels, right=False)

    # Count the number of students in each category
      count_by_range = df['Total Range'].value_counts().sort_index()

    # Plot bar chart
      st.bar_chart(count_by_range)
     except FileNotFoundError:
               st.error('CSV files not found. Please check file is uploaded or not if not please upload files.')

def dept_upload_file():
          uploaded_file_dept = st.file_uploader("upload a file for IT ",type=["csv"])
          f2= st.session_state.get('username')
          save_directory=f"uploads/{f2}"
          if uploaded_file_dept is not None:
             os.makedirs(save_directory,exist_ok=True)

             
             f2= st.session_state.get('username')
             new_file_name=f"{f2}_IT.csv"
             file_path=os.path.join(save_directory,new_file_name)
             
             try:
              df = pd.read_csv(uploaded_file_dept)

        # Preprocess the data
              df1 = preprocess_data(df)
              df1.to_csv(file_path, index=False)
              st.success(f"File saved ")
             except:
                  st.error(f"please choose a appropriate file or file format")


             
          

          uploaded_file1_dept = st.file_uploader("upload a file for COMP ",type=["csv"])
          if uploaded_file1_dept is not None:
             os.makedirs(save_directory,exist_ok=True)

             f2= st.session_state.get('username')
             
             new_file_name=f"{f2}_COMP.csv"
             file_path=os.path.join(save_directory,new_file_name)
             try:
              df = pd.read_csv(uploaded_file1_dept)

        # Preprocess the data
              df1 = preprocess_data(df)
              df1.to_csv(file_path, index=False)
              st.success(f"File saved ")
             except:
                  st.error(f"please choose a appropriate file or file format")


          uploaded_file2_dept = st.file_uploader("upload a file for ENTC ",type=["csv"]) 
          if uploaded_file2_dept is not None:
             os.makedirs(save_directory,exist_ok=True)

             f2= st.session_state.get('username')
             
             new_file_name=f"{f2}_E&TC.csv"
             file_path=os.path.join(save_directory,new_file_name)
             try:
              df = pd.read_csv(uploaded_file2_dept)

        # Preprocess the data
              df1 = preprocess_data(df)
              df1.to_csv(file_path, index=False)
              st.success(f"File saved ")
             except:
                  st.error(f"please choose a appropriate file or file format")

  












#*******************main***********************************************

def app():
     try:
        if 'username' not in st.session_state:
          st.session_state.username = ''
        
        st.markdown("<h1 style='font-size: 32px;'>Performance Overview: Class & Department</h1>", unsafe_allow_html=True)
        st.caption(":blue[_Insights_] into Class and Department Success :bar_chart:")

        if st.session_state.get('username'):
         f2= st.session_state.get('username')
         selected = option_menu(
           menu_title=None,
           options=["Department","IT","COMP","E&TC"],
           icons=["bookmark-fill","bar-chart-fill","bar-chart-fill","bar-chart-fill"],
           menu_icon="cast",
           default_index=0,
           orientation="horizontal",
           )

#************************************department**************************************************          
         if selected == "Department":
          username = st.session_state.get('username')

          if username is None:
              st.error('Please log in to access student data.')
              return

        # Construct file paths
         
        # Read CSV files into DataFrames
          try:
             choice21 = st.selectbox('select Department',['None','First Sem','Second Sem'])
             if choice21 == 'First Sem':
              term= 'SEM1'
             elif choice21 == 'Second Sem':
              term= 'SEM2'
             else:
              st.write("please select sem")               
             
             username = st.session_state.get('username')
             df1 = pd.read_csv(f"./uploads/{username}/{username}_IT_SE9_{term}.csv")
             df2 = pd.read_csv(f"./uploads/{username}/{username}_IT_SE10_{term}.csv")
             df3 = pd.read_csv(f"./uploads/{username}/{username}_IT_SE11_{term}.csv")
             df4 = pd.read_csv(f"./uploads/{username}/{username}_IT_TE9_{term}.csv")
             df5 = pd.read_csv(f"./uploads/{username}/{username}_IT_TE10_{term}.csv")
             df6 = pd.read_csv(f"./uploads/{username}/{username}_IT_TE11_{term}.csv")
             df7 = pd.read_csv(f"./uploads/{username}/{username}_IT_BE9_{term}.csv")
             df8 = pd.read_csv(f"./uploads/{username}/{username}_IT_BE10_{term}.csv")
             df9 = pd.read_csv(f"./uploads/{username}/{username}_IT_BE11_{term}.csv")

             df21 = pd.read_csv(f"./uploads/{username}/{username}_COMP_SE9_{term}.csv")
             df22 = pd.read_csv(f"./uploads/{username}/{username}_COMP_SE10_{term}.csv")
             df23 = pd.read_csv(f"./uploads/{username}/{username}_COMP_SE11_{term}.csv")
             df24 = pd.read_csv(f"./uploads/{username}/{username}_COMP_TE9_{term}.csv")
             df25 = pd.read_csv(f"./uploads/{username}/{username}_COMP_TE10_{term}.csv")
             df26 = pd.read_csv(f"./uploads/{username}/{username}_COMP_TE11_{term}.csv")
             df27 = pd.read_csv(f"./uploads/{username}/{username}_COMP_BE9_{term}.csv")
             df28 = pd.read_csv(f"./uploads/{username}/{username}_COMP_BE10_{term}.csv")
             df29 = pd.read_csv(f"./uploads/{username}/{username}_COMP_BE11_{term}.csv")


             df31 = pd.read_csv(f"./uploads/{username}/{username}_E&TC_SE9_{term}.csv")
             df32 = pd.read_csv(f"./uploads/{username}/{username}_E&TC_SE10_{term}.csv")
             df33 = pd.read_csv(f"./uploads/{username}/{username}_E&TC_SE11_{term}.csv")
             df34 = pd.read_csv(f"./uploads/{username}/{username}_E&TC_TE9_{term}.csv")
             df35 = pd.read_csv(f"./uploads/{username}/{username}_E&TC_TE10_{term}.csv")
             df36 = pd.read_csv(f"./uploads/{username}/{username}_E&TC_TE11_{term}.csv")
             df37 = pd.read_csv(f"./uploads/{username}/{username}_E&TC_BE9_{term}.csv")
             df38 = pd.read_csv(f"./uploads/{username}/{username}_E&TC_BE10_{term}.csv")
             df39 = pd.read_csv(f"./uploads/{username}/{username}_E&TC_BE11_{term}.csv")

# Calculate the average of the "Total" column for each pair of files
             average1_2 = (df1["Total"].mean() + df2["Total"].mean()+ df3["Total"].mean() + df4["Total"].mean() + df5["Total"].mean()+ df6["Total"].mean() + df7["Total"].mean() + df8["Total"].mean()+ df9["Total"].mean()) / 9
             average3_4 = (df21["Total"].mean() + df22["Total"].mean()+ df23["Total"].mean() + df24["Total"].mean() + df25["Total"].mean()+ df26["Total"].mean() + df27["Total"].mean() + df28["Total"].mean()+ df29["Total"].mean()) / 9
             average5_6 = (df31["Total"].mean() + df32["Total"].mean()+ df33["Total"].mean() + df34["Total"].mean() + df35["Total"].mean()+ df36["Total"].mean() + df37["Total"].mean() + df38["Total"].mean()+ df39["Total"].mean()) / 9

             averages = [average1_2, average3_4, average5_6]
             labels = ["IT", "COMP", "E&TC"]

             st.bar_chart(dict(zip(labels, averages)))

          except FileNotFoundError:
               st.error('CSV files not found. Please check file is uploaded or not if not please upload files.')
              

        



#***********************IT*************************************************************************************  
         if selected == "IT":
          choice2111 = st.selectbox('select Department',['None','First Sem','Second Sem'])
          if choice2111 == 'First Sem':
           sem= 'SEM1'
          elif choice2111 == 'Second Sem':
           sem= 'SEM2'
          else:
           st.write("please select sem")

          st.title(f"IT")
    
          selected1 = option_menu(
          menu_title=None,
          options=["class","SE","TE","BE"],
          menu_icon="cast",
          default_index=0,
          orientation="horizontal,",
          )

          if selected1 == "class":
               class_chart("IT",sem)


            

            
                  
          


#**************************************************SE********************************************

          if selected1 == "SE":
           st.title('SE Result Analysis')
        # Retrieve username from session state
           username = st.session_state.get('username')

           SE9_file_path = f"./uploads/{f2}/{username}_IT_SE9_{sem}.csv"
           SE10_file_path = f"./uploads/{f2}/{username}_IT_SE10_{sem}.csv"
           SE11_file_path = f"./uploads/{f2}/{username}_IT_SE11_{sem}.csv" 
          
           chart_div(SE9_file_path,SE10_file_path,SE11_file_path,"SE9","SE10","SE11") 
           
           choice = st.selectbox('select class',['None','DIV A','DIV B','DIV C'])
           if choice == "DIV A":
                  path232= SE9_file_path
                  attainment(path232) 
           if choice == "DIV B":
                  path232= SE10_file_path
                  attainment(path232)
           if choice == "DIV C":
                  path232= SE11_file_path
                  attainment(path232)
                        
   
         
                  


#****************************************************TE**********************************
          if selected1 == "TE":
             st.title('TE Result Analysis')


        # Retrieve username from session state
             username = st.session_state.get('username')


             TE9_file_path = f"./uploads/{f2}/{username}_IT_TE9_{sem}.csv"
             TE10_file_path = f"./uploads/{f2}/{username}_IT_TE10_{sem}.csv"
             TE11_file_path = f"./uploads/{f2}/{username}_IT_TE11_{sem}.csv"
        
             chart_div(TE9_file_path,TE10_file_path,TE11_file_path,"TE9","TE10","TE11")
       # div wise
             choice = st.selectbox('select class',['None','DIV A','DIV B','DIV C'])
             if choice == "DIV A":
                  path232= TE9_file_path
                  attainment(path232)
             if choice == "DIV B":
                  path232= TE10_file_path
                  attainment(path232)
             if choice == "DIV C":
                  path232= TE11_file_path
                  attainment(path232)
        #replace files    
     

#****************************************************BE**********************************
          if selected1 == "BE":
             st.title('BE Result Analysis')


        # Retrieve username from session state
             username = st.session_state.get('username')

             BE9_file_path = f"./uploads/{f2}/{username}_IT_BE9_{sem}.csv"
             BE10_file_path = f"./uploads/{f2}/{username}_IT_BE10_{sem}.csv"
             BE11_file_path = f"./uploads/{f2}/{username}_IT_BE11_{sem}.csv"
        
             chart_div(BE9_file_path,BE10_file_path,BE11_file_path,"BE9","BE10","BE11")
       # div wise
             choice = st.selectbox('select class',['None','DIV A','DIV B','DIV C'])
             if choice == "DIV A":
                  path232= BE9_file_path
                  attainment(path232)
             if choice == "DIV B":
                  path232= BE10_file_path
                  attainment(path232)
             if choice == "DIV C":
                  path232= BE11_file_path
                  attainment(path232)
        #replace files    
            


             
             

    
             
             
    








#************************************************************COMP**********************************************************        
         if selected == "COMP":
          choice2122 = st.selectbox('select Department',['None','First Sem','Second Sem'])
          if choice2122 == 'First Sem':
           sem= 'SEM1'
          elif choice2122 == 'Second Sem':
           sem= 'SEM2'
          else:
           st.write("please select sem")


          st.title(f"COMP")
          selected2 = option_menu(
          menu_title=None,
          options=["class","SE","TE","BE"], 
          menu_icon="cast",
          default_index=0,
          orientation="horizontal,",
          )
           
          if selected2 == "class":
             class_chart("COMP",sem)
             st.write(sem)
            
    
          

#**************************************************SE********************************************

          if selected2 == "SE":
           st.title('SE Result Analysis')
        # Retrieve username from session state
           username = st.session_state.get('username')

           SE9_file_path = f"./uploads/{f2}/{username}_COMP_SE9_{sem}.csv"
           SE10_file_path = f"./uploads/{f2}/{username}_COMP_SE10_{sem}.csv"
           SE11_file_path = f"./uploads/{f2}/{username}_COMP_SE11_{sem}.csv"
          
           chart_div(SE9_file_path,SE10_file_path,SE11_file_path,"SE9","SE10","SE11") 
           
           choice = st.selectbox('select class',['None','DIV A','DIV B','DIV C'])
           if choice == "DIV A":
                  path232= SE9_file_path
                  attainment(path232) 
           if choice == "DIV B":
                  path232= SE10_file_path
                  attainment(path232)
           if choice == "DIV C":
                  path232= SE11_file_path
                  attainment(path232)
                        
        #replace files    

                  


#****************************************************TE**********************************
          if selected2 == "TE":
             st.title('TE Result Analysis')


        # Retrieve username from session state
             username = st.session_state.get('username')

             TE9_file_path = f"./uploads/{f2}/{username}_COMP_TE9_{sem}.csv"
             TE10_file_path = f"./uploads/{f2}/{username}_COMP_TE10_{sem}.csv"
             TE11_file_path = f"./uploads/{f2}/{username}_COMP_TE11_{sem}.csv"
        
             chart_div(TE9_file_path,TE10_file_path,TE11_file_path,"TE9","TE10","TE11")
       # div wise
             choice = st.selectbox('select class',['None','DIV A','DIV B','DIV C'])
             if choice == "DIV A":
                  path232= TE9_file_path
                  attainment(path232) 
             if choice == "DIV B":
                  path232= TE10_file_path
                  attainment(path232)
             if choice == "DIV C":
                  path232= TE11_file_path
                  attainment(path232)
        #replace files    








#****************************************************BE**********************************
          if selected2 == "BE":
             st.title('BE Result Analysis')


        # Retrieve username from session state
             username = st.session_state.get('username')

             BE9_file_path = f"./uploads/{f2}/{username}_COMP_BE9_{sem}.csv"
             BE10_file_path = f"./uploads/{f2}/{username}_COMP_BE10_{sem}.csv"
             BE11_file_path = f"./uploads/{f2}/{username}_COMP_BE11_{sem}.csv"

             
        
             chart_div(BE9_file_path,BE10_file_path,BE11_file_path,"BE9","BE10","BE11")
       # div wise
             choice = st.selectbox('select class',['None','DIV A','DIV B','DIV C'])
             if choice == "DIV A":
                  path232= BE9_file_path
                  attainment(path232)
             if choice == "DIV B":
                  path232= BE9_file_path
                  attainment(path232)
             if choice == "DIV C":
                  path232= BE9_file_path
                  attainment(path232)
        #replace files    
             





#********************************************************E&TC**********************************************************

         if selected == "E&TC":
          choice2133 = st.selectbox('select Department',['None','First Sem','Second Sem'])
          if choice2133 == 'First Sem':
           sem= 'SEM1'
          elif choice2133 == 'Second Sem':
           sem= 'SEM2'
          else:
           st.write("please select sem")

           
          st.title(f"E&TC")
          selected3 = option_menu(
          menu_title=None,
          options=["class","SE","TE","BE"],
          menu_icon="cast",
          default_index=0,
          orientation="horizontal,",
          )
          if selected3 == "class":
             class_chart("E&TC",sem)
            
        #replace files
             

#**************************************************SE********************************************

          if selected3 == "SE":
           st.title('SE Result Analysis')
        # Retrieve username from session state
           username = st.session_state.get('username')

           SE9_file_path = f"./uploads/{f2}/{username}_E&TC_SE9_{sem}.csv"
           SE10_file_path = f"./uploads/{f2}/{username}_E&TC_SE10_{sem}.csv"
           SE11_file_path = f"./uploads/{f2}/{username}_E&TC_SE11_{sem}.csv"
          
           chart_div(SE9_file_path,SE10_file_path,SE11_file_path,"SE9","SE10","SE11") 
           
           choice = st.selectbox('select class',['None','DIV A','DIV B','DIV C'])
           if choice == "DIV A":
                  path232= SE9_file_path
                  attainment(path232) 
           if choice == "DIV B":
                  path232= SE10_file_path
                  attainment(path232)
           if choice == "DIV C":
                  path232= SE11_file_path
                  attainment(path232)
                        
        #replace files    
           
                  


#****************************************************TE**********************************
          if selected3 == "TE":
             st.title('TE Result Analysis')


        # Retrieve username from session state
             username = st.session_state.get('username')

             TE9_file_path = f"./uploads/{f2}/{username}_E&TC_TE9_{sem}.csv"
             TE10_file_path = f"./uploads/{f2}/{username}_E&TC_TE10_{sem}.csv"
             TE11_file_path = f"./uploads/{f2}/{username}_E&TC_TE11_{sem}.csv"
        
             chart_div(TE9_file_path,TE10_file_path,TE11_file_path,"TE9","TE10","TE11")
       # div wise
             choice = st.selectbox('select class',['None','DIV A','DIV B',' DIV C'])
             if choice == "DIV A":
                  path232= TE9_file_path
                  attainment(path232) 
             if choice == "DIV B":
                  path232= TE10_file_path
                  attainment(path232)
             if choice == "DIV C":
                  path232= TE11_file_path
                  attainment(path232)
        #replace files    
             







#****************************************************BE**********************************
          if selected3 == "BE":
             st.title('BE Result Analysis')

        # Retrieve username from session state
             username = st.session_state.get('username')

             BE9_file_path = f"./uploads/{f2}/{username}_E&TC_BE9_{sem}.csv"
             BE10_file_path = f"./uploads/{f2}/{username}_E&TC_BE10_{sem}.csv"
             BE11_file_path = f"./uploads/{f2}/{username}_E&TC_BE11_{sem}.csv"
        
             chart_div(BE9_file_path,BE10_file_path,BE11_file_path,"BE9","BE10","BE11")
       # div wise
             choice = st.selectbox('select class',['None','DIV A','DIV B',' DIV C'])
             if choice == "DIV A":
                  path232= BE9_file_path
                  attainment(path232)
             if choice == "DIV B":
                  path232= BE9_file_path
                  attainment(path232)
             if choice == "DIV C":
                  path232= BE9_file_path
                  attainment(path232)
        #replace files    
             


          




     

# Check if the button is clicked
   



         
        else:
             st.write("Please Login")
             st.caption("or")
             st.write("If you are a Student, go to Student Submission")
              

    
     except:
        if st.session_state.username=='':
            st.text('Please Login First')  


    










     
    
