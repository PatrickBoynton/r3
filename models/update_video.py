from sqlalchemy import update
from models.video import Video
from db import db


def update_video(video):
    print("UPDATE VIDEO", flush=True)
    print(f"Video: {video}")
    # if video in db.session.dirty:
    #     db.session.commit()
    #     print('Successful change!', flush=True)
    # else:
    #     print('No changes detected.', flush=True)
