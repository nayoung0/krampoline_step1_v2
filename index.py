
from flask import Flask
from flask_cors import CORS
# from flask_sqlalchemy import SQLAlchemy
from os import path

# db = SQLAlchemy()
DB_NAME = 'krampoline_step1_v2.db'

from flask import (
    Flask, 
    redirect, 
    request, 
    jsonify, 
    url_for, 
    render_template,
    Response,
    Blueprint
)

app = Flask(__name__)
CORS(app, resources={r'/api/*': {"origins": "*"}})

app.config['SECRET_KEY'] = 'semicircle_secret_key hollimoly guacamole roly poly'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///krampoline_step1_v2.db'
# db.init_app(app)

@app.route('/api/')
def home():
    return None

# 유저 생성
@app.route('/api/users', methods=['POST'])
def create_user():
    # input
    # username
    return jsonify({
        "username": "kidneybeans2"
    })
    # return jsonify()

# 지도 생성
@app.route('/api/maps', methods=['POST'])
def create_map():
    # input
    # 시작 날짜
    # 종료 날짜
    # 계절
    return jsonify({
        "start_at": "2023-12-20T00:00:00.000000+09:00",
        "end_at": "2023-12-25T00:00:00.000000+09:00",
        "season": "winter",
        "lo_1": {
            "created_at": None,
            "memo": None,
            "stamp_url": None
        },
        "lo_2": {
            "created_at": None,
            "memo": None,
            "stamp_url": None
        },
        "lo_3": {
            "created_at": None,
            "memo": None,
            "stamp_url": None
        },
        "lo_4": {
            "created_at": None,
            "memo": None,
            "stamp_url": None
        },
        "lo_5": {
            "created_at": None,
            "memo": None,
            "stamp_url": None
        },
        "lo_6": {
            "created_at": None,
            "memo": None,
            "stamp_url": None
        },
        "lo_7": {
            "created_at": None,
            "memo": None,
            "stamp_url": None
        },
        "lo_8": {
            "created_at": "2023-12-20T00:00:00.000000+09:00",
            "memo": None,
            "stamp_url": None
        },
        "lo_9": {
            "created_at": None,
            "memo": None,
            "stamp_url": None
        },
        "lo_10": {
            "created_at": None,
            "memo": None,
            "stamp_url": None
        },
        "lo_11": {
            "created_at": None,
            "memo": None,
            "stamp_url": None
        },
        "lo_12": {
            "created_at": None,
            "memo": None,
            "stamp_url": None
        },
        "lo_13": {
            "created_at": None,
            "memo": None,
            "stamp_url": None
        },
        "lo_14": {
            "created_at": None,
            "memo": None,
            "stamp_url": None
        },
        "lo_15": {
            "created_at": None,
            "memo": None,
            "stamp_url": None
        }
    })

# 지도 정보 리턴
@app.route('/api/maps', methods=['GET'])
def get_map():
    # username
    return jsonify({
        "start_at": "2023-12-20T00:00:00.000000+09:00",
        "end_at": "2023-12-25T00:00:00.000000+09:00",
        "season": "winter",
        "lo_1": {
            "created_at": None,
            "memo": None,
            "stamp_url": None
        },
        "lo_2": {
            "created_at": None,
            "memo": None,
            "stamp_url": None
        },
        "lo_3": {
            "created_at": None,
            "memo": None,
            "stamp_url": None
        },
        "lo_4": {
            "created_at": None,
            "memo": None,
            "stamp_url": None
        },
        "lo_5": {
            "created_at": None,
            "memo": None,
            "stamp_url": None
        },
        "lo_6": {
            "created_at": None,
            "memo": None,
            "stamp_url": None
        },
        "lo_7": {
            "created_at": None,
            "memo": None,
            "stamp_url": None
        },
        "lo_8": {
            "created_at": "2023-12-24T00:00:00.000000+09:00",
            "memo": "너무 예쁜 크리스마스 박물관! 딱 내 스타일이다 💖 평생 잊지 못할 크리스마스 ⛄️❄️",
            "stamp_url": "https://drive.google.com/file/d/10pWHdJfClzg2Jfcx3mIDnLlmGWLATgFx/view?usp=drive_link"
        },
        "lo_9": {
            "created_at": None,
            "memo": None,
            "stamp_url": None
        },
        "lo_10": {
            "created_at": None,
            "memo": None,
            "stamp_url": None
        },
        "lo_11": {
            "created_at": "2023-12-23T15:00:00.000000+09:00",
            "memo": "오늘 제주도의 1100고지에서 보낸 시간은 정말 꿈만 같았다. 눈으로 뒤덮인 자연 경관과 평화로움이 내 마음을 완전히 사로잡았다. 정말 잊지 못할 경험이다!🍃✨❄️",
            "stamp_url": None
        },
        "lo_12": {
            "created_at": None,
            "memo": None,
            "stamp_url": None
        },
        "lo_13": {
            "created_at": "2023-12-22T10:00:00.000000+09:00",
            "memo": "유채꽃이 하나도 안 펴있을까봐 한참 걱정했는데, 너무 예쁘게 피어있었다. 역시 제주도 여행은 겨울인가?🌼🌼",
            "stamp_url": "https://drive.google.com/file/d/1iMUDe3A3BBh_W2A2QXi7zl1-dPouAYbt/view?usp=sharing"
        },
        "lo_14": {
            "created_at": "2023-12-22T16:00:00.000000+09:00",
            "memo": "내가 가 있을 때 어떻게 꽃이 활짝 피어 있었지? 🌺 이번 제주도 나의 여행은 진짜 운이 좋다!",
            "stamp_url": "https://drive.google.com/drive/u/0/folders/1mfxrQ6ZxcdS2XnZmwWpiFr0MsMGY5gY7"
        },
        "lo_15": {
            "created_at": None,
            "memo": None,
            "stamp_url": None
        }
    })
    
# 스탬프 생성
@app.route('/api/stamps', methods=['POST'])
def create_stamp():
    # input
    # location
    # memo
    return jsonify({
        "created_at": "2023-12-20T00:00:00.000000+09:00",
        "memo": "sampple memo",
        "stamp_url": "https://files.oaiusercontent.com/file-vf8iYyD6SHG5S74z0HPAnh1K?se=2023-11-30T18%3A07%3A09Z&sp=r&sv=2021-08-06&sr=b&rscc=max-age%3D31536000%2C%20immutable&rscd=attachment%3B%20filename%3D2bcabcde-62be-421e-90b0-cdceb4fc4a5c.webp&sig=UhNVCuUq7V1I0XiYccw5hktCIvbukn7p8D%2BJGlqsTZo%3D"
    })


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
