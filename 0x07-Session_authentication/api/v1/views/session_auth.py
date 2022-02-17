#!/usr/bin/env python3
'''session auth views'''

from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'],
                 strict_slashes=False)
def login():
    '''Return User instance
    based on email'''
    user_email = request.form.get('email')
    user_password = request.form.get('password')
    if user_email is None or user_email == '':
        return jsonify({"error": "password missing"}), 400
    if user_password is None or user_password == '':
        return jsonify({"error": "password missing"}), 400
    users = User.search({'email': user_email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404
    active_user = None
    for user in users:
        if user.is_valid_password(user_password):
            active_user = user
            break
    if active_user is None:
        return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth
    session_id = auth.create_session(active_user.id)
    json_user = jsonify(active_user.to_json())
    auth.user_id_by_session_id[getenv('SESSION_NAME')] = session_id
    return json_user


@app_views.route('/auth_session/logout',
                 methods=['DELETE'],
                 strict_slashes=False)
def logout():
    '''logout functionality'''
    from api.v1.app import auth
    if auth.destroy_session(request):
        return jsonify({}), 200
    return abort(404)
