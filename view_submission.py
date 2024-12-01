import streamlit as st
import pandas as pd
import os
import webbrowser
import streamlit as st
import webbrowser
import warnings
warnings.filterwarnings('ignore')
import os
import pandas as pd


username = st.session_state.get('username', None)




def check_submissions():
    st.title("Check Assignment Submissions")
    filtered_file_path = f"./uploads/{username}/filtered_students.csv"
    
    # Ensure the filtered_students.csv exists
    if os.path.exists(filtered_file_path):
        # Read filtered_students.csv
        filtered_df = pd.read_csv(filtered_file_path)
        
        # Allow the teacher to select a subject
        subjects = filtered_df['Assignment Subject'].unique()
        selected_subject = st.selectbox("Select a Subject", subjects)
        
        # Filter data for the selected subject
        subject_data = filtered_df[filtered_df['Assignment Subject'] == selected_subject]
        
        if not subject_data.empty:
            st.write(f"Submissions for Subject: {selected_subject}")
            
            # Table Headers
            headers = ['RollNo', 'Assignment Name', 'Assignment Date', 
                       'Completion Date', 'Status', 'Submission Date', 'View', 'Assign Marks']
            col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
            col1.write(f"**{headers[0]}**")
            col2.write(f"**{headers[1]}**")
            col3.write(f"**{headers[2]}**")
            col4.write(f"**{headers[3]}**")
            col5.write(f"**{headers[4]}**")
            col6.write(f"**{headers[5]}**")
            col7.write(f"**{headers[6]}**")
            col8.write(f"**{headers[7]}**")
            
            # Add rows dynamically
            for idx, row in subject_data.iterrows():
                col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
                
                # Make RollNo column larger
                col1.markdown(f"<h5 style='color: green;'>{str(row['RollNo'])}</h5>", unsafe_allow_html=True)
                
                # Handle empty entries, assign 'null' where applicable
                col2.write(row['Assignment Name'] if pd.notna(row['Assignment Name']) else "null")
                col3.write(row['Assignment Date'] if pd.notna(row['Assignment Date']) else "null")
                col4.write(row['Completion Date'] if pd.notna(row['Completion Date']) else "null")
                
                # Handle Status coloring
                status = row['Status'] if pd.notna(row['Status']) else "null"
                if status.lower() == 'submitted':
                    col5.markdown(f"<span style='color: green;'>{status}</span>", unsafe_allow_html=True)
                else:
                    col5.markdown(f"<span style='color: #FF474C;'>{status}</span>", unsafe_allow_html=True)
                
                col6.write(row['Submission Date'] if pd.notna(row['Submission Date']) else "null")
                
                # Handle "View" column for file
                if pd.notna(row['View']):
                    if col7.button("📂", key=f"view_{idx}"):
                        # Open the file in the default viewer
                        file_path = row['View']
                        if os.path.exists(file_path):
                            webbrowser.open(f"file://{os.path.abspath(file_path)}")
                        else:
                            st.error("File not found!")
                else:
                    col7.write("❌")
                
                # Allow teacher to assign marks in the new "Assign Marks" column
                marks = col8.text_input(f"Marks for {row['RollNo']}", value=str(row['Assign Marks']) if pd.notna(row['Assign Marks']) else "")
                
                # Save the marks when updated
                if marks:
                    filtered_df.at[idx, 'Assign Marks'] = marks
            
            # Update the CSV with the new "Assign Marks" values after editing
            if st.button("Save Marks"):
                filtered_df.to_csv(filtered_file_path, index=False)
                st.success("Marks have been saved successfully!")

            # Filtered data for download - only the selected subject and necessary columns
            download_data = subject_data[['RollNo', 'Assignment Name', 'Assignment Date', 
                                          'Completion Date', 'Status', 'Submission Date', 'Assign Marks']]
            
            # Download updated data (filtered subject data only)
            st.download_button(
                label="Download Subject Data as CSV",
                data=download_data.to_csv(index=False),
                file_name=f"{selected_subject}_assignments.csv",
                mime="text/csv"
            )
            
        else:
            st.info("No records found for the selected subject.")
    else:
        st.error("Filtered students file not found! Please contact the administrator.")    


def app():
     try:
        
     #    st.set_option('deprecation.showPyplotGlobalUse', False)


        if st.session_state.get('username'):
          check_submissions()
        else:
             st.write("Please Login")
     except:
        if st.session_state.username=='':
            st.text('Please Login First')    

         
        
   

  
  
