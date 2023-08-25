# pip install requests
import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np
import re

# st.header("Enter the Keyword")
selected_keyword = st.text_input("Enter Keyword")


def clean_data(raw_data):
    # Remove function name and surrounding text
    cleaned_data = re.sub(r'my_amazing_function && my_amazing_function\((.*)\)', r'\1', raw_data)

    # Convert escaped characters to their original form
    cleaned_data = cleaned_data.encode().decode('unicode_escape')

    # Extract keywords using regular expression
    keywords = re.findall(r'"(.+?)"', cleaned_data)

    # Remove unwanted elements and clean keywords
    keywords = [re.sub(r'<\\/b>', '', keyword) for keyword in keywords if not re.match(r'^[a-z]$', keyword)]

    # Remove unwanted elements and clean keywords
    keywords = [re.sub(r'<b>', '', keyword) for keyword in keywords if not re.match(r'^[a-z]$', keyword)]


    return keywords


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

    #Related Searches
    url = "https://www.google.com/complete/search"
    params = {
    "client": "hp",
    "hl": "en",
    "sugexp": "msedr",
    "gs_rn": "62",
    "gs_ri": "hp",
    "cp": "1",
    "gs_id": "9c",
    "q": selected_keyword,
    "xhr": "t",
    "callback": "hello",
    }

    response = requests.get(url, params=params)
    raw_data = response.text

    keywords = clean_data(raw_data)
    res = keywords[:-2]


    # Display values with better formatting
    st.subheader("Keyword Metrics")
    st.write(f"Volume: {Volume:,}")
    st.write(f"CPC: {CPC}")
    st.write(f"Competition: {Competition:.2f}")
    
    # Display the list in the sidebar
    st.sidebar.header("Related Searches")
    for item in res:
        st.sidebar.write(item)
    
    # st.subheader("Credits")
    st.write(f"Available credits: {credits}")
    # st.write("----")

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