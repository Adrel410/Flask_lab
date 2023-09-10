from flask import Flask, render_template   
from flask import Flask, render_template, request

app = Flask(__name__)             

@app.route("/")                  
def hello():                      
   return render_template("index.html")         
    
@app.route("/Adeola")              
def hello_name(name):              
    name = request.args.get('Adeola')
    return "Hello "+ name          

@app.route("/about")
def about():
    name = request.args.get('name') if request.args.get('name') else "Hello World!" 
    return render_template("about.html", aboutName=name)   
    
if __name__ == "__main__":        # when running python app.py
    #app.run()                     # run the flask app
    #change app.run() to the following
    app.run(debug=True)