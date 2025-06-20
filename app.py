app = Flask(__name__)

@app.route("/todo")
def todo():
    return render_template("todo.html")