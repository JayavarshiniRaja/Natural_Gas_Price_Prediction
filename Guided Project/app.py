from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('DecisionTree.pkl')

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST','GET'])
def predict():
    # s = request.form['ip']
    # s = s.split('-')
    # s = ''.join(s)
    # t = model.predict(np.array(int(s)).reshape(-1,1))
    s = [i for i in request.form.values()]
    for i in range(3):
        if len(s[i])==1:
            s[i] = '0'+s[i]
    temp = s[0]+'-'+s[1]+'-'+s[2]
    s = [int(i) for i in s]
    s = (s[2]*100+s[1])*100+s[0]
    t = model.predict(np.array(s).reshape(-1,1))
    return render_template('index.html', prediction_text="The Price is %.2f $ on the DATE: "%t[0]+temp)
    # return render_template('index.html', prediction_text=s)

if __name__=='__main__':
    app.run(debug=True)
