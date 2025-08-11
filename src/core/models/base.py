from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        # Лучше добавить проверку на абстрактные классы
        if cls.__dict__.get("__abstract__", False):
            return None
        return cls.__name__.lower()

    id: Mapped[int] = mapped_column(primary_key=True)


class User(Base):
    __tablename__ = "users"
    # __table_args__ = {"extend_existing": True}

    username: Mapped[str] = mapped_column(unique=True)
