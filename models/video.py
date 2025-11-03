from uuid import uuid4
from db import db


class Video(db.Model):
    __tablename__: str = "videos"
    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid4)

    title = db.Column(db.String(), unique=True, nullable=False)

    url = db.Column(db.String(), unique=True, nullable=False)

    image = db.Column(db.String(), unique=True, nullable=True)

    duration = db.Column(db.Float(), nullable=False)

    uploaded_date = db.Column(db.DateTime(), nullable=False)

    video_status = db.relationship(
        "VideoStatus",
        back_populates="video",
        uselist=False,
        cascade="all, delete, delete-orphan",
    )
