from flask import Flask,jsonify


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<div><h1>thi is other Api </h1><p>Api data is on /api</p></div>"


@app.route('/api')
def mydata():
    data = [
    {'name': 'John', 'age': 30, 'city': 'New York'},
    {'name': 'Emily', 'age': 25, 'city': 'Los Angeles'},
    {'name': 'Michael', 'age': 45, 'city': 'Chicago'},
    {'name': 'Sarah', 'age': 33, 'city': 'Houston'},
    {'name': 'Daniel', 'age': 28, 'city': 'San Francisco'},
    {'name': 'Jessica', 'age': 36, 'city': 'Miami'},
    {'name': 'Andrew', 'age': 42, 'city': 'Seattle'},
    {'name': 'Olivia', 'age': 31, 'city': 'Boston'},
    {'name': 'David', 'age': 37, 'city': 'Atlanta'},
    {'name': 'Sophia', 'age': 29, 'city': 'Denver'},
    {'name': 'Matthew', 'age': 38, 'city': 'Dallas'},
    {'name': 'Emma', 'age': 27, 'city': 'Phoenix'},
    {'name': 'Christopher', 'age': 44, 'city': 'Philadelphia'},
    {'name': 'Ava', 'age': 32, 'city': 'San Diego'},
    {'name': 'James', 'age': 39, 'city': 'Washington, D.C.'},
    {'name': 'Mia', 'age': 26, 'city': 'Austin'},
    {'name': 'Joseph', 'age': 43, 'city': 'Portland'},
    {'name': 'Abigail', 'age': 34, 'city': 'Nashville'},
    {'name': 'Ryan', 'age': 35, 'city': 'New Orleans'},
    {'name': 'Charlotte', 'age': 23, 'city': 'Las Vegas'},
    {'name': 'Jacob', 'age': 41, 'city': 'San Antonio'},
    {'name': 'Harper', 'age': 30, 'city': 'Minneapolis'},
    {'name': 'William', 'age': 24, 'city': 'Detroit'},
    {'name': 'Ella', 'age': 42, 'city': 'Kansas City'},
    {'name': 'Alexander', 'age': 28, 'city': 'Raleigh'},
    {'name': 'Sofia', 'age': 31, 'city': 'Orlando'},
    {'name': 'Benjamin', 'age': 33, 'city': 'Indianapolis'},
    {'name': 'Luna', 'age': 29, 'city': 'Charlotte'},
    {'name': 'Ethan', 'age': 36, 'city': 'Salt Lake City'},
    {'name': 'Liam', 'age': 27, 'city': 'Columbus'},
    {'name': 'Grace', 'age': 38, 'city': 'San Jose'},
    {'name': 'Lucas', 'age': 25, 'city': 'Tampa'},
    {'name': 'Chloe', 'age': 43, 'city': 'St. Louis'},
    {'name': 'Henry', 'age': 37, 'city': 'Pittsburgh'},
    {'name': 'Penelope', 'age': 26, 'city': 'Milwaukee'},
    {'name': 'Sebastian', 'age': 32, 'city': 'Memphis'},
    {'name': 'Avery', 'age': 40, 'city': 'Honolulu'},
    {'name': 'Jack', 'age': 23, 'city': 'Oklahoma City'},
    {'name': 'Madison', 'age': 30, 'city': 'Albuquerque'},
    {'name': 'Owen', 'age': 34, 'city': 'Boise'},
    {'name': 'Scarlett', 'age': 35, 'city': 'Anchorage'},
    {'name': 'Wyatt', 'age': 31, 'city': 'Baltimore'},
    {'name': 'Hannah', 'age': 27, 'city': 'Hartford'},
    {'name': 'Grayson', 'age': 38, 'city': 'Cincinnati'},
    {'name': 'Lily', 'age': 29, 'city': 'Providence'},
    {'name': 'Leo', 'age': 33, 'city': 'Richmond'},
    {'name': 'Victoria', 'age': 39, 'city': 'Jacksonville'},
    {'name': 'Gabriel', 'age': 24, 'city': 'Salt Lake City'},
    {'name': 'Nora', 'age': 36, 'city': 'Louisville'},
    {'name': 'Julian', 'age': 28, 'city': 'Birmingham'}
    ]
    status_code = 200
    response_data = (data, status_code)
    response_data = (response_data[0], response_data[1], {'is_valid': True})
    return jsonify(response_data)


if __name__ == '__main__':
    app.run(debug=True)
