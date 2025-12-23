from flask import Flask
from flask_cors import CORS
from flask_smorest import Api
from models.update_video import update_video
from db import db
from models import VideoContext
from models.create_video_context import create_video_context
from models.create_video import create_video
from utils import set_interval

def create_app():
    app = Flask(__name__, static_folder="/app/data", static_url_path="")
    CORS(app)
    # Swagger configuration
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["UPLOAD_EXTENSIONS"] = [".mp4"]
    app.config["UPLOAD_PATH"] = "/app/data"
    app.config["API_TITLE"] = "r3vids"
    app.config["API_VERSION"] = "v5"
    app.config["OPENAPI_VERSION"] = "3.1.1"
    app.config["OPENAPI_URL_PREFIX"] = ""
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/"
    app.config["OPENAPI_SWAGGER_UI_URL"] = (
        "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    )

    # SQALCHEMY configuration
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "postgresql://postgres:safepass1@database/r3vidsf"
    )

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    from models.create_video import create_video
    from models.video import Video
    from routes.videos_routes import blueprint as VideosRoutes
    from routes.video_context_routes import blueprint as VideoContextRoutes

    api = Api(app)

    with app.app_context():
        import os
        db.create_all()
        
        if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
            create_video()
        if  db.session.query(Video).first():
            update_video()


        if not db.session.query(VideoContext).first():
            create_video_context()
        else:
            print("Video context exists.", flush=True)
    
    set_interval(create_video, 900, app)
    
    api.register_blueprint(VideosRoutes)
    api.register_blueprint(VideoContextRoutes)
    
    return app
