from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

history = []


@app.route('/')
def input():
    return render_template('input_r.html', history=history[-5:])


@app.route('/result')
def result():
    a = request.args.get('a', None)
    b = request.args.get('b', None)

    if a and b:
        multiplication_result = int(a) * int(b)
        history.append(f'{a} * {b} = {multiplication_result}')
        return render_template('result.html', a=a, b=b, multiplication_result=multiplication_result)

    return 'jedna z liczb nie została podana'


if __name__ == '__main__':
    app.run(debug=True)
