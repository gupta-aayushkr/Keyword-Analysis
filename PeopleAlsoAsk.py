# pip install requests
import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np

st.header("Enter the Keyword")
selected_keyword = st.text_input("Enter Keyword")

if selected_keyword:
    my_data = {
        'country': 'us',
        'currency': 'USD',
        'dataSource': 'gkp',
        'kw[]': selected_keyword
    }
    my_headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer bede33d91baed7fd50d0'
    }

    response = requests.post(
        'https://api.keywordseverywhere.com/v1/get_keyword_data', data=my_data, headers=my_headers)

    keywords_data = response.json()['data']
    trend_dict = keywords_data[0]["trend"]
    keywords_dict = keywords_data[0]

    trend_list = []
    for i in trend_dict:
        trend_list.append(i["value"])
    

    date_list = []
    for i in trend_dict:
        date_list.append(i["month"]+  " " + str(i["year"]))

    keyword = keywords_data[0]["keyword"]
    df = pd.DataFrame(columns=["vol", "cpc", "competition", "trend"])

    Volume = keywords_dict["vol"]
    CPC = keywords_dict["cpc"]["currency"] + keywords_dict["cpc"]["value"]
    Competition = keywords_dict["competition"]
    credits = response.json()["credits"]

    # Display values with better formatting
    st.subheader("Keyword Metrics")
    st.write(f"Volume: {Volume:,}")
    st.write(f"CPC: {CPC}")
    st.write(f"Competition: {Competition:.2f}")

    st.subheader("Credits")
    st.write(f"Available credits: {credits}")
    st.write("----")

    x_data = date_list
    y_data = trend_list


    # Create a bar plot for categorical data using Plotly
    fig = go.Figure(data=go.Bar(x=date_list, y=trend_list, marker_color='#ff4b4b'))

    # Calculate the trend line using numpy's polyfit
    x_values = np.arange(len(date_list))
    trend_line = np.polyfit(x_values, trend_list, 1)
    trend_line_values = np.polyval(trend_line, x_values)

    # Add trend line trace to the figure
    fig.add_trace(go.Scatter(x=date_list, y=trend_line_values, mode='lines', name='Trend Line'))

    # Customize the layout
    fig.update_layout(
        title="Keyword Data Bar Plot with Trend Line",
        xaxis_title="12-Months",
        yaxis_title="Values",
    )

    # Display the graph in the Streamlit app
    st.plotly_chart(fig)