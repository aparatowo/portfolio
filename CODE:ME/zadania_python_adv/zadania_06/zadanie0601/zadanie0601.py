from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def input():
    return render_template('input.html')


@app.route('/result')
def result():
    return render_template('result.html')


if __name__ == '__main__':
    app.run(debug=True)
