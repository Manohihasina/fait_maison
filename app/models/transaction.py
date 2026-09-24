from datetime import datetime
from decimal import Decimal
from typing import TYPE_CHECKING
from sqlalchemy import CheckConstraint, ForeignKey, Numeric, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

if TYPE_CHECKING:
    from app.models.product import Product
    from app.models.status import Status
    from app.models.user import User
    from app.models.transaction_history import TransactionHistory

class Transaction(Base):
    __tablename__ = "transactions"
    __table_args__ = (
        CheckConstraint("quantity > 0", name="chk_transactions_quantity"),
        CheckConstraint("unit_price > 0", name="chk_transactions_unit_price"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id", onupdate="CASCADE", ondelete="RESTRICT", name="fk_transactions_product"),
        nullable=False,
    )
    quantity: Mapped[int] = mapped_column(nullable=False)
    vendeur: Mapped[str] = mapped_column(String(100), nullable=False)
    unit_price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    status_id: Mapped[int] = mapped_column(
        ForeignKey("status.id", onupdate="CASCADE", ondelete="RESTRICT", name="fk_transactions_status"),
        nullable=False,
    )
    transaction_date: Mapped[datetime] = mapped_column(server_default=func.now(), nullable=False)
    created_by: Mapped[int] = mapped_column(
        ForeignKey("users.id", onupdate="CASCADE", ondelete="RESTRICT", name="fk_transactions_created_by"),
        nullable=False,
    )

    product: Mapped["Product"] = relationship(back_populates="transactions")
    status: Mapped["Status"] = relationship(back_populates="transactions")
    creator: Mapped["User"] = relationship(back_populates="transactions_created")
    histories: Mapped[list["TransactionHistory"]] = relationship(back_populates="transaction")