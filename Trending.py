import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter
import re
# from nltk.util import ngrams
# import nltk
import os

#changes
# Same Work as Glob Glob. List CSV from directory CSV Files 
csv_folder_path = "CSV Files"
csv_files = []
for file in os.listdir(csv_folder_path):
    if file.endswith(".csv"):
        csv_files.append(file)


# Display a dropdown to select a CSV files
selected_csv = st.selectbox("Select a CSV file", csv_files)
df2 = pd.read_csv(os.path.join(csv_folder_path, selected_csv))
df = pd.read_csv(os.path.join(csv_folder_path, selected_csv))

#DF analysis
df["Sum"] = round(df2.iloc[:, -12:].sum(axis=1),2)
df["6-Months"] = round(df2.iloc[:, -6:].sum(axis=1) - df2.iloc[:, -12:-6].sum(axis=1),2)
df["3-Months"] = round(df2.iloc[:, -3:].sum(axis=1) - df2.iloc[:, -6:-3].sum(axis=1),2)
df["1-Month"] = round(df2.iloc[:, -1:].sum(axis=1) - df2.iloc[:, -2:-1].sum(axis=1),2)

# st.write(df)
keywords = df['Month']
all_keywords = ' '.join(keywords)

#r is raw string. \w+ --> w meands alphanumeric + underscores and plus means more than one
# this will return a list
words = re.findall(r'\w+', all_keywords) #returns a list

for i in range(len(words)):
    words[i] = words[i].lower()

# Counting the frequency
word_counts = Counter(words) #returns a dict
total_words = sum(word_counts.values())

# Calculate the frequency as a percentage and sort
word_freq_percentage = {}
for word, count in word_counts.items():
    word_freq_percentage[word] = (count / total_words) * 100

# Sorted - sorted(iterable, key=None, reverse=False)
# key is for how to sort, lamba recieve the (key,value) and returns item[1] - value pair for sorting
sorted_word_freq_percentage = {}
sorted_items = sorted(word_freq_percentage.items(), key=lambda item: item[1], reverse=True)
for key, value in sorted_items:
    sorted_word_freq_percentage[key] = value



# Top 10 occured Keywords
top_keywords = list(sorted_word_freq_percentage.keys())[:20]

st.header("Keyword Filter")
selected_keyword2 = st.text_input("Enter Keyword")


# Create checkboxes for each keyword and their frequency
st.sidebar.header("Keyword Filter Checkbox")
checkboxes = {}
for keyword in top_keywords:
    selected = st.sidebar.checkbox(f"{keyword} ({sorted_word_freq_percentage[keyword]:.2f}%)", value=False)
    checkboxes[keyword] = selected

# st.write("checking chechboxes", checkboxes)
# print("selected exits:", selected)
# Filter the data based on the selected keyword
selected_keyword = []
for keyword, selected in checkboxes.items():
    if selected: #checboxes dictionary contains all top keywords with true or false in front of them
        selected_keyword.append(keyword)


#Filter from checkbox
# Display the selected keyword and filtered data
st.write(f"Displaying data for keyword: {', '.join(selected_keyword)}")
if "All" in selected_keyword:
    filtered_data = df
else:
    #all returns true if all the conditions inside it are True.
    # text is each element in Month Column
    filtered_data = df[df['Month'].apply(lambda text: all(keyword.lower() in text.lower() for keyword in selected_keyword))]

# Apply keyword filter to the DataFrame
df = filtered_data

#Filter from Search Bar

df = df[df["Month"].str.contains(selected_keyword2, case=False, na=False)]


df_12M = df.iloc[:,-16:-4]
df_Keywords = df.iloc[:, 1:2]
df_1M = df.iloc[:, -1:]
df_Sum = df.iloc[:, -4:-3]
df_6M = df.iloc[:, -3:-2]
df_3M = df.iloc[:, -2:-1]

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

#Handling No data Error
try:
    st.data_editor(
        data_df,
        column_config={
            "Keywords": st.column_config.TextColumn(
                "Keywords", help="Related Keywords", max_chars=100
            ),
            "12M": st.column_config.BarChartColumn(
                "12M",
                help="Trending in the last 12 months",
                y_min=0,
                y_max=100,
            ),
            "6M": st.column_config.NumberColumn(
                "6M",
                help="Trending in the last 6 months",
                format="%.2f",
            ),
            "3M": st.column_config.NumberColumn(
                "3M",
                help="Trending in the last 3 months",
                format="%.2f",
            ),
            "1M": st.column_config.NumberColumn(
                "1M",
                help="Trending in the last 1 month",
                format="%.2f",
            ),
            "Sum": st.column_config.NumberColumn(
                "Sum", help="Most Searched Trend", format="%.2f"
            ),
        },
        hide_index=True,
        width=1000, height=1000,
    )
except:
    st.warning("No data available.")