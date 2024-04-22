# app.py

from flask import Flask, render_template
import pandas as pd
from sort_algorithms import heap_sort, quick_sort
import time

app = Flask(__name__)

CSV_FILE_PATH = 'Cost_of_Living_Index_2022.csv'

@app.route('/expenses')
@app.route('/expenses')
def expenses():
    global_df = pd.read_csv(CSV_FILE_PATH, header=0)
    global_df.columns = ['Rank', 'Country', 'Cost of Living Index', 'Rent Index', 'Cost of Living Plus Rent Index', 'Groceries Index', 'Restaurant Price Index', 'Local Purchasing Power Index']

    data_to_sort = global_df[['Country', 'Cost of Living Index']].dropna()

    # Timing heap sort
    start_time = time.perf_counter()
    data_to_sort_sorted_heap = data_to_sort.sort_values(by='Cost of Living Index', ascending=False, kind='heap')
    heap_time = time.perf_counter() - start_time
    most_expensive_heap = data_to_sort_sorted_heap.head(5)[['Country', 'Cost of Living Index']].values.tolist()
    least_expensive_heap = data_to_sort_sorted_heap.tail(5)[['Country', 'Cost of Living Index']].values.tolist()

    # Timing quick sort
    start_time = time.perf_counter()
    data_to_sort_sorted_quick = data_to_sort.sort_values(by='Cost of Living Index', ascending=False)  
    quick_time = time.perf_counter() - start_time
    most_expensive_quick = data_to_sort_sorted_quick.head(5)[['Country', 'Cost of Living Index']].values.tolist()
    least_expensive_quick = data_to_sort_sorted_quick.tail(5)[['Country', 'Cost of Living Index']].values.tolist()


    heap_time_str = "{:.5f}".format(heap_time)
    quick_time_str = "{:.5f}".format(quick_time)

    return render_template('expenses.html', 
                           heap_time=heap_time_str, quick_time=quick_time_str,
                           most_expensive_heap=most_expensive_heap, least_expensive_heap=least_expensive_heap,
                           most_expensive_quick=most_expensive_quick, least_expensive_quick=least_expensive_quick)


@app.route('/')
def home():
    return render_template('home.html')



@app.route('/budget', endpoint='budget') 
def budget_page():
    return render_template('budget.html')


@app.route('/tips', endpoint='tips')
def tips_page():
    return render_template('tips.html')




@app.route('/budget/save', methods=['POST'])
def save_budget():
    content = request.json
    user_id = content['userId'] 
    budget_data[user_id] = content['data']
    return jsonify({"message": "Data saved successfully"}), 200

@app.route('/budget/load/<user_id>', methods=['GET'])
def load_budget(user_id):
    data = budget_data.get(user_id, {})
    return jsonify(data), 200

if __name__ == "__main__":
    app.run(debug=True)
