from flask import Flask, url_for,request, jsonify
from datetime import datetime

app = Flask(__name__)

activity_log = [
    {
        'id': 0,
        'user_id': 1,
        'username': 'john',
        'timestamp': datetime.utcnow(),
        'details': "Important stuff here",
        'location': '/api/activities/0',
    },
    {
        'id': 1,
        'user_id': 2,
        'username': 'yoko',
        'timestamp': datetime.utcnow(),
        'details': "Even more important",
        'location': '/api/activities/1',
    },

 ]

@app.route('/api/activities/<int:id>', methods=["GET"])
def single(id):
    return  jsonify(activity_log[id])
    

@app.route('/api/activities', methods=["GET"])
def all_activites():
    return jsonify({'activities': activity_log})

@app.route('/api/activities', methods=["POST"])
def new_activity():
    if not request.json:
        abort(400)
    new_act = request.get_json()
    if 'user_id' not in new_act
    or 'username' not in new_act
    or 'details' not in new_act:
        abort(400)
    new_act['id'] = 2
    new_act['location'] = url_for('single', id=2)
    new_act['timestamp'] = datetime.utcnow()
    return new_act,201
