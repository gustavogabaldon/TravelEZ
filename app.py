from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

budget_data = {}


@app.route('/')
def home():
    return render_template('home.html')



@app.route('/budget', endpoint='budget') 
def budget_page():
    return render_template('budget.html')


@app.route('/expenses', endpoint='expenses')
def expenses():
    return render_template('expenses.html')

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
