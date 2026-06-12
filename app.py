from flask import Flask, send_file, request
from datetime import datetime

app = flask.Flask(__name__)

@app.route('/download')
def download_image():
    ip = flask.request.remote_addr
    time = datetime.now()

    # تسجيل البيانات
    with open("logs.txt", "a") as f:
        f.write(f"IP: {ip} | Time: {time}\n")

    # إرسال الصورة
    return flask.send_file("image.jpg", as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    import flask
from datetime import datetime
import os

app = flask.Flask(__name__)

@app.route('/download')
def download_image():
    ip = flask.request.remote_addr
    time = datetime.now()

    # تسجيل IP
    with open("logs.txt", "a") as f:
        f.write(f"IP: {ip} | Time: {time}\n")

    # مسار الصورة
    image_path = os.path.join("images", "product.jpg")

    return flask.send_file(image_path, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))