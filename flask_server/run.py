import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify
from werkzeug.utils import secure_filename
from flask_restful import reqparse
from flask_cors import CORS
import time
import json
# 모듈 임포트
from FastStyleTransfer.run import FastStyleTransfer


# 업로드 폴더가 있는 절대경로를 받아온다.
UPLOAD_DIR = os.getcwd()
# 플라스크 서버 시작
app = Flask(__name__)
app.config['UPLOAD_DIR'] = UPLOAD_DIR + '/static/'
# CORS
CORS(app, resources={r'*': {'origins': 'http://localhost:8080'}})
# 나중에 올릴 떄 여기 바꿔줘야함
url_path = "https://i02b103.p.ssafy.io/"

# 패스트 스타일
@app.route('/faststyletransfer', methods=['POST'])
def images_main():
    f = request.files['photo']
    # print(request.form)
    image_type = request.form['type']
    fname = secure_filename(f.filename)
    path = os.path.join(app.config['UPLOAD_DIR'] +
                        "faststyletransfer/content/", fname)
    f.save(path)
    result = FastStyleTransfer(image_type, path)
    return jsonify(path=url_path + "/static/faststyletransfer/result/" + result)

# 서버 시작
if __name__ == '__main__':
    app.run(debug=True)
