from flask import Flask           # import flask framework
app = Flask(__name__)             # create an app instance

@app.route("/")                   # use the home url
def hello():                      # method called hello
    return "Hello World!"         # returns "hello world"
if __name__ == "__main__":        # when running python app.py
    #app.run()                     # run the flask app
    #change app.run() to the following
    app.run(debug=True)
