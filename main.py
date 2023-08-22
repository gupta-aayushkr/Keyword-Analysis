import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Discord-Analysis.csv')

df_12M = df.iloc[:,-16:-4]
df_Keywords = df.iloc[:, 1:2]
df_Sum = df.iloc[:, -1:]
df_6M = df.iloc[:, -4:-3]
df_3M = df.iloc[:, -3:-2]
df_1M = df.iloc[:, -2:-1]

def df2arr2(df):
    arr = df.to_numpy()
    list1 = []
    for i in arr:
        list1.append(i)
    return list1

def df2arr(df):
    arr = df.to_numpy()
    list1 = []
    for i in arr:
        for j in i:
            list1.append(j)
    return list1

arr_12M, arr_Keywords, arr_Sum, arr_6M, arr_3M, arr_1M = [],[],[],[],[],[]
arr_12M = df2arr2(df_12M)
arr_6M = df2arr(df_6M)
arr_3M = df2arr(df_3M)
arr_1M = df2arr(df_1M)
arr_Sum = df2arr(df_Sum)
arr_Keywords = df2arr(df_Keywords)


data_df = pd.DataFrame(
    {
        "Keywords": arr_Keywords,
        "12M": arr_12M,
        "6M": arr_6M,
        "3M": arr_3M,
        "1M": arr_1M,
        "Sum": arr_Sum,
    }
)


st.data_editor(
    data_df,
    column_config={
        "Keywords": st.column_config.TextColumn(
            "Keywords", help="The name of the user", max_chars=100
        ),
        "12M": st.column_config.BarChartColumn(
            "12M",
            help="Sales in the last 12 months",
            y_min=0,
            y_max=100,
        ),
        "6M": st.column_config.NumberColumn(
            "6M",
            help="Sales in the last 6 months",
            format="%.2f",  # Adjust the format as needed
        ),
        "3M": st.column_config.NumberColumn(
            "3M",
            help="Sales in the last 3 months",
            format="%.2f",  # Adjust the format as needed
        ),
        "1M": st.column_config.NumberColumn(
            "1M",
            help="Sales in the last 1 month",
            format="%.2f",  # Adjust the format as needed
        ),
        "Sum": st.column_config.NumberColumn(
            "Sum", help="Total sales sum", format="%.2f"  # Adjust the format as needed
        ),
    },
    hide_index=True,
)
