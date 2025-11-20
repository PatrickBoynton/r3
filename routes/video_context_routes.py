from flask.views import MethodView
from flask_smorest import Blueprint

from models import VideoContext, Video
from schemas import VideoSchema

blueprint = Blueprint("video-context", __name__, "Operations on video context")


@blueprint.route("/video-context")
class VideoContextList(MethodView):
    @blueprint.response(200)
    def get(self):
        video_context = VideoContext.query.first()
        id = video_context.id
        current_video = None
        total_videos = video_context.total_videos

        if video_context.current_video:
            cvo = Video.query.get_or_404(video_context.current_video)
            current_video = VideoSchema().dump(cvo)

        context = {
            "id": id,
            "current_video": current_video,
            "total_videos": total_videos,
        }
        return context
