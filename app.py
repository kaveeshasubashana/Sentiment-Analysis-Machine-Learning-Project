from flask import Flask, render_template, request, redirect
from pipline import preprocessing, vectorizer, get_prediction


app = Flask(__name__)



data = dict()
reviews = ['good product', 'bad productr', 'i like it']
positive = 2
negative = 1

@app.route("/")
def index():
    data['reviews'] = reviews
    data['positive'] = positive
    data['negative'] = negative
    return render_template('index.html', data=data)

@app.route("/", methods = ['POST'])
def mypost():
    text = request.form['text']
    ppt=preprocessing(text)
    vd=vectorizer(ppt)
    pred=get_prediction(vd)

    if pred == 'positive':
        global positive
        positive += 1
    elif pred == 'negative':
        global negative
        negative += 1

    reviews.insert(0, text)
    return redirect(request.url)




if __name__ == "__main__":
    app.run()