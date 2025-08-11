from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base


class User(Base):
    __tablename__ = "users"
    # __table_args__ = {"extend_existing": True}

    username: Mapped[str] = mapped_column(unique=True)
