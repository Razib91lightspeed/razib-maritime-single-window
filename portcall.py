from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>There are 42 portcalls</p><p>More ships on their way.</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
