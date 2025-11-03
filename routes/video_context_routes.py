from models import Video, VideoContext
from flask.views import MethodView
from flask_smorest import Blueprint
from schemas import VideoSchema

blueprint = Blueprint("video-context", __name__, "Operations on video context")


@blueprint.route("/video-context")
class VideoContextList(MethodView):
    @blueprint.response(200, VideoSchema)
    def get(self):
        video_context = VideoContext.query.first()
        current_video = Video.query.get(video_context.current_video)
        return current_video
