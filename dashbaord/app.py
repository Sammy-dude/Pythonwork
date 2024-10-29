import pandas as pd
import matplotlib.pyplot as plt
import os
from flask import Flask, render_template

app = Flask(__name__, static_folder='static')


# Function to simulate logging test results
def log_test_results():
    data = {
        "Build Number": [1, 2, 3],
        "Passed": [100, 98, 100],
        "Failed": [3, 5, 2],
        "Flaky": [2, 1, 3]
    }
    df = pd.DataFrame(data)
    df.to_csv('test_results.csv', index=False)


# Function to generate pie chart from test results
def generate_pie_chart(build_number):
    df = pd.read_csv('test_results.csv')
    results = df[df['Build Number'] == build_number].iloc[0]

    labels = 'Passed', 'Failed', 'Flaky'
    sizes = [results['Passed'], results['Failed'], results['Flaky']]
    colors = ['green', 'red', 'yellow']
    explode = (0.1, 0, 0)  # explode the 1st slice

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')

    plt.savefig(f'static/build_{build_number}_pie_chart.png')  # Ensure path is correct
    plt.close()



@app.route('/')
def dashboard():
    log_test_results()  # Log results (you would normally do this outside of the dashboard route)
    for build in range(1, 4):
        generate_pie_chart(build)

    images = [f'build_{i}_pie_chart.png' for i in range(1, 4)]
    return render_template('dashboard.html', images=images)


if __name__ == '__main__':
    app.run(debug=True)
