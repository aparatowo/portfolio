# Rafał Nitychoruk
from flask import Flask, render_template, request, make_response
from werkzeug.utils import redirect

app = Flask(__name__, template_folder='.')


@app.route('/')
def index():
    theme = 'light'
    theme_from_cookie = request.cookies.get('theme')
    if theme_from_cookie == 'dark' or theme_from_cookie == 'light':
        theme = request.cookies.get('theme')

    visit_count = 0
    if request.cookies.get('visit'):
        visit_count = int(request.cookies.get('visit'))

    context = {
        'visit_count': (visit_count + 1),
        'theme': theme
    }

    response = make_response(render_template('index.html', **context))
    response.set_cookie(key='visit',
                        value=str(context['visit_count']),
                        max_age=None)
    print(response)
    return response


@app.route('/set_theme')
def set_color_palette():
    palette = request.args.get('theme')

    response = make_response(redirect('/'))
    response.set_cookie(key='theme',
                        value=palette,
                        max_age=None)
    return response


if __name__ == '__main__':
    app.run(debug=True)
