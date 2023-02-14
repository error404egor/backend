import sqlalchemy
from .db_session import SqlAlchemyBase
from werkzeug.security import generate_password_hash, check_password_hash


class User(SqlAlchemyBase):
    __tablename__ = 'user'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True, unique=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False, default="", unique=False)
    mail = sqlalchemy.Column(sqlalchemy.String, nullable=False, default="", unique=True)
    password = sqlalchemy.Column(sqlalchemy.String, nullable=False, default="", unique=False)

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
