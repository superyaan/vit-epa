

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


username = st.session_state.get('username')            



def graph_sub(path):
    selected_file = f"./uploads/{username}/{path}"

   
    df = pd.read_csv(selected_file)

    # Strip column names of any extra spaces
    df.columns = df.columns.str.strip()
    
    # Display the range of roll numbers in the file
    roll_min = df['RollNo'].min()
    roll_max = df['RollNo'].max()
    st.write(f"Roll numbers range from {roll_min} to {roll_max}")

    # Input to enter the roll number for which to generate graphs
    roll_number = st.number_input("Enter a roll number", min_value=roll_min, max_value=roll_max, step=1)
    
    # Filter the dataframe for the selected roll number
    if roll_number in df['RollNo'].values:  
        student_data = df[df['RollNo'] == roll_number]  

        # Exclude 'Total' from subjects for graphs and metrics
        numeric_subjects = student_data.select_dtypes(include=['number']).columns.drop(['RollNo', 'Total'], errors='ignore')

        # Separate theory and practical subjects
        theory_subjects = [col for col in numeric_subjects if 'TH' in col]
        practical_subjects = [col for col in numeric_subjects if 'PR' in col]

        # Calculate class averages for each subject
        class_averages = df[numeric_subjects].mean()

        # Metrics display
        st.title("Student Performance Dashboard")
        total_marks = student_data[numeric_subjects].sum(axis=1).values[0]
        avg_marks = student_data[numeric_subjects].mean(axis=1).values[0]
        class_avg_marks = class_averages.mean()
        highest_subject = student_data[numeric_subjects].idxmax(axis=1).values[0]
        highest_subject_marks = student_data[highest_subject].values[0]
        lowest_subject = student_data[numeric_subjects].idxmin(axis=1).values[0]

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("🌟 Total Marks", f"{total_marks}")
        col2.metric("📊 Average Marks", f"{avg_marks:.2f}")
        col3.metric("🏆 Top Subject", f"{highest_subject}: {highest_subject_marks}")
        col4.metric("⚠️ Lowest Subject", lowest_subject)

        # Compare student's average with the class average
        st.subheader("Class Average Comparison")
        st.write(f"Class Average Marks: {class_avg_marks:.2f}")
        st.write(f"Difference (Student vs. Class): {avg_marks - class_avg_marks:.2f}")

        # Identify top and bottom performers based on total marks
        df['TotalMarks'] = df[numeric_subjects].sum(axis=1)
        top_performer = df.loc[df['TotalMarks'].idxmax()]
        # bottom_performer = df.loc[df['TotalMarks'].idxmin()]

        st.subheader("Top and Bottom Performers")
        col1, col2 = st.columns(2)
        col1.metric("🏅 Top Performer", f"RollNo: {top_performer['RollNo']}", f"Total Marks: {top_performer['TotalMarks']}")
        # col2.metric("🔻 Bottom Performer", f"RollNo: {bottom_performer['RollNo']}", f"Total Marks: {bottom_performer['TotalMarks']}")

        # Visualization section
        st.subheader("Performance Overview")

        # Compare Student's Marks with Class Averages
        comparison_data = pd.DataFrame({
            'Subjects': numeric_subjects,
            'Student Marks': student_data[numeric_subjects].values.flatten(),
            'Class Average': class_averages.values
        })

        comparison_fig = px.bar(comparison_data, x='Subjects', y=['Student Marks', 'Class Average'],
                                barmode='group', title="Student vs Class Average Marks",
                                labels={'value': 'Marks', 'variable': 'Comparison'})
        st.plotly_chart(comparison_fig, use_container_width=True)

        # Theory Marks Bar Chart
        if theory_subjects:
            st.subheader("Theory Marks 🎯")
            theory_data = student_data.melt(id_vars='RollNo', value_vars=theory_subjects)
            theory_bar_fig = px.bar(theory_data, x='variable', y='value', 
                                    title='Theory Marks per Subject',
                                    labels={'value': 'Marks', 'variable': 'Subjects'},
                                    color='value', color_continuous_scale=px.colors.sequential.Plasma)
            st.plotly_chart(theory_bar_fig, use_container_width=True)

            theory_pie_fig = px.pie(theory_data, values='value', names='variable', 
                                    title='Theory Marks Distribution',
                                    color_discrete_sequence=px.colors.sequential.RdBu)
            st.plotly_chart(theory_pie_fig, use_container_width=True)

        # Practical Marks Bar Chart
        if practical_subjects:
            st.subheader("Practical Marks 🔧")
            practical_data = student_data.melt(id_vars='RollNo', value_vars=practical_subjects)
            practical_bar_fig = px.bar(practical_data, x='variable', y='value', 
                                       title='Practical Marks per Subject',
                                       labels={'value': 'Marks', 'variable': 'Subjects'},
                                       color='value', color_continuous_scale=px.colors.sequential.Viridis)
            st.plotly_chart(practical_bar_fig, use_container_width=True)

            practical_pie_fig = px.pie(practical_data, values='value', names='variable', 
                                       title='Practical Marks Distribution',
                                       color_discrete_sequence=px.colors.sequential.Blues)
            st.plotly_chart(practical_pie_fig, use_container_width=True)

        # Line Graph with a Trendline and Prediction Marker
        st.subheader("Performance Trend 📈")
        marks = student_data[numeric_subjects].values.flatten().tolist()
        avg_marks_trend = [avg_marks] * len(numeric_subjects)  # Repeat avg_marks for trendline

        line_fig = go.Figure()
        line_fig.add_trace(go.Scatter(x=numeric_subjects, y=marks, 
                                      mode='lines+markers', 
                                      line=dict(color='firebrick', width=4),
                                      name='Marks'))
        line_fig.add_trace(go.Scatter(x=numeric_subjects, 
                                      y=avg_marks_trend,  
                                      mode='lines', line=dict(dash='dash', color='blue'),
                                      name='Projected Trend'))
        line_fig.update_layout(title="Performance Trend with Prediction", 
                               xaxis_title="Subjects", yaxis_title="Marks",
                               showlegend=True)
        st.plotly_chart(line_fig, use_container_width=True)

    else:
        st.error("Roll number not found in the selected file.")


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




def app():
     try:
        
     #    st.set_option('deprecation.showPyplotGlobalUse', False)
        st.title('Detailed Student Report')

        if st.session_state.get('username'):
          st.caption("📊 Explore key performance :blue[_metrics_] and :blue[_metrics_] for each student. 📈")
          file_selection_page()
             



        else:
             st.write("Please Login")
     except:
        if st.session_state.username=='':
            st.text('Please Login First')        