from flask import Flask, render_template,request
import pickle
# import  sklearn

app = Flask(__name__)

model = pickle.load(open('tree.pkl','rb'))


@app.route('/')
def new():
    return render_template('index.html')

@app.route('/predi', methods=['POST'])
def predi():
    if request.method == 'POST':
        gender = request.form['gen']
        age = request.form['age']
        diabet = request.form['diabet']
        bp = request.form['bp']
        smoke = request.form['smoke']
        serum = request.form['serum']

    if gender == 'Male':
        gend = 1
    else:
        gend = 0

    if diabet == 'Yes':
        diabet = 1
    else:
        diabet = 0

    if bp == 'Yes':
        bp = 1
    else:
        bp = 0

    if smoke == 'yes':
        smoke = 1
    else:
        smoke = 0

    predict_new = model.predict([[age, gend, diabet, bp, smoke, serum]])
    output = ([predict_new])

    if predict_new == 1:
        state = "Person Will Die In The Heart Attack"
    else:
        state = "Person Will Not Die In The Heart Attack"

    print(predict_new)
    if output == 0:
        return render_template('index.html', predict_text="sorry..")
    else:
        return render_template('index.html',predict_text="{} ".format(state))
    return render_template('index.html')


if __name__ == "__main__":
 app.run(debug=True)
