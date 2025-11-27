from models.video import Video
from db import db
import os

ip_address = os.getenv("IP_ADDRESS")


def update_video():
    video_to_check = db.session.query(Video).first()
    if video_to_check.url not in ip_address:
        print(f"IP ADDRESS: {ip_address}")
        videos = db.session.query(Video).all()
        for video in videos:
            video.url = f"http://{ip_address}:5001/{video.title}.mp4"
            db.session.add(video)
            db.session.commit()
    else:
        print(f"ip address: {ip_address}")
