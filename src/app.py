from flask import Flask, render_template

def create_app():
    app = Flask(__name__, template_folder='./templates', static_folder='./static')
    
    from .routes.challenges import challenges_bp
    app.register_blueprint(challenges_bp, url_prefix='/challenges')

    return app

def run_flask_app():
    from waitress import serve
    app = create_app()
    print("Flask app created, launching server...")
    serve(app, host='0.0.0.0', port=8080)
    
    
