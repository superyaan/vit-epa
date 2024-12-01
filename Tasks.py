import streamlit as st
from datetime import date
import warnings
warnings.filterwarnings('ignore')
import os
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

username = st.session_state.get('username', None)


            

              
                  



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
                                choice111=st.selectbox("select Trerm",['Select term','First Term','Second Term'])
                        if choice11 =="DIV B":
                            with col2: 
                                choice112=st.selectbox("select Trerm",['Select term','First Term','Second Term'])
                        if choice11 =="DIV C":
                            with col2: 
                                choice113=st.selectbox("select Trerm",['Select term','First Term','Second Term'])        
                
                
                
                if choice1=="TE":
                    with col1:
                        choice12 = st.selectbox('select Division',['None','DIV A','DIV B','DIV C']) 
                        if choice12 =="DIV A":
                            with col2: 
                                choice121=st.selectbox("select Trerm",['Select term','First Term','Second Term'])
                        if choice12 =="DIV B":
                            with col2: 
                                choice122=st.selectbox("select Trerm",['Select term','First Term','Second Term'])
                        if choice12 =="DIV C":
                            with col2: 
                                choice123=st.selectbox("select Trerm",['Select term','First Term','Second Term'])        
                                
                if choice1=="BE":
                    with col1:
                        choice13 = st.selectbox('select Division',['None','DIV A','DIV B','DIV C']) 
                        if choice13 =="DIV A":
                            with col2: 
                                choice131=st.selectbox("select Trerm",['Select term','First Term','Second Term'])
                        if choice13 =="DIV B":
                            with col2: 
                                choice132=st.selectbox("select Trerm",['Select term','First Term','Second Term'])
                        if choice13 =="DIV C":
                            with col2: 
                                choice133=st.selectbox("select Trerm",['Select term','First Term','Second Term'])

#*************************************************COMP*******************************************************************         

           if  choice == "COMP":
               with col2:
                   choice2 = st.selectbox('select class',['None','SE','TE','BE'])   
                   if choice2=="SE":
                    with col1:
                        choice21 = st.selectbox('select Division',['None','DIV A','DIV B','DIV C']) 
                        if choice21 =="DIV A":
                            with col2: 
                                choice211=st.selectbox("select Trerm",['Select term','First Term','Second Term'])
                        if choice21 =="DIV B":
                            with col2: 
                                choice212=st.selectbox("select Trerm",['Select term','First Term','Second Term'])
                        if choice21 =="DIV C":
                            with col2: 
                                choice213=st.selectbox("select Trerm",['Select term','First Term','Second Term'])        

                   if choice2=="TE":
                    with col1:
                        choice22 = st.selectbox('select Division',['None','DIV A','DIV B','DIV C']) 
                        if choice22 =="DIV A":
                            with col2: 
                                choice221=st.selectbox("select Trerm",['Select term','First Term','Second Term'])
                        if choice22 =="DIV B":
                            with col2: 
                                choice222=st.selectbox("select Trerm",['Select term','First Term','Second Term'])
                        if choice22 =="DIV C":
                            with col2: 
                                choice223=st.selectbox("select Trerm",['Select term','First Term','Second Term'])        
                   
                   
                   
                   if choice2=="BE":
                    with col1:
                        choice23 = st.selectbox('select Division',['None','DIV A','DIV B','DIV C']) 
                        if choice23 =="DIV A":
                            with col2: 
                                choice231=st.selectbox("select Trerm",['Select term','First Term','Second Term'])
                        if choice23 =="DIV B":
                            with col2: 
                                choice232=st.selectbox("select Trerm",['Select term','First Term','Second Term'])
                        if choice23 =="DIV C":
                            with col2: 
                                choice233=st.selectbox("select Trerm",['Select term','First Term','Second Term'])
         
