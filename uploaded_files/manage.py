
import streamlit as st
import pandas as pd
import os
import plotly.express as px
import plotly.graph_objects as go

# Specify the folder path where CSV files are stored
folder_path = './uploads/Sarvesh Patil'  # Replace with your actual folder path

# Function to load CSV files
def load_csv_files(folder):
    csv_files = [f for f in os.listdir(folder) if f.endswith('.csv')]
    return csv_files

# Display list of CSV files
csv_files = load_csv_files(folder_path)
selected_file = st.selectbox("Select a CSV file", csv_files)

# Load the selected CSV file
if selected_file:
    file_path = os.path.join(folder_path, selected_file)
    df = pd.read_csv(file_path)

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
