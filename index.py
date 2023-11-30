import sys
from flask import (
    Flask, 
    redirect, 
    request, 
    jsonify, 
    url_for, 
    render_template,
    Response
)

app = Flask(__name__)


@app.route('/api/main')
def get(): 
    return jsonify({"hello": "world!"})

# @app.route('/users', methods=['POST'])
# def create_user():
#     payload = request.get_json()

#     print('username', payload.get('username'))
    
#     print(payload)
#     print(request.headers)
    
#     return jsonify({
#         "id": 1,
#         "start_at": "2023-12-25",
#         "end_at": "2023-12-30",
#         "username": "kidneybeans2"
#     })

# # @app.route('/users/<username>', methods=['POST'])
# # def create_user(username):
# #     payload = request.view_args.get('view_args')

# #     print('username', payload.get('username'))
    
# #     print(payload)
# #     print(request.headers)
    
# #     return jsonify({
# #         "id": 1,
# #         "start_at": "2023-12-25",
# #         "end_at": "2023-12-30",
# #         "username": "kidneybeans2"
# #     })


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
