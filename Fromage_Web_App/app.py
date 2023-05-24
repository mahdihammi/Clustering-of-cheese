from flask import Flask, render_template, request
import joblib
app = Flask(__name__)


model = joblib.load('../kmeans_model.joblib')

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/predict", methods=['POST', 'GET'])
def predict():
    if request.method == 'POST' :
        calories = request.form['calories']
        sodium = request.form['sodium']
        calcium = request.form['calcium']
        lipides = request.form['lipides']
        retinol = request.form['retinol']
        folates = request.form['folates']
        proteines = request.form['proteines']
        cholesterol = request.form['cholesterol']
        magnesium = request.form['magnesium']

        data_input = [[calories,sodium,calcium,lipides,retinol,folates,proteines,cholesterol,magnesium]]

        predicted = model.predict(data_input)[0]


    return render_template('result.html', result = predicted)





if __name__ == '__main__':
    app.run(debug=True)


