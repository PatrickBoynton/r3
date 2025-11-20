from marshmallow import Schema, fields


class VideoStatusSchema(Schema):
    id = fields.Str(dump_only=True)
    played = fields.Boolean(required=True)
    current_play_time = fields.Float(required=True)
    play_count = fields.Integer(required=True)
    selection_count = fields.Integer(required=True)
    is_watch_later = fields.Boolean(required=True)
    last_played = fields.DateTime(required=False)


class VideoSchema(Schema):
    id = fields.Str(dump_only=True)
    title = fields.Str(required=True)
    url = fields.Str(required=True)
    image = fields.Str(required=False)
    duration = fields.Float(required=True)
    uploaded_date = fields.DateTime(required=True)
    video_status = fields.Nested(VideoStatusSchema, required=True)


class VideoContextSchema(Schema):
    id = fields.Str(dump_only=True)
    current_video = fields.Str(allow_none=True)
    total_videos = fields.Integer()

class RandomVideoQueryArgs(Schema):
    played = fields.Boolean(required=False)
    lte = fields.Integer(required=False)
    gte = fields.Integer(required=False)
