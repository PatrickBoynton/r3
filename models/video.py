from uuid import uuid4

from db import db

video_tags = db.Table(
        "video_tags",
        db.Column("video_id",
                  db.UUID(as_uuid=True),
                  db.ForeignKey("videos.id"),
                  primary_key=True),
        db.Column("tag_id",
                  db.UUID(as_uuid=True),
                  db.ForeignKey("tags.id"),
                  primary_key=True)
)


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
    tags = db.relationship("Tag", secondary=video_tags, back_populates="videos")
