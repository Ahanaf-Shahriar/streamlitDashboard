import pandas as pd 
import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go


import plotly.graph_objects as go

def marital_status(df):
    marital_status_counts = df['MaritalStatus'].value_counts()
    labels = marital_status_counts.index
    values = marital_status_counts.values

    # Define the RGBA colors
    colors = ['rgba(0, 195, 255, 0.325)', 'rgba(255, 60, 0, 0.325)', 'rgba(72, 60, 50, 0.8)']

    # Create a pie chart with the specified colors
    fig_2 = go.Figure(data=go.Pie(
        labels=labels,
        values=values,
        marker=dict(colors=colors),
        textfont=dict(color='white')  # Set label text color to white
,
        textinfo='label+percent'
    ))

    # Customize the layout
    fig_2.update_layout(
        title='Marital Status Distribution',
    )

    # Display the chart
    st.plotly_chart(fig_2)

def age_barchart(df):
    # Define the age ranges
    employee_age = df['Age']

    # Define the age ranges
    bins = [0, 20, 30, 40, 50, 60, 100]
    labels = ['0-20', '20-30', '30-40', '40-50', '50-60', '60+']

    # Bin the ages into the ranges
    age_range = pd.cut(employee_age, bins=bins, labels=labels, right=False)

    # Count the number of employees in each age range
    age_counts = age_range.value_counts().sort_index()

    # Create the bar chart using Plotly
    fig = go.Figure(data=[go.Bar(x=age_counts.index, y=age_counts.values,marker=dict(color='rgba(0, 195, 255, 0.325)'))])

    # Customize the bar chart layout
    fig.update_layout(
        title='Employee Age Distribution',
        xaxis_title='Age Range',
        yaxis_title='Number of Employees'
    )

    # Render the bar chart in Streamlit
    st.plotly_chart(fig)







def employe_age_gender_barchart(df):
    # Group the data by Age and Gender and calculate the count
    grouped_data = df.groupby(['Age', 'Gender']).size().reset_index(name='Count')

    # Create the bar chart
    fig = go.Figure(data=[go.Bar(x=grouped_data['Age'], y=grouped_data['Count'], text=grouped_data['Gender'],
                                 textposition='auto')])

    # Customize the layout
    fig.update_layout(
        title='Employee Count by Age and Gender',
        xaxis_title='Age',
        yaxis_title='Count',
        barmode='group'
    )

    # Render the chart in Streamlit
    st.plotly_chart(fig)





def employee_display(df):
 
     minimum_age = df['Age'].min() 
     maximum_age = df['Age'].max()
   


     st.markdown(
        f"""
        <div style='display: flex;'>
            <div class='block green'>
                <h3>Minimum Employee Age</h3>
                <p>{minimum_age}</p>
            </div>
            <div class='block'>
                <h3>maximum Employee Age</h3>
                <p>{maximum_age}</p>
            </div>
           
           
        </div>
        
        </div>
        """,
        unsafe_allow_html=True
    )
     marital_status(df)
     
     
