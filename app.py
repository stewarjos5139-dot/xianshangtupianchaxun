from flask import Flask, render_template, request, send_from_directory
import os
import json
import datetime

app = Flask(__name__)

PHOTO_DIR = "photos"
CONFIRM_FILE = "confirmed.json"
FEEDBACK_FILE = "feedback.txt"


def load_confirmed():
    if os.path.exists(CONFIRM_FILE):
        with open(CONFIRM_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_confirmed(data):
    with open(CONFIRM_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search", methods=["POST"])
def search():

    last6 = request.form["id"]
    
    # 验证输入：必须是6位，且每位是数字或X
    if len(last6) != 6 or not all(c.isdigit() or c == 'X' for c in last6):
        return render_template("result.html", photos=[], id=last6, error="请输入6位数字ID（最后一位可为X）")
    
    confirmed = load_confirmed()

    result = []

    for file in os.listdir(PHOTO_DIR):

        if file.lower().endswith((".jpg", ".png", ".jpeg")):

            # 检查文件名（不含扩展名）是否以last6结尾
            base_name = file.split('.')[0]
            if base_name.endswith(last6):

                path = os.path.join(PHOTO_DIR, file)
                size = os.path.getsize(path)
                size_kb = round(size / 1024, 2)

                result.append({
                    "name": file,
                    "size": size_kb,
                    "confirmed": file in confirmed
                })

    # 如果没找到照片，传递一个空列表
    return render_template("result.html", photos=result, id=last6)


@app.route("/confirm", methods=["POST"])
def confirm():

    filename = request.form["filename"]

    confirmed = load_confirmed()

    if filename not in confirmed:

        confirmed[filename] = True
        save_confirmed(confirmed)

        with open(FEEDBACK_FILE, "a", encoding="utf-8") as f:
            f.write(f"{datetime.datetime.now()} | {filename} | 确认无误\n")

    return "确认成功 <br><a href='/'>返回查询</a>"


@app.route("/feedback", methods=["POST"])
def feedback():

    filename = request.form["filename"]
    text = request.form["text"]

    with open(FEEDBACK_FILE, "a", encoding="utf-8") as f:
        f.write(f"{datetime.datetime.now()} | {filename} | 反馈: {text}\n")

    return "反馈提交成功 <br><a href='/'>返回查询</a>"


@app.route("/photos/<filename>")
def photos(filename):
    return send_from_directory(PHOTO_DIR, filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)