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

@app.route('/todos',methods=['GET','POST'])
def task_list():
    conn = db_con()
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor = conn.execute("SELECT * FROM Todo")
        tasks = [
        dict(id=row[0], title=row[2],task=row[2])
        for row in cursor.fetchall()
        ]
        if tasks is not None:
            return jsonify(tasks),200
   
 
    if request.method == 'POST':
       new_title = request.form["title"]
       new_task = request.form["task"]
       sql = '''INSERT INTO Todo (title,task) VALUES(?,?)'''
       cursor = cursor.execute(sql,(new_title, new_task))
       conn.commit()
       return  f"{cursor.lastrowid} added"
     
@app.route('/todo/<int:id>',methods=['GET','PUT','DELETE'])
def todo(id):
    conn = db_con()
    cursor = conn.cursor()
    todo =None
    if request.method == 'GET':
        cursor.execute(' SELECT * FROM Todo Where id=?',(id,))
        rows = cursor.fetchall()
        for r in rows:
            todo = r
        if todo is not None:
            return jsonify(todo)
        else:
            return jsonify({'error': 'Not found'}), 404
        
    if request.method == 'PUT':
        sql = '''UPDATE Todo SET title=?,task=? WHERE id=?'''
        title = request.form["title"]
        task = request.form["task"]
        new_todo = {
            'id':id,
            'title':title,
            'task':task
        }
        cursor = cursor.execute(sql,(title, task,id))
        conn.commit()
        return jsonify(new_todo)

    if request.method =='DELETE':
        sql = '''DELETE FROM Todo Where id=?'''
        cursor = cursor.execute(sql,(id,))
        conn.commit()
        return f"{id} has been deleted"

if __name__ == '__main__':
    app.run(debug=True)



# .venv\Scripts\activate