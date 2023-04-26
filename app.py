from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/mydata')
def mydata():
    data = [
        {'name': 'John', 'age': 30, 'city': 'New York'},
        {'name': 'Jane', 'age': 25, 'city': 'Los Angeles'},
        {'name': 'Bob', 'age': 40, 'city': 'Chicago'}
    ]
    status_code = 200
    response_data = (data, status_code)
    # Adding new data to the response
    response_data = (response_data[0], response_data[1], {'is_valid': True})
    return jsonify(response_data)


if __name__ == '__main__':
    app.run()
