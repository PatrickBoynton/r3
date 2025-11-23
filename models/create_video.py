import datetime
import os
import subprocess

from db import db
from models import Video
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
    video_to_check = db.session.query(Video).first()
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
        print(f"File: {file}", flush=True)
        video = Video(
            title=os.path.splitext(file)[0],
            url=f"http://{ip_address}:5001/{file}",
            image=None,
            duration=get_duration(path + file),
            uploaded_date=datetime.datetime.now(),
            video_status=video_status,
        )
        
        if not video_to_check:
            db.session.add(video)
        else:
            continue

    db.session.commit()
    return video