#*************************************************E&TC*******************************************************************         
       
           if  choice == "E&TC":
               with col2:
                   choice3 = st.selectbox('select class',['None','SE','TE','BE'])   
                   if choice3=="SE":
                    with col1:
                        choice31 = st.selectbox('select Division',['None','DIV A','DIV B','DIV C']) 
                        if choice31 =="DIV A":
                            with col2: 
                                choice311=st.selectbox("select Trerm",['Select term','First Term','Second Term'])
                        if choice31 =="DIV B":
                            with col2: 
                                choice312=st.selectbox("select Trerm",['Select term','First Term','Second Term'])
                        if choice31 =="DIV C":
                            with col2: 
                                choice313=st.selectbox("select Trerm",['Select term','First Term','Second Term'])        
                   
                   
                   if choice3=="TE":
                    with col1:
                        choice32 = st.selectbox('select Division',['None','DIV A','DIV B','DIV C']) 
                        if choice32 =="DIV A":
                            with col2: 
                                choice321=st.selectbox("select Trerm",['Select term','First Term','Second Term'])
                        if choice32 =="DIV B":
                            with col2: 
                                choice322=st.selectbox("select Trerm",['Select term','First Term','Second Term'])
                        if choice32 =="DIV C":
                            with col2: 
                                choice323=st.selectbox("select Trerm",['Select term','First Term','Second Term'])        
                   
                   if choice3=="BE":
                    with col1:
                        choice33 = st.selectbox('select Division',['None','DIV A','DIV B','DIV C']) 
                        if choice33 =="DIV A":
                            with col2: 
                                choice331=st.selectbox("select Trerm",['Select term','First Term','Second Term'])
                        if choice33 =="DIV B":
                            with col2: 
                                choice332=st.selectbox("select Trerm",['Select term','First Term','Second Term'])
                        if choice33 =="DIV C":
                            with col2: 
                                choice333=st.selectbox("select Trerm",['Select term','First Term','Second Term'])














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



          if "choice112" in locals() and choice112 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_IT_SE10_SEM1.csv"
              graph_sub(path_sub)
          if "choice112" in locals() and choice112 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_IT_SE10_SEM2.csv"
              graph_sub(path_sub)



          if "choice113" in locals() and choice113 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_IT_SE11_SEM1.csv"
              graph_sub(path_sub)
          if "choice113" in locals() and choice113 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_IT_SE11_SEM2.csv"
              graph_sub(path_sub)



 #****************************TE****************************************************
          if "choice121" in locals() and choice121 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_IT_TE9_SEM1.csv"
              graph_sub(path_sub)
          if "choice121" in locals() and choice121 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_IT_TE9_SEM2.csv"
              graph_sub(path_sub)



          if "choice122" in locals() and choice122 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_IT_TE10_SEM1.csv"
              graph_sub(path_sub)
          if "choice122" in locals() and choice122 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_IT_TE10_SEM2.csv"
              graph_sub(path_sub)


          if "choice123" in locals() and choice123 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_IT_TE11_SEM1.csv"
              graph_sub(path_sub)
          if "choice123" in locals() and choice123 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_IT_TE11_SEM2.csv"
              graph_sub(path_sub)

               
 #****************************BE***********************************************************
          if "choice131" in locals() and choice131 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_IT_BE9_SEM1.csv"
              graph_sub(path_sub)
          if "choice131" in locals() and choice131 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_IT_BE9_SEM2.csv"
              graph_sub(path_sub)


          if "choice132" in locals() and choice132 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_IT_BE10_SEM1.csv"
              graph_sub(path_sub)
          if "choice132" in locals() and choice132 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_IT_BE10_SEM2.csv"
              graph_sub(path_sub)


          if "choice133" in locals() and choice133 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_IT_BE11_SEM1.csv"
              graph_sub(path_sub)
          if "choice133" in locals() and choice133 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_IT_BE11_SEM2.csv"
              graph_sub(path_sub)

                


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



          if "choice212" in locals() and choice212 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_COMP_SE10_SEM1.csv"
              graph_sub(path_sub)
          if "choice212" in locals() and choice212 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_COMP_SE10_SEM2.csv"
              graph_sub(path_sub)


          if "choice213" in locals() and choice213 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_COMP_SE11_SEM1.csv"
              graph_sub(path_sub)
          if "choice213" in locals() and choice213 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_COMP_SE11_SEM2.csv"
              graph_sub(path_sub)


 #****************************TE******************
          if "choice221" in locals() and choice221 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_COMP_TE9_SEM1.csv"
              graph_sub(path_sub)
          if "choice221" in locals() and choice221 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_COMP_TE9_SEM2.csv"
              graph_sub(path_sub)



          if "choice222" in locals() and choice222 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_COMP_TE10_SEM1.csv"
              graph_sub(path_sub)
          if "choice222" in locals() and choice222 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_COMP_TE10_SEM2.csv"
              graph_sub(path_sub)



          if "choice223" in locals() and choice223 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_COMP_TE11_SEM1.csv"
              graph_sub(path_sub)
          if "choice223" in locals() and choice223 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_COMP_TE11_SEM2.csv"
              graph_sub(path_sub)


               
 #****************************BE******************
          if "choice231" in locals() and choice231 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_COMP_BE9_SEM1.csv"
              graph_sub(path_sub)
          if "choice231" in locals() and choice231 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_COMP_BE9_SEM2.csv"
              graph_sub(path_sub)



          if "choice232" in locals() and choice232 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_COMP_BE10_SEM1.csv"
              graph_sub(path_sub)
          if "choice232" in locals() and choice232 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_COMP_BE10_SEM2.csv"
              graph_sub(path_sub)


          if "choice233" in locals() and choice233 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_COMP_BE11_SEM1.csv"
              graph_sub(path_sub)
          if "choice233" in locals() and choice233 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_COMP_BE11_SEM2.csv"
              graph_sub(path_sub)
             





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



          if "choice312" in locals() and choice312 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_E&TC_SE10_SEM1.csv"
              graph_sub(path_sub)
          if "choice312" in locals() and choice312 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_E&TC_SE10_SEM2.csv"
              graph_sub(path_sub)


          if "choice313" in locals() and choice313 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_E&TC_SE11_SEM1.csv"
              graph_sub(path_sub)
          if "choice313" in locals() and choice313 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_E&TC_SE11_SEM2.csv"
              graph_sub(path_sub)


 #****************************TE**********************************************
          if "choice321" in locals() and choice321 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_E&TC_TE9_SEM1.csv"
              graph_sub(path_sub)
          if "choice321" in locals() and choice321 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_E&TC_TE9_SEM2.csv"
              graph_sub(path_sub)

         


          if "choice322" in locals() and choice322 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_E&TC_TE10_SEM1.csv"
              graph_sub(path_sub)
          if "choice322" in locals() and choice322 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_E&TC_TE10_SEM2.csv"
              graph_sub(path_sub)
 

          if "choice323" in locals() and choice323 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_E&TC_TE11_SEM1.csv"
              graph_sub(path_sub)
          if "choice323" in locals() and choice323 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_E&TC_TE11_SEM2.csv"
              graph_sub(path_sub)

               
 #****************************BE*********************************************
          if "choice331" in locals() and choice331 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_E&TC_BE9_SEM1.csv"
              graph_sub(path_sub)
          if "choice331" in locals() and choice331 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_E&TC_BE9_SEM2.csv"
              graph_sub(path_sub)



          if "choice332" in locals() and choice332 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_E&TC_BE10_SEM1.csv"
              graph_sub(path_sub)
          if "choice332" in locals() and choice332 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_E&TC_BE10_SEM2.csv"
              graph_sub(path_sub)

          if "choice333" in locals() and choice333 == "First Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_E&TC_BE11_SEM1.csv"
              graph_sub(path_sub)
          if "choice333" in locals() and choice333 == "Second Term":
              username = st.session_state.get('username')
              path_sub=f"{username}_E&TC_BE11_SEM2.csv"
              graph_sub(path_sub)
