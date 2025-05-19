from flask import Flask, request, render_template_string

app = Flask(__name__)

messages = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.form.get('message')
        if msg:
            messages.append(msg)
    return render_template_string("""
        <h1>留言板</h1>
        <form method="post">
            <input name="message" placeholder="输入留言" required>
            <input type="submit" value="提交">
        </form>
        <ul>
        {% for m in messages %}
            <li>{{ m }}</li>
        {% endfor %}
        </ul>
    """, messages=messages)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
