from flask import Flask, render_template, request
import utils
app = Flask(__name__) 

@app.route('/') 
def home(): 
    return render_template('index.html')

@app.route('/predict/', methods=['GET', 'POST']) 
def predict(): 
    if request.method == 'POST': 
        sepal_length = request.form.get('sepal_length',type=float)
        sepal_width = request.form.get('sepal_width',type=float)
        petal_length = request.form.get('petal_length',type=float)
        petal_width = request.form.get('petal_width',type=float) 

    prediction = utils.preprocessdata(sepal_length,sepal_width, petal_length, petal_width) 

    if prediction==0:
        prediction="Iris-setosa" 
    elif prediction==1:
        prediction="Iris-versicolor"
    else:
        prediction="Iris-virginica"

    return render_template('predict.html', prediction=prediction) 
if __name__ == '__main__': 
    app.run(debug=True) 