def append_to_csv(filtered_df, assign_currdate, assign_name, assign_subject, assign_date):
    output_file_path = f"./uploads/{username}/filtered_students.csv"
    assign_currdate_str = assign_currdate.strftime("%Y-%m-%d")
    # Ensure assign_date is in a proper format, if provided, else use the current date
    assign_date_str = assign_date if assign_date else assign_currdate_str
    
    # Add assignment details as new columns to the DataFrame
    filtered_df['Assignment Date'] = assign_currdate_str
    filtered_df['Assignment Name'] = assign_name
    filtered_df['Assignment Subject'] = assign_subject
    filtered_df['Completion Date'] = assign_date_str
    filtered_df['Status'] = ""
    filtered_df['Submission Date'] = ""
    filtered_df['View'] = ""
    filtered_df['Assign Marks']=0
    filtered_df['remark']=""
    # Check if the file already exists
    if os.path.exists(output_file_path):
        # Append the new data without writing header if the file exists
        filtered_df.to_csv(output_file_path, mode='a', header=False, index=False)
        st.success("Filtered students data with assignment details has been appended to CSV!")
    else:
        # If the file doesn't exist, create a new file and write the header
        filtered_df.to_csv(output_file_path, mode='w', header=True, index=False)
        st.success("Filtered students data with assignment details has been written to a new CSV!")

