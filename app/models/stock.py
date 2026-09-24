from datetime import datetime
from typing import TYPE_CHECKING
from sqlalchemy import CheckConstraint, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

if TYPE_CHECKING:
    from app.models.product import Product
    from app.models.stock_history import StockHistory

class Stock(Base):
    __tablename__ = "stock"
    __table_args__ = (
        CheckConstraint("quantity >= 0", name="chk_stock_quantity"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id", onupdate="CASCADE", ondelete="RESTRICT", name="fk_stock_product"),
        unique=True,
        nullable=False,
    )
    quantity: Mapped[int] = mapped_column(default=0, nullable=False)
    last_updated: Mapped[datetime] = mapped_column(server_default=func.now(), nullable=False)

    product: Mapped["Product"] = relationship(back_populates="stock")
    histories: Mapped[list["StockHistory"]] = relationship(back_populates="stock")