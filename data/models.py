import sqlalchemy
from .db_session import SqlAlchemyBase


class Models(SqlAlchemyBase):
    __tablename__ = 'models'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True, unique=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False, default="", unique=True)
    file = sqlalchemy.Column(sqlalchemy.String, nullable=False, default="")