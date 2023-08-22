import streamlit as st
import pandas as pd
import numpy as np

from collections import Counter
import re
from nltk.util import ngrams
import nltk

df = pd.read_csv('Discord-Analysis.csv')
keywords = df['Month']

all_keywords = ' '.join(keywords)
words = re.findall(r'\w+', all_keywords)
words = [word.lower() for word in words]

# Count the frequency of each word
word_counts = Counter(words)
total_words = sum(word_counts.values())

# Calculate the frequency as a percentage and sort
word_freq_percentage = {word: (count / total_words) * 100 for word, count in word_counts.items()}
sorted_word_freq_percentage = dict(sorted(word_freq_percentage.items(), key=lambda item: item[1], reverse=True))

# Create a sidebar section for filtering
# st.sidebar.header("Keyword Filter")
# selected_keyword = st.sidebar.text_input("Enter Keyword")

# Get the top 10 one-word frequencies and their corresponding words
top_keywords = list(sorted_word_freq_percentage.keys())[:20]

# Create a Streamlit sidebar section for filtering
# st.sidebar.header("Keyword Filter 2")
# selected_keyword = st.sidebar.selectbox("Select Keyword", ["All"] + top_keywords)

# Create checkboxes for each keyword and their frequency
st.sidebar.header("Keyword Filter Checkbox")
checkboxes = {}
for keyword in top_keywords:
    selected = st.sidebar.checkbox(f"{keyword} ({sorted_word_freq_percentage[keyword]:.2f}%)", value=False)
    checkboxes[keyword] = selected

# Filter the data based on the selected keyword
selected_keyword = [keyword for keyword, selected in checkboxes.items() if selected]

# Display the selected keyword and filtered data
st.write(f"Displaying data for keyword: {', '.join(selected_keyword)}")
if "All" in selected_keyword:
    filtered_data = df
else:
    filtered_data = df[df['Month'].apply(lambda text: all(keyword.lower() in text.lower() for keyword in selected_keyword))]


# Apply keyword filter to the DataFrame
df = filtered_data


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
    width=1000, height=1000,
)
