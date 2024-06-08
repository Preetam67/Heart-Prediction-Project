# importing the libraries
from flask import Flask,render_template,request,url_for
import pickle

#Global variables
import os
app=Flask(__name__)
loaded_model=pickle.load(open('heart.pkl','rb'))
imageFolder = os.path.join('static', 'image')
print(imageFolder)
app.config['UPLOAD_FOLDER'] = imageFolder

# @app.route('/')
@app.route('/')
def home():
    
    
    return render_template("index.html")
    
    
#user defined routes

@app.route('/form')
def form():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'formdoc.svg')
    return render_template("form.html", user_image=pic1)   

@app.route("/")
def fome():
    return render_template('form.html')


@app.route("/result",methods=['POST','GET'])
def result():
    age=float(request.form['age'])
    creatinine_phosphokinase=float(request.form['creatinine_phosphokinase'])
    ejection_fraction=float(request.form['ejection_fraction'])
    platelets=float(request.form['platelets'])
    serum_creatinine=float(request.form['serum_creatinine'])
    serum_sodium=float(request.form['serum_sodium'])
    sex=float(request.form['sex'])
    time=float(request.form['time'])

    
    prediction=loaded_model.predict([[age,creatinine_phosphokinase,ejection_fraction,platelets,serum_creatinine,serum_sodium,sex,time]])[0]
    
    if prediction==0:
        return render_template('result.html')
    else:
        return render_template('result2.html') 
        
    
if __name__ =='__main__':
    app.run(debug=True) 


