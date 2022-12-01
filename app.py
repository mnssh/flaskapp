#Create an API in Flask

from flask import Flask,request,render_template

app = Flask(__name__,template_folder='Template')
@app.route('/',methods=['GET','POST'])
def home():
    return render_template('Index.html')

    
if __name__ == '__main__':
    app.run(debug=False)