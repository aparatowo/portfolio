from flask import Flask, render_template, request

app = Flask(__name__)
haslo_haselko = 'haslo_haselko'

@app.route('/login', methods=['get'])
# @app.route('/', methods=['get', 'post'])
def login_form():
    return render_template('login.html')

@app.route('/pass', methods=['post'])
def show_pass():
    # login_input = request.form.get('login_input')
    pass_input = request.form.get('pass_input')
    correct_pass = 'Gratulacje! <fanfary.wave>'
    wrong_pass = 'Niestety... <small_violin_plays_sad_music.wave>'
    if pass_input == haslo_haselko:
        pass_input = correct_pass
    else:
        pass_input = wrong_pass


    return render_template('pass.html', pass_input=pass_input)


if __name__ == '__main__':
    app.run()
