from flask.views import MethodView
from flask_smorest import Blueprint
from db import db
from models import Video, VideoContext, VideoStatus
from schemas import VideoSchema, RandomVideoQueryArgs
from sqlalchemy.sql.expression import func
from models.create_video import create_video
from flask import request
from datetime import datetime

blueprint = Blueprint("videos", __name__, description="Operations on videos")


# http://192.168.1.156:5000/
@blueprint.route("/videos")
class VideoList(MethodView):
    @blueprint.response(200, VideoSchema(many=True))
    def get(self):
        return Video.query.all()

    @blueprint.response(204)
    def put(self):
        videos = Video.query.all()
        video_context = VideoContext.query.all()
        for video in videos:
            video.video_status.played = False
            video.video_status.current_play_time = 0
            video.video_status.selection_count = 0
            video.video_status.play_count = 0
            video.video_status.is_watch_later = False
            video.video_status.last_played = None

        for context in video_context:
            context.current_video = None

        db.session.commit()
        print(f"Video status reset.")
        return ""


# http://192.168.1.156:5000/guid
@blueprint.route("/videos/<string:id>")
class SingleVideo(MethodView):
    @blueprint.response(200, VideoSchema)
    def get(self, id):
        video = Video.query.get_or_404(id)
        video_context = VideoContext.query.first()
        print(f"video selected: {video.title}")
        if video_context:
            video_context.current_video = video.id
        else:
            video_context.current_video = VideoContext(current_video=video.id)
            db.session.add(video_context)

        video.video_status.selection_count += 1
        video.video_status.played = True
        video.video_status.last_played = datetime.now()

        db.session.commit()

        return video

    @blueprint.response(200, VideoSchema(many=False))
    def put(self, id):
        video = Video.query.get(id)
        video_data = request.get_json()
        print(f"video to update: {video.title}")
        if video:
            print(f"Updating video: {video.title}")
            video.id = video_data["id"]
            video.title = video_data["title"]
            video.url = video_data["url"]
            video.image = video_data["image"]
            video.duration = video_data["duration"]
            video.uploaded_date = video_data["uploaded_date"]
            video.video_status.id = video_data["video_status"]["id"]
            video.video_status.played = video_data["video_status"]["played"]
            video.video_status.current_play_time = video_data["video_status"][
                "current_play_time"
            ]
            video.video_status.play_count = video_data["video_status"]["play_count"]
            video.video_status.selection_count = video_data["video_status"][
                "selection_count"
            ]
            video.video_status.is_watch_later = video_data["video_status"][
                "is_watch_later"
            ]
            video.video_status.last_played = video_data["video_status"]["last_played"]
            db.session.commit()
        else:
            print("No video, creating new video.")
            video = Video(**video_data)
            db.session.add(video)
            db.session.commit()

        print(f"Returning video: {video.title}")

        return video


# http://192.168.1.156:5000/videos/random
# Filter for newly played videos:
# http://192.168.1.156:5000/videos/random?played=false
@blueprint.route("/videos/random")
class VideoRandom(MethodView):
    @blueprint.arguments(RandomVideoQueryArgs, location="query")
    @blueprint.response(200, VideoSchema)
    def get(self, filter_args):
        if "played" in filter_args:
            random_video = (
                Video.query.join(VideoStatus)
                .filter(VideoStatus.played == False)
                .order_by(func.random())
                .first()
            )
            print(f"Unplayed video picked: {random_video.title}")
        else:
            random_video = Video.query.order_by(func.random()).first()

        random_video.video_status.selection_count += 1
        random_video.video_status.played = True
        random_video.video_status.last_played = datetime.now()

        print(f"random video selected: {random_video.title}", flush=True)
        video_context = VideoContext.query.first()

        if video_context:
            video_context.current_video = random_video.id
            db.session.commit()
        else:
            print("No video context.")
            video_context = VideoContext(current_video=random_video.id)
            db.session.add(video_context)

        db.session.commit()
        return random_video


@blueprint.route("/videos/upload")
class VideoUpdate(MethodView):
    @blueprint.response(201, VideoSchema)
    def post(self):
        uploaded_file = request.files["file"]
        if uploaded_file.filename != "":
            uploaded_file.save(uploaded_file.filename)
            create_video()
        return ""
