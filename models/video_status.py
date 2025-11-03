from uuid import uuid4
from db import db

class VideoStatus(db.Model):
    __tablename__ = 'video_status'
    
    id = db.Column(db.UUID(as_uuid=True), 
                                primary_key=True,
                                default=uuid4)

    played = db.Column(db.Boolean(), 
                            nullable=False)

    current_play_time = db.Column(db.Float(), 
                                        nullable=False) 

    play_count = db.Column(db.Integer(), 
                                nullable=False)

    selection_count = db.Column(db.Integer(), 
                                        nullable=False)

    is_watch_later = db.Column(db.Boolean(), 
                                    nullable=False)

    last_played = db.Column(db.DateTime(), 
                                    nullable=True)
    
    video = db.relationship('Video', 
                                                        uselist=False,
                                                        back_populates='video_status')

    video_id = db.Column(db.UUID(as_uuid=True), 
                                db.ForeignKey('videos.id'),
                                unique=True,
                                nullable=False)
