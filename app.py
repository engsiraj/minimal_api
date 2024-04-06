from flask import Flask, jsonify, request, Response


app = Flask(__name__)



data = {
    1: {'id':1,'name': 'John', 'age': 30, 'city': 'New York'},
    2: {'id':2,'name': 'Emily', 'age': 25, 'city': 'Los Angeles'},
    3: {'id':3,'name': 'Michael', 'age': 45, 'city': 'Chicago'},
    4: {'id':4,'name': 'Sarah', 'age': 33, 'city': 'Houston'},
    5: {'id':5,'name': 'Daniel', 'age': 28, 'city': 'San Francisco'},
    6: {'id':6,'name': 'Jessica', 'age': 36, 'city': 'Miami'},
    7: {'id':7,'name': 'Andrew', 'age': 42, 'city': 'Seattle'},
    8: {'id':8,'name': 'Olivia', 'age': 31, 'city': 'Boston'},
    9: {'id':9,'name': 'David', 'age': 37, 'city': 'Atlanta'},
    10: {'id':10,'name': 'Sophia', 'age': 29, 'city': 'Denver'},
    }

@app.route("/")
def hello_world():
    return "<div><h1>this is other Api </h1><p>Api data is on /users and /user/id</p></div>"

@app.route('/users',methods=['GET','POST'])
def users_list():

    if request.method == 'GET':
        if len(data) > 0:
            return jsonify(data)
        else:
            return 'not found', 404
        
    if request.method == 'POST':
        user_data = request.json
        if not user_data:
            return Response('invalid data',status=400)
        else:
            new_user_id = max(data.keys())+1
            user_data['id'] = new_user_id
            data[new_user_id] = user_data
            return jsonify(user_data,201)
        
@app.route('/user/<int:id>',methods=['GET','PUT','DELETE'])
def user(id):
    if request.method =='GET':
       user = data.get(id)
       if user:
           return jsonify(user),200
       else:
           return Response('user not found', status=404)
       
    elif request.method =='PUT':
       user = data.get(id)
       if not user:
           return Response('user not found',status=404)
       else:
           other = request.json
           user.update(other)
           return jsonify(other),200
       
    elif request.method =='DELETE':
       user = data.pop(id,None)
       if  user:
           return Response('user deleted',status=200)
       else:
           return Response('user deleted',status=200)
       








if __name__ == '__main__':
    app.run(debug=True)
