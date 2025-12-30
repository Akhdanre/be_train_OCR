from flask import Flask
from config import Config


def create_app(config_class=Config):
    """Application factory function."""
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    # db.init_app(app)
    # migrate.init_app(app, db)
    
    # # Register blueprints
    # app.register_blueprint(main_bp)
    # app.register_blueprint(user_bp, url_prefix='/api/users')
    
    # Create database tables
    # with app.app_context():
    #     db.create_all()
    
    return app
