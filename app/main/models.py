from app.main.database import Base

from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Films(Base):
    __tablename__ = "films"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(), nullable=False)
    link: Mapped[str] = mapped_column(String(), nullable=False)


