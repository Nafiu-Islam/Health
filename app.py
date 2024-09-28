from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

app = Flask(__name__)

# Initialize an empty DataFrame to store health data
health_data = pd.DataFrame(columns=['Date', 'HeartRate', 'Steps', 'SleepHours'])

# Route to render the main HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submissions
@app.route('/submit', methods=['POST'])
def submit_data():
    if request.method == 'POST':
        # Get data from form
        date = request.form['date']
        heart_rate = float(request.form['heart_rate'])
        steps = int(request.form['steps'])
        sleep_hours = float(request.form['sleep_hours'])

        # Create a new DataFrame with the submitted data
        new_data = pd.DataFrame([{
            'Date': date,
            'HeartRate': heart_rate,
            'Steps': steps,
            'SleepHours': sleep_hours
        }])

        # Concatenate the new data with the existing DataFrame
        global health_data
        health_data = pd.concat([health_data, new_data], ignore_index=True)

        # Redirect back to the home page
        return redirect(url_for('index'))

# Route to generate visualizations
@app.route('/visualize/<chart_type>')
def visualize(chart_type):
    global health_data
    
    # Convert the 'Date' column to datetime format for plotting
    health_data['Date'] = pd.to_datetime(health_data['Date'])
    
    # Generate the requested plot
    if chart_type == 'heart_rate':
        plt.figure(figsize=(10, 6))
        plt.plot(health_data['Date'], health_data['HeartRate'], marker='o', color='b')
        plt.title('Heart Rate Over Time')
        plt.xlabel('Date')
        plt.ylabel('Heart Rate')
        plt.grid(True)
        plt.savefig('static/heart_rate_plot.png')
        plt.close()

    elif chart_type == 'steps':
        plt.figure(figsize=(10, 6))
        plt.bar(health_data['Date'], health_data['Steps'], color='green')
        plt.title('Steps Per Day')
        plt.xlabel('Date')
        plt.ylabel('Steps')
        plt.savefig('static/steps_plot.png')
        plt.close()

    return render_template('index.html', chart_type=chart_type)

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
