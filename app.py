from flask import Flask

app = Flask(__name__)
iprint("Hellp from app1)
@app.route("/")
def hello():
    return "Hello from Flask!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
