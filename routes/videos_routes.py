import random
from datetime import datetime

from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint
from sqlalchemy import desc
from sqlalchemy import func

from db import db
from models import Video, VideoContext, VideoStatus, create_video
from schemas import VideoSchema, RandomVideoQueryArgs

blueprint = Blueprint("videos", __name__, description="Operations on videos")


def update_random_video(random_video):
    random_video.video_status.selection_count += 1
    random_video.video_status.played = True
    random_video.video_status.last_played = datetime.now()

    print(f"Video selected: {random_video.title}", flush=True)
    video_context = VideoContext.query.first()
    video_context.video_plays += 1
    video_context.current_video = random_video.id
    db.session.add(video_context)

    db.session.commit()


# http://192.168.1.156:5000/
@blueprint.route("/videos")
class VideoList(MethodView):
    @blueprint.response(200, VideoSchema(many=True))
    def get(self):
        played_videos = Video.query.join(VideoStatus).filter_by(played=True).all()
        videos = Video.query.order_by(Video.title).all()

        if played_videos:
            return (
                Video.query.join(VideoStatus)
                .order_by(desc(VideoStatus.last_played).nulls_last())
                .all()
            )
        else:
            return videos

    @blueprint.response(204)
    def put(self):
        videos = Video.query.all()
        video_context = VideoContext.query.first()
        for video in videos:
            video.video_status.played = False
            video.video_status.current_play_time = 0
            video.video_status.selection_count = 0
            video.video_status.play_count = 0
            video.video_status.is_watch_later = False
            video.video_status.last_played = None

            video_context.current_video = None
            video_context.previous_video = None
            video_context.video_plays = 0

        db.session.commit()
        print(f"Video status reset.")
        return ""

    @blueprint.response(204)
    def patch(self):
        videos = Video.query.all()
        for video in videos:
            video.video_status.play_count = 0
            video.video_status.selection_count = 0

        db.session.commit()
        print("Video plays and selections reset.")


# http://192.168.1.156:5000/guid
@blueprint.route("/videos/<string:video_id>")
class SingleVideo(MethodView):
    @blueprint.response(200, VideoSchema)
    def get(self, video_id):
        video = Video.query.get_or_404(video_id)
        video_context = VideoContext.query.first()
        video_context.video_plays += 1
        print(f"video selected: {video.title}")

        video_context.current_video = video.id
        db.session.add(video_context)

        video.video_status.selection_count += 1
        video.video_status.played = True
        video.video_status.last_played = datetime.now()

        db.session.commit()

        return video

    @blueprint.response(200, VideoSchema(many=False))
    def put(self, video_id):
        video = Video.query.get(video_id)
        video_data = request.get_json()

        if video:
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
    def get(self, args):
        videos = db.session.query(Video).join(VideoStatus).all()

        print(f"request url: {request.url}", flush=True)

        filters = {
            "lte": lambda v: Video.duration <= v * 60,
            "gte": lambda v: Video.duration >= v * 60
        }

        for arg, condition in filters.items():
            value = request.args.get(arg)
            print(f"value: {value}", flush=True)
            if value is not None:
                # Keep int around value, it doesn't read value as an int otherwise, because it is a string naturally.
                videos = db.session.query(Video).where(condition(int(value))).all()
        # Closer to 1, stronger variety, closer to 0 more repeats.
        #  add an ** and a number after the divisor to tune:  (video.video_status.selection_count + 1) ** 2
        weights = [1 / (video.video_status.selection_count + 1) for video in videos]

        random_video = random.choices(videos, weights=weights, k=1)[0]
        print(f"Video duration: {random_video.duration / 60}", flush=True)

        update_random_video(random_video)

        return random_video


@blueprint.route("/videos/random/new")
class NewRandomVideo(MethodView):
    @blueprint.arguments(RandomVideoQueryArgs, location="query")
    @blueprint.response(200, VideoSchema)
    def get(self, args):
        minimum_plays = db.session.query(func.min(VideoStatus.selection_count)).scalar()
        videos = db.session.query(Video).join(VideoStatus).filter(VideoStatus.selection_count == minimum_plays).all()

        filters = {
            "lte": lambda v: Video.duration <= v * 60,
            "gte": lambda v: Video.duration >= v * 60
        }

        for arg, condition in filters.items():
            value = request.args.get(arg)
            print(f"value: {value}", flush=True)
            if value is not None:
                videos = db.session.query(Video).where(condition(int(value))).all()

        random_video = random.choice(videos)

        update_random_video(random_video)

        db.session.commit()
        return random_video


@blueprint.route("/videos/upload")
class VideoUpdate(MethodView):
    @blueprint.response(201, VideoSchema)
    def post(self):
        uploaded_file = request.files["file"]
        if uploaded_file.filename != "":
            uploaded_file.save("/app/data/" + uploaded_file.filename)
            create_video()
            print(f"Video added: {uploaded_file.filename}", flush=True)

        return ""
