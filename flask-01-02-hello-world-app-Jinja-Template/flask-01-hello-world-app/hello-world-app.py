from flask import Flask

app = Flask(__name__) 

@app.route("/home")
def home():
    return "hello from flask!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)