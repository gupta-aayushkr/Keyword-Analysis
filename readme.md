# CSV Data Analysis with Streamlit

This is a Streamlit app that allows you to analyze CSV data files containing sales information. It provides insights into sales trends over different time periods, allows keyword filtering, and displays the results using interactive data visualization.

## Getting Started

1. Clone this repository to your local machine.
2. Make sure you have Python and the required libraries installed. You can install them using the following command:
   ```bash
   pip install streamlit pandas numpy nltk
   ```
3. Place your CSV files containing sales data in the `CSV Files` folder within the repository.

## Running the App

Navigate to the repository directory in your terminal and run the following command:
```bash
streamlit run app.py
```

This will open the Streamlit app in your web browser, where you can interact with the CSV data and analyze it using the provided functionalities.

## Features

### CSV Data Loading and Analysis

- Select a CSV file from the dropdown menu to load and analyze its data.
- Calculate and display the sum of sales over different time periods: 12 months, 6 months, 3 months, and 1 month.
- Perform keyword analysis on the 'Month' column and display the top keywords based on their frequency.

### Keyword Filtering

- Use the sidebar checkboxes to filter data based on selected keywords.
- The data will be filtered and displayed according to the selected keywords.

### Data Visualization

- Visualize the filtered data using interactive data visualizations.
- The data is presented in a data table with customizable columns, including keyword, sales in different time periods, and total sales sum.

## Authors

- [Your Name]

## License

This project is licensed under the [MIT License](LICENSE).
```

Replace `[Your Name]` in the "Authors" section with your actual name.

Don't forget to create a `LICENSE` file in the repository directory if you want to use the MIT License, and make sure to customize the README file further based on your preferences and additional information you'd like to include.