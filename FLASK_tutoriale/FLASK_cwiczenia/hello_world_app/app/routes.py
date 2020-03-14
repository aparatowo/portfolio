from app import app

@app.route('/')
@app.route('/index')
def index():
    return 'Hello World!\n' \
           'This is an "app" app :)\n' \
           'And it have debug mode!'