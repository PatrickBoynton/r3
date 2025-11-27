import os
from db import db
from models import VideoContext


def create_video_context():
    video_context = None

    if not VideoContext.query.first():
        path = "/app/data/"
        num_videos = sum(len(files) for _, _, files in os.walk(path))
        video_context = VideoContext(
            current_video=None,
            previous_video=None,
            total_videos=num_videos,
            video_plays=0,
            current_os=os.getenv("CURRENT_OS"),
        )
        db.session.add(video_context)
        db.session.commit()
    return video_context
