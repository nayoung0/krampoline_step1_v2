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


@app.route('/main')
def get(): 
    return jsonify({"hello": "world!"})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3000)
