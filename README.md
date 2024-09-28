# Health Visualization Tool

This is a Flask-based web application that allows users to input health data (heart rate, steps, and sleep hours) and visualize the results using various charts. The data is stored in memory using a Pandas DataFrame, and visualizations are created using Matplotlib and Seaborn.

## Features
- Submit health data (date, heart rate, steps, sleep hours) through a web form.
- Generate visualizations of heart rate over time and steps per day.
- Visualizations are saved as images and displayed on the web page.

## Prerequisites
To run this project, you need the following installed on your machine:
- Python 3.x
- Flask
- Pandas
- Matplotlib
- Seaborn

You can install the required Python libraries by running:
```bash
pip install flask pandas matplotlib seaborn
