from uuid import uuid4

from db import db


class VideoContext(db.Model):
    __tablename__ = "video_context"

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid4)

    current_video = db.Column(
        db.UUID(as_uuid=True), db.ForeignKey("videos.id"), unique=True, nullable=True
    )
    previous_video = db.Column(db.UUID(as_uuid=True), db.ForeignKey('videos.id'), unique=True, nullable=True)
    total_videos = db.Column(db.Integer, default=0)
