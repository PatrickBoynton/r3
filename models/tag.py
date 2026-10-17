from uuid import uuid4

from db import db
from models.video import video_tags

class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = db.Column(db.String(), nullable=False)
    videos = db.relationship("Video", secondary=video_tags,  back_populates="tags")
