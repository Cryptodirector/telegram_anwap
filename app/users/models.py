import datetime

from app.main.database import Base
from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import mapped_column, Mapped


class Users(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    created_at: Mapped[datetime.datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())"), nullable=False
    )
    last_activity:  Mapped[datetime.datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())"), onupdate=datetime.datetime.utcnow(), nullable=True
    )


class FilmUsers(Base):
    __tablename__ = 'film_user'

    id: Mapped[int] = mapped_column(primary_key=True)
    id_film: Mapped[int] = mapped_column(nullable=True)
    id_users: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=True)
