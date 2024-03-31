import plotly.express as px
import pandas as pd
from . import db
from .models import Dashboard, Complaint, Case
from sqlalchemy import func

def dashboard_chart():
    # Create a DataFrame from the provided data snippet
    df = pd.read_csv('/Users/tommy/github-classroom/comp0034-cw2i-TommyLau-bit/src/data/dataset_prepared.csv')  # Update the path to your CSV file

    # Aggregate the 'Closed on Time?' data
    on_time_data = df[df['Closed on Time?'] == 'on time'].groupby(['Request Received (Year)', 'Request Received (Month)']).size().reset_index(name='On Time Count')
    late_data = df[df['Closed on Time?'] == 'late'].groupby(['Request Received (Year)', 'Request Received (Month)']).size().reset_index(name='Late Count')

    # Combine the data into a single DataFrame
    combined_data = pd.merge(on_time_data, late_data, on=['Request Received (Year)', 'Request Received (Month)'], how='outer').fillna(0)

    # Create a bar chart with both on-time and late counts
    fig = px.bar(combined_data, x='Request Received (Year)', y=['On Time Count', 'Late Count'], barmode='group', title='Case Closure Timeliness Overview')

    # Customize the figure
    fig.update_layout(xaxis_title="Year", yaxis_title="Number of Cases", 
                      legend_title_text='Case Status', 
                      legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
    fig.update_traces(texttemplate='%{value}', textposition='outside')
    fig.update_yaxes(type='linear')  # Change to 'log' if large disparities in counts

    return {"fig": fig.to_html(full_html=False, include_plotlyjs=True)}

def complaint_chart():
    # Query the database for counts of each reason
    complaints = db.session.query(Complaint.reason_grouped, func.count(Complaint.id)).group_by(Complaint.reason_grouped).all()
    
    # Convert query results to a DataFrame
    df = pd.DataFrame(complaints, columns=['Reason', 'Count'])
    
    # Calculate percentage of each reason
    total_complaints = df['Count'].sum()
    df['Percentage'] = (df['Count'] / total_complaints) * 100

    # Sort DataFrame by count in descending order
    df = df.sort_values(by='Count', ascending=False)

    # Create the horizontal bar chart
    fig = px.bar(df, y='Reason', x='Count', orientation='h', 
                 text='Percentage', title='Complaints by Reason',
                 labels={'Count': 'Number of Complaints', 'Reason': 'Complaint Reason'},
                 hover_data={'Percentage': True},
                 color='Count', color_continuous_scale='blues')

    # Customize layout
    fig.update_traces(marker_line_width=1.5, opacity=0.8, textposition='outside')
    fig.update_layout(xaxis_title="Number of Complaints", yaxis_title=None,
                      coloraxis_showscale=False, showlegend=False)

    return {"fig": fig.to_html(full_html=False, include_plotlyjs=True)}

def dashboard_active_cases_chart():
    # Query the database for active cases grouped by category
    dashboards = db.session.query(Dashboard.case_active_grouped).all()
    
    # Convert query results to a DataFrame
    df = pd.DataFrame(dashboards, columns=['Active Case Group'])
    
    # Count the occurrences of each category
    df_count = df['Active Case Group'].value_counts().reset_index()
    df_count.columns = ['Active Case Group', 'Count']

    # Create the bar chart
    fig = px.bar(df_count, x='Active Case Group', y='Count', 
                 title='Dashboard Active Cases Overview', 
                 labels={'Active Case Group': 'Active Case Group', 'Count': 'Number of Cases'},
                 color='Active Case Group', color_continuous_scale='blues')

    # Customize layout
    fig.update_traces(marker_line_width=1.5, opacity=0.8)
    fig.update_layout(xaxis_title="Active Case Group", yaxis_title="Number of Cases",
                      coloraxis_showscale=False, showlegend=False)

    return {"fig": fig.to_html(full_html=False, include_plotlyjs=True)}

def get_complaint_reasons_distribution():
    # Query the database for counts of each reason
    results = db.session.query(Complaint.reason_grouped, db.func.count(Complaint.id)).group_by(Complaint.reason_grouped).all()
    
    # Convert query results to a DataFrame
    df = pd.DataFrame(results, columns=['Reason', 'Count'])
    
    # Sort the DataFrame by count in descending order
    df = df.sort_values(by='Count', ascending=False)
    
    # Create the chart
    fig = px.bar(df, x='Reason', y='Count', title='Distribution of Complaints by Reason', color='Reason',
                 labels={'Reason': 'Complaint Reason', 'Count': 'Number of Complaints'},
                 color_discrete_sequence=px.colors.qualitative.Bold)
    
    # Customize layout
    fig.update_layout(xaxis_title="Complaint Reason", yaxis_title="Number of Complaints",
                      legend_title="Complaint Reason", barmode='group',
                      margin=dict(l=0, r=0, t=50, b=0))
    
    return {"fig": fig.to_html(full_html=False, include_plotlyjs=True)}

def case_closure_time_distribution():
    # Query case data from the database
    case_data = db.session.query(Case.case_active_grouped).all()
    
    # Convert the query result to a DataFrame
    df = pd.DataFrame(case_data, columns=['Case Active Days Group'])
    
    # Assuming 'case_active_grouped' contains categorical data, we'll visualize the counts
    df_count = df['Case Active Days Group'].value_counts().reset_index()
    df_count.columns = ['Case Active Days Group', 'Count']
    
    # Create the histogram
    fig = px.histogram(df_count, x='Case Active Days Group', y='Count', 
                       title='Distribution of Case Closure Times',
                       labels={'Case Active Days Group': 'Case Closure Time (Grouped)', 'Count': 'Frequency'})
    
    # Customize layout
    fig.update_layout(xaxis_title="Case Closure Time (Grouped)", yaxis_title="Frequency",
                      margin=dict(l=0, r=0, t=50, b=0))
    
    return {"fig": fig.to_html(full_html=False, include_plotlyjs=True)}