@st.dialog("Cast your vote")
def vote(item, filtered_df):
     st.write(f"Assignment details")
     assign_currdate = date.today()
     
     st.write(assign_currdate)
     assign_name = st.text_input("Assignment Name")
     assign_subject = st.text_input("Subject")
     assign_date = st.date_input("Select completion date", min_value=date.today())
    
     
     st.write(f"Type your mail format")
     reason = st.text_input("Subject for mail")
     reason2 = st.text_input("body for mail (Optional)")
     assignment_file = st.file_uploader("Upload Assignment", type=["pdf", "docx"])
     if st.button("Submit"):
         if assignment_file is not None:

            append_to_csv(filtered_df, assign_currdate, assign_name, assign_subject, assign_date)
                    
            if item:
                send_email(item, assignment_file,reason, reason2 or "Please complete the attached assignment before the date.")
            else:
                st.warning("No students found in the selected marks range.")
         else:
            st.error("Please upload an assignment file!")


            
def graph_sub(path):
           uploaded_csv = f"./uploads/{username}/{path}"
           
           if uploaded_csv is not None:
          #     uploaded_csv1 = st.file_uploader("Upload Student CSV", type="csv")
              df = pd.read_csv(uploaded_csv)

              min_marks, max_marks = st.slider('Select Marks Range', min_value=int(df['Total'].min()), 
                                     max_value=int(df['Total'].max()), 
                                     value=(int(df['Total'].min()), int(df['Total'].max())))
    
              filtered_df = df[(df['Total'] >= min_marks) & (df['Total'] <= max_marks)]
              st.write("Filtered Students", filtered_df)

    # Upload assignment file
              if "vote" not in st.session_state:        
                    if st.button("continue"):
                        email_list = filtered_df['mail'].tolist()
                        vote(email_list)
                        # vote("A")



          

def upload_file():
           uploaded_csv = st.file_uploader("Upload Students CSV :envelope_with_arrow:", type="csv")
           
           st.write(username)
           if uploaded_csv is not None:
              df = pd.read_csv(uploaded_csv)

              min_marks, max_marks = st.slider('Select Marks Range', min_value=int(df['Total'].min()), 
                                     max_value=int(df['Total'].max()), 
                                     value=(int(df['Total'].min()), int(df['Total'].max())))
    
              filtered_df = df[(df['Total'] >= min_marks) & (df['Total'] <= max_marks)]
              st.write("Filtered Students", filtered_df)

    # Upload assignment file
              if "vote" not in st.session_state:        
                    if st.button("continue"):
                        email_list = filtered_df['mail'].tolist()
                        vote(email_list, filtered_df)
  
          
            

def send_email(to_addresses, assignment_file,subject,body):
    from_address = 'sarvesh98patil81@gmail.com'
    password = 'qzvn dswg pxdo kgke'
    
    try:
        msg = MIMEMultipart()
        msg['From'] = from_address
        msg['To'] = ', '.join(to_addresses)
        msg['Subject'] = subject

        body = body
       
        
        msg.attach(MIMEText(body, 'plain'))

        # Check if the file was uploaded properly
        if assignment_file is not None:
            # Open the file as binary
            attachment = assignment_file.getvalue()
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment)
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename= {assignment_file.name}')

            msg.attach(part)

            # Setup SMTP server
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(from_address, password)
            text = msg.as_string()
            server.sendmail(from_address, to_addresses, text)
            server.quit()
            st.success(f"Emails sent to {', '.join(to_addresses)}")

        else:
            st.error("Assignment file not uploaded properly.")

    except Exception as e:
        st.error(f"Error sending email: {e}")
        print(f"Error sending email: {e}")


def app():
     try:
        
     #    st.set_option('deprecation.showPyplotGlobalUse', False)
        st.title('Assign Work to Students')

        if st.session_state.get('username'):
          st.caption(":blue[_Upload_] and :blue[_Assign_] Student Work 	:pencil:")
          option = st.radio("Choose an option:", ("Select Existing File", "Upload New File"))

          selected_file = None
          if option == "Upload New File":
            upload_file()
          if option == "Select Existing File":
            file_selection_page()
        else:
             st.write("Please Login")
     except:
        if st.session_state.username=='':
            st.text('Please Login First')        


         
        
   

  
  
