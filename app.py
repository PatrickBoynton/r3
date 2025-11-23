from flask import Flask
from flask_cors import CORS
from flask_smorest import Api
from models.update_video import update_video
from db import db
from models import VideoContext
from models.create_video_context import create_video_context


# http://172.17.0.156:5000/AA1.mp4
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
        db.create_all()

        if not db.session.query(Video).first():
            create_video()
        else:
            print("Videos in the database.", flush=True)
            update_video()

        if not db.session.query(VideoContext).first():
            create_video_context()
        else:
            print('Video context exists.', flush=True)

    api.register_blueprint(VideosRoutes)
    api.register_blueprint(VideoContextRoutes)
    return app
