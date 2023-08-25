# CSV Data Analysis with Streamlit

This is a Streamlit app that allows you to analyze CSV data files containing Keywords information. It provides insights into Keyword trends over different time periods, allows keyword filtering, and displays the results using interactive data visualization.

## Getting Started

1. Clone this repository to your local machine.
2. Make sure you have Python and the required libraries installed. You can install them using the following command:
   ```bash
   pip install streamlit pandas numpy nltk
   ```
3. Place your CSV files containing Keywords data in the `CSV Files` folder within the repository.

## Running the App

Navigate to the repository directory in your terminal and run the following command:
```bash
streamlit run app.py
```

This will open the Streamlit app in your web browser, where you can interact with the CSV data and analyze it using the provided functionalities.

## Trending.py (Homepage)

### CSV Data Loading and Analysis

- Select a CSV file from the dropdown menu to load and analyze its data.
- Calculate and display the Keyword Trends over different time periods: 12 months, 6 months, 3 months, and 1 month.
- Perform keyword analysis on the 'Keyword' column and display the top keywords based on their frequency.

### Keyword Filtering

- Use the sidebar checkboxes to filter data based on selected keywords.
- The data will be filtered and displayed according to the selected keywords.

### Data Visualization

- Visualize the filtered data using interactive data visualizations.
- The data is presented in a data table with customizable columns, including keyword, search volume in different time periods, and total search volume.

## Search.py (Sidebar)

### Usage

- In Search.py accessable from Sidebar, you'll see a text input field where you can enter a keyword.
- Once you enter a keyword and press Enter, the app will retrieve keyword data.
- It will display metrics such as volume, CPC, and competition for the entered keyword.
- In the sidebar, you'll find a list of related search suggestions based on the entered keyword.

## Note

### Issues Solved
- Requirements.txt is important for streamlit to install nltk. Otherwise, Not Found Error will be shown.

## Authors

- Aayush Kumar Gupta