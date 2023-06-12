import streamlit as st
import pandas as pd 
from demographics import employee_display ,age_barchart ,employe_age_gender_barchart
import plotly.graph_objects as go
#import matplotlib.pyplot as plt
#import squarify


def nav():
    # Create a sidebar
    st.sidebar.title("Navigation")
    
    # Add navigation links
    page = st.sidebar.radio("Go to", ("overview", "Demographics", "Performance Tracker","attrition"))
    
    # Render different pages based on the selected navigation link
    if page == "overview":
        st.header("OverView")
        # Add content for the home page
    elif page == "Demographics":
        st.header("Demographics")
        # Add content for the about page
    elif page == "Performance Tracker":
        st.header("Performance Tracker")
    elif page == "attrition":
        st.header("attrition")
        # Add content for the contact page


def employee_Data(df):
    numberOfEmployees = df.shape[0]
    attrition_column = df.loc[:, 'Attrition']
    activeEmployees = attrition_column.eq('No').sum()  
    inactiveEmployees = numberOfEmployees - activeEmployees 
    activeEmployees = numberOfEmployees - inactiveEmployees 
    
    attritionRate = (inactiveEmployees / numberOfEmployees) * 100
    formatted_attritionRate = f"{attritionRate:.1f}%"

    # Display the blocks side by side
    st.markdown(
        f"""
        <div style='display: flex;'>
            <div class='block green'>
                <h3>Employee Number</h3>
                <p>{numberOfEmployees}</p>
            </div>
            <div class='block'>
                <h3>Active Employees</h3>
                <p>{activeEmployees}</p>
            </div>
            <div class='block green'>
                <h3>Inactive Employees</h3>
                <p>{inactiveEmployees}</p>
            </div>
            <div class='block'>
                <h3>Attrition</h3>
                <p>{formatted_attritionRate}</p>
            </div>
        </div>
        
        <div style='display: flex;'>
            <div style='flex: 1;'>
                <!-- Add the bar chart here -->
                <h3>Employee Count by Year</h3>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Convert 'HireDate' column to datetime
    df['HireDate'] = pd.to_datetime(df['HireDate'])

    # Extract the year from 'HireDate' column
    df['Year'] = df['HireDate'].dt.year


    # Count the occurrences of 'Yes' and 'No' per year
    attrition_counts = df.groupby(['Year', 'Attrition']).size().unstack().fillna(0)
    department_counts = df['Department'].value_counts()

    # Create a bar chart using Plotly
    fig = go.Figure(data=[
        go.Bar(name='No', x=attrition_counts.index, y=attrition_counts['No'], marker=dict(color='rgba(0, 195, 255, 0.325)')),
        go.Bar(name='Yes', x=attrition_counts.index, y=attrition_counts['Yes'], marker=dict(color='white'))
    ])

    # Customize the chart layout
    fig.update_layout(
        title='Employee Hiring Trend',
        xaxis=dict(title='Year'),
        yaxis=dict(title='Employee Count'),
        barmode='stack',  # Stack the bars for each year
    )
    fig.update_layout(legend_title_text='Attrition')  # Add legend title

    # Display the chart using Streamlit
    st.plotly_chart(fig)

    fig2 = go.Figure(data=[go.Bar(x=department_counts.index, y=department_counts.values,marker=dict(color='rgba(0, 195, 255, 0.325)'))])

# Customize the chart layout
    fig2.update_layout(
    title='Number of Employees by Department',
    xaxis=dict(title='Department'),
    yaxis=dict(title='Number of Employees')
    )

# Show the chart
    st.plotly_chart(fig2)

    



def main(df):
       css = open('style.css', 'r').read()

    # Link the CSS file
       st.markdown(f'<head><style>{css}</style></head>', unsafe_allow_html=True)

    # Navigation
       nav()
   
    # Title and content
       st.markdown("<div class='main'><h1 class='title'>My Dashboard</h1></div>", unsafe_allow_html=True)

    
if __name__ == '__main__':
    df = pd.read_csv('/Users/ahanafshahriar/PycharmProjects/streamlitDash/HRM_Dashboard/Employee.csv')

    main(df)
    employee_Data(df)
    st.title("Demographics")
    employee_display(df)
    age_barchart(df)
    employe_age_gender_barchart(df)
    


