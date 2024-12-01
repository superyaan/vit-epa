import streamlit as st
from datetime import date
import warnings
warnings.filterwarnings('ignore')
import os
import pandas as pd


username = st.session_state.get('username', None)
def student_assignment_upload():
    st.title("Student Assignment Submission")
    
    # Input student details
    roll_no = st.text_input("Enter Your Roll Number")
    filtered_file_path = f"./uploads/{username}/filtered_students.csv"
    
    # Ensure the filtered_students.csv exists
    if os.path.exists(filtered_file_path):
        # Read filtered_students.csv
        filtered_df = pd.read_csv(filtered_file_path)
        
        # Validate roll number
        if roll_no.isdigit() and int(roll_no) in filtered_df['RollNo'].values:
            student_data = filtered_df[filtered_df['RollNo'] == int(roll_no)]
            
            # Filter records where the "Completion Date" is not overdue
            today = date.today()
            student_data['Completion Date'] = pd.to_datetime(student_data['Completion Date'], errors='coerce')
            valid_data = student_data[student_data['Completion Date'] >= pd.Timestamp(today)]
            
            if valid_data.empty:
                st.error("Submission deadline has passed for all assignments.")
            else:
                subjects = valid_data['Assignment Subject'].unique()
                
                # Allow the student to select a subject
                subject = st.selectbox("Select the Subject for Assignment Submission", subjects)
                
                # Input for remark
                remark = st.text_input("Add a Remark (Optional)")
                
                # Upload assignment file
                assignment_file = st.file_uploader("Upload Assignment", type=["pdf", "docx"])
                
                # On submit, update filtered_students.csv
                if st.button("Submit Assignment"):
                    if assignment_file is not None:
                        # Generate a unique path to store the uploaded file
                        assignment_dir = f"./uploads/{username}/submitted_assignments"
                        os.makedirs(assignment_dir, exist_ok=True)
                        assignment_path = f"{assignment_dir}/{roll_no}_{subject}_{assignment_file.name}"
                        
                        # Save the uploaded file
                        with open(assignment_path, "wb") as f:
                            f.write(assignment_file.getbuffer())
                        
                        # Update the filtered_students.csv file
                        submission_date = date.today().strftime("%Y-%m-%d")
                        filtered_df.loc[(filtered_df['RollNo'] == int(roll_no)) & 
                                        (filtered_df['Assignment Subject'] == subject), 'Status'] = "Submitted"
                        filtered_df.loc[(filtered_df['RollNo'] == int(roll_no)) & 
                                        (filtered_df['Assignment Subject'] == subject), 'Submission Date'] = submission_date
                        filtered_df.loc[(filtered_df['RollNo'] == int(roll_no)) & 
                                        (filtered_df['Assignment Subject'] == subject), 'View'] = assignment_path
                        filtered_df.loc[(filtered_df['RollNo'] == int(roll_no)) & 
                                        (filtered_df['Assignment Subject'] == subject), 'remark'] = remark
                                        
                        
                        # Save changes back to CSV
                        filtered_df.to_csv(filtered_file_path, index=False)
                        st.success("Assignment Submitted Successfully!")
                    else:
                        st.error("Please upload an assignment file!")
        else:
            st.error("Roll Number not found in the records!")
    else:
        st.error("Filtered students file not found! Please contact the administrator.")
def app():
        student_assignment_upload()

          


         
        
   

  
  
