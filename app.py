from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3


app = Flask(__name__)
CORS(app)

def db_con():
    conn =None
    try:
        conn = sqlite3.connect('todo.sqlite')
    except sqlite3.Error as e:
        print(e)
    return conn

@app.route("/")
def hello_world():
    return "<div><h1>this is other Api </h1><p>Api data is on /users and /user/id</p></div>"

@app.route('/todos',methods=['GET','POST','OPTIONS'])
def task_list():
    conn = db_con()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor = conn.execute("SELECT * FROM Todo")
        tasks = [
        dict(id=row[0], title=row[1],task=row[2])
        for row in cursor.fetchall()
        ]
        if tasks is not None:
            return jsonify(tasks),200
   
    if request.method == 'POST':
        data = request.get_json()
        app.logger.info(data)
        title = data["title"]
        task = data["task"]
        sql = 'INSERT INTO Todo (title,task) VALUES( ?,? )'
        cursor = cursor.execute(sql,(title, task))
        conn.commit()
        return jsonify({'Added': f'{cursor.lastrowid}'}),200
    
    if request.method == "OPTIONS":
        response = app.make_response("")
        response.headers["Access-Control-Allow-Origin"] = "http://localhost:5173"  
        response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"  
        response.headers["Access-Control-Allow-Headers"] = "Content-Type"  
        return response
     

@app.route('/todo/<int:id>',methods=['GET','PUT','DELETE'])
def todo(id):
    conn = db_con()
    cursor = conn.cursor()
    todo =None

    if request.method == 'GET':
        cursor.execute('SELECT * FROM Todo Where id=?',(id,))
        rows = cursor.fetchall()
        for r in rows:
            todo = r
        if todo is not None:
            return jsonify(todo) ,200
        else:
            return jsonify({'error': 'Not found'}), 404
        
    if request.method == 'PUT':
        try:
            data = request.get_json()
            title = data['title']
            task = data['task']
            sql = 'UPDATE Todo SET title=?, task=? WHERE id=?'
            cursor.execute(sql, (title, task, id))
            conn.commit()
            return jsonify({'updated': f'{id}'}), 200
        except sqlite3.Error as err:
            print(f"Error updating data: {err}")
            return jsonify({'error': 'Database error'}), 500

    if request.method =='DELETE':
        sql = 'DELETE FROM Todo Where id=?'
        cursor = cursor.execute(sql,(id,))
        conn.commit()
        return f"{id} has been deleted",200

if __name__ == '__main__':
    app.run(debug=True)



# .venv\Scripts\activate
#  app.logger.info(data)