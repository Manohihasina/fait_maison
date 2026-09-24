from datetime import datetime
from typing import TYPE_CHECKING
from sqlalchemy import CheckConstraint, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

if TYPE_CHECKING:
    from app.models.stock import Stock
    from app.models.user import User
    from app.models.type_mouvement import TypeMouvement

class StockHistory(Base):
    __tablename__ = "stock_history"
    __table_args__ = (
        CheckConstraint("quantity_ajouter_ou_enleve <> 0", name="chk_stock_history_quantity"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    stock_id: Mapped[int] = mapped_column(
        ForeignKey("stock.id", onupdate="CASCADE", ondelete="CASCADE", name="fk_stock_history_stock"),
        nullable=False,
    )
    quantity_ajouter_ou_enleve: Mapped[int] = mapped_column(nullable=False)
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), nullable=False)
    created_by: Mapped[int] = mapped_column(
        ForeignKey("users.id", onupdate="CASCADE", ondelete="RESTRICT", name="fk_stock_history_user"),
        nullable=False,
    )
    type_mouvement_id: Mapped[int] = mapped_column(
        ForeignKey("type_mouvement.id", onupdate="CASCADE", ondelete="RESTRICT", name="fk_stock_history_type"),
        nullable=False,
    )

    stock: Mapped["Stock"] = relationship(back_populates="histories")
    creator: Mapped["User"] = relationship(back_populates="stock_histories")
    type_mouvement: Mapped["TypeMouvement"] = relationship(back_populates="stock_histories")