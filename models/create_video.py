import os
import subprocess
from datetime import datetime

from db import db
from models import Video
from models.category import Category
from models.tag import Tag
from models.video_status import VideoStatus

ip_address = os.getenv("IP_ADDRESS")


def get_duration(file_name):
    result = subprocess.run(
            [
                "ffprobe",
                "-v",
                "error",
                "-show_entries",
                "format=duration",
                "-of",
                "default=noprint_wrappers=1:nokey=1",
                file_name,
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
    )
    return float(result.stdout.strip())


def create_video():
    path = "/app/data/"
    video = None

    for file in os.listdir(path):
        video_status = VideoStatus(
                played=False,
                current_play_time=0.0,
                play_count=0,
                selection_count=0,
                is_watch_later=False,
                last_played=None,
        )

        tags = Tag(name="Boo")

        category = Category(
                name="Uncategorized"
        )

        video = Video(
                title=os.path.splitext(file)[0],
                url=f"http://{ip_address}:5001/{file}",
                image=None,
                duration=get_duration(path + file),
                uploaded_date=datetime.now(),
                video_status=video_status,
                tags=[Tag(name="Boo"), Tag(name="Yah")],
        )

        if not db.session.query(Video).filter(Video.title == video.title).first():
            db.session.add(video)
        else:
            continue

    db.session.commit()

    return video
