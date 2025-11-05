import datetime
import os, subprocess

from models import Video
from models.video_status import VideoStatus
from db import db
from dotenv import load_dotenv

ip_address = os.getenv('IP_ADDRESS')

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


def get_ip():
    try:
        with open("/etc/resolv.conf", "r") as file:
            for line in file:
                if "nameserver" in line:
                    gateway_ip = line.split()[1]
                    print(f"Found gateway IP {gateway_ip}")
                    return gateway_ip
    except:
        print("FAIL")


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

        video = Video(
            title=os.path.splitext(file)[0],
            url=f"http://{ip_address}:5000/{file}",
            image=None,
            duration=get_duration(path + file),
            uploaded_date=datetime.datetime.now(),
            video_status=video_status,
        )
        video_to_check = db.session.query(Video).filter_by(title=video.title).first()

        if not video_to_check:
            db.session.add(video)
        else:
            continue
    db.session.commit()
    return video
