from flask import Flask, render_template

app = Flask(__name__)

# 模擬一些部落格文章
posts = [
    {
        "id": 1,
        "title": "Flask 入門教學",
        "author": "小明",
        "content": "這是我的第一篇 Flask 部落格文章，Flask 是個輕量又好用的 Python Web 框架。"
    },
    {
        "id": 2,
        "title": "Jinja2 模板語法簡介",
        "author": "小華",
        "content": "Jinja2 是 Flask 內建的模板引擎，讓我們可以用簡單語法嵌入資料到 HTML 中。"
    }
]

@app.route("/")
def index():
    return render_template("index.html", posts=posts)

@app.route("/post/<int:post_id>")
def show_post(post_id):
    # 根據 ID 找出文章
    post = next((p for p in posts if p["id"] == post_id), None)
    if post:
        return render_template("post.html", post=post)
    else:
        return "<h1>找不到這篇文章 😢</h1>", 404

if __name__ == "__main__":
    app.run(debug=True)
