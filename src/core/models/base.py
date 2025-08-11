from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column

from .mixins.id_int_pk import IntIdPkMxn


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        # Лучше добавить проверку на абстрактные классы
        if cls.__dict__.get("__abstract__", False):
            return None
        return cls.__name__.lower()


class User(IntIdPkMxn, Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(unique=True)
    # __table_args__ = {"extend_existing": True}
