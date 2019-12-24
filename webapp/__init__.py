from flask import Flask
from webapp.model import db, Station 

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    return app  

app = create_app()

@app.route('/hi')
def index():
    return 'hi'
    





