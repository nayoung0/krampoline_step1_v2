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

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return None

# 유저 생성
@views.route('/users', methods=['POST'])
def create_user():
    # input
    # username
    return jsonify({
        "username": "kidneybeans2"
    })
    # return jsonify()

# 지도 생성
@views.route('/users/<string:username>/maps', methods=['POST'])
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
            "created_at": None,
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
@views.route('/maps', methods=['GET'])
def get_map():
    # username
    return jsonify({
        "start_at": "2023-12-20T00:00:00.000000+09:00",
        "end_at": "2023-12-25T00:00:00.000000+09:00",
        "season": "winter",
        "lo_1": {
            "created_at": "2023-12-25T00:00:00.000000+09:00",
            "memo": "",
            "stamp_url": ""
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
            "created_at": "2023-12-25T00:00:00.000000+09:00",
            "memo": "",
            "stamp_url": ""
        },
        "lo_5": {
            "created_at": "2023-12-25T00:00:00.000000+09:00",
            "memo": "",
            "stamp_url": ""
        },
        "lo_6": {
            "created_at": "2023-12-25T00:00:00.000000+09:00",
            "memo": "",
            "stamp_url": ""
        },
        "lo_7": {
            "created_at": "2023-12-25T00:00:00.000000+09:00",
            "memo": "",
            "stamp_url": ""
        },
        "lo_8": {
            "created_at": None,
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
    
# 스탬프 생성
@views.route('/stamps', methods=['POST'])
def create_stamp():
    # input
    # location
    # memo
    return jsonify({
        "created_at": "2023-12-20T00:00:00.000000+09:00",
        "memo": "sampple memo",
        "stamp_url": "https://files.oaiusercontent.com/file-vf8iYyD6SHG5S74z0HPAnh1K?se=2023-11-30T18%3A07%3A09Z&sp=r&sv=2021-08-06&sr=b&rscc=max-age%3D31536000%2C%20immutable&rscd=attachment%3B%20filename%3D2bcabcde-62be-421e-90b0-cdceb4fc4a5c.webp&sig=UhNVCuUq7V1I0XiYccw5hktCIvbukn7p8D%2BJGlqsTZo%3D"
    })

