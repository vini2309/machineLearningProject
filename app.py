from flask import Flask

app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
def index():
    return "Starting machine learning Project and CI/CD Pipeline has been established successfully"

if __name__=="__main__":
    app.run(debug=True)