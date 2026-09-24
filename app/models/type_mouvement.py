from typing import TYPE_CHECKING
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

if TYPE_CHECKING:
    from app.models.stock_history import StockHistory

class TypeMouvement(Base):
    __tablename__ = "type_mouvement"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

    stock_histories: Mapped[list["StockHistory"]] = relationship(back_populates="type_mouvement")