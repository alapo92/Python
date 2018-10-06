from flask import Flask

app = Flask(__name__)  #    python variable that gives a file a unique name


@app.route('/')     # 'http://www.google.com/' last slash indicates home page
def home():
    return 'Hello, World!'


app.run(port=5000)

#   going to a page always sends a GET
