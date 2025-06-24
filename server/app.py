from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from server.models import db
from server.config import Config
from server.controllers.auth_controller import auth_bp
from server.controllers.episode_controller import episode_bp
from server.controllers.guest_controller import guest_bp
from server.controllers.appearance_controller import appearance_bp


migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
     

    db.init_app(app)
    migrate.init_app(app, db)
    JWTManager(app)
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(episode_bp)
    app.register_blueprint(guest_bp)
    app.register_blueprint(appearance_bp)

    @app.route('/')
    def index():
        return "<h1>late-show -api</h1>"
    
    with app.app_context():
        db.create_all

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)