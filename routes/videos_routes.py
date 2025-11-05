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
    def put(self, video_id):
        video = Video.query.get_or_404(video_id)
        video_data = request.get_json()
        print(f"video to update: {video.title}")
        if video:
            print(f"Updating video: {video.title}")
            for key, value in video_data.items():
                if hasattr(video, key):
                    setattr(video, key, value)

            for key, value in video_data.get("video_status", {}).items():
                if hasattr(video.video_status, key):
                    setattr(video.video_status, key, value)

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
            if "lte" in filter_args:
                random_video = (
                    Video.query.join(VideoStatus)
                    .filter(
                        VideoStatus.played == False,
                        Video.duration <= int(filter_args["lte"]) * 60,
                    )
                    .order_by(func.random())
                    .first()
                )
            if "gte" in filter_args:
                random_video = (
                    Video.query.join(VideoStatus)
                    .filter(
                        VideoStatus.played == False,
                        Video.duration <= int(filter_args["gte"]) * 60,
                    )
                    .order_by(func.random())
                    .first()
                )
        elif "lte" in filter_args:
            random_video = (
                Video.query.filter(Video.duration <= int(filter_args["lte"] * 60))
                .order_by(func.random())
                .first()
            )
        elif "gte" in filter_args:
            random_video = (
                Video.query.filter(Video.duration >= int(filter_args["gte"] * 60))
                .order_by(func.random())
                .first()
            )
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
