from uuid import uuid4

from db import db


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = db.Column(db.String(), nullable=False)
