import os, uuid, json
from http.cookies import SimpleCookie
from flask import Flask, request, abort, send_from_directory

app = Flask(__name__)
UP = '/tmp/uploads'          # Vercel 只写 /tmp
os.makedirs(UP, exist_ok=True)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    # 返回静态上传页
    return send_from_directory('public', 'index.html')

@app.route('/up', methods=['POST'])
def upload():
    token = request.headers.get('X-Token') or request.form.get('token')
    if token != '你想设的口令':
        abort(401)
    f = request.files['file']
    ext = f.filename.rsplit('.', 1)[-1]
    name = f"{uuid.uuid4().hex}.{ext}"
    f.save(os.path.join(UP, name))
    return json.dumps({'url': f'/files/{name}'}), 200, {'Content-Type': 'application/json'}

@app.route('/files/<path:filename>')
def files(filename):
    return send_from_directory(UP, filename)

# Vercel 入口
if __name__ != '__main__':
    app = app