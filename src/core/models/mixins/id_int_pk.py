from sqlalchemy.orm import Mapped, mapped_column


class IntIdPkMxn:
    id: Mapped[int] = mapped_column(unique=True)
