from datetime import datetime
from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

if TYPE_CHECKING:
    from app.models.transaction import Transaction
    from app.models.user import User

class TransactionHistory(Base):
    __tablename__ = "transaction_history"

    id: Mapped[int] = mapped_column(primary_key=True)
    transaction_id: Mapped[int] = mapped_column(
        ForeignKey("transactions.id", onupdate="CASCADE", ondelete="CASCADE", name="fk_transaction_history_transaction"),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), nullable=False)
    created_by: Mapped[int] = mapped_column(
        ForeignKey("users.id", onupdate="CASCADE", ondelete="RESTRICT", name="fk_transaction_history_user"),
        nullable=False,
    )

    transaction: Mapped["Transaction"] = relationship(back_populates="histories")
    creator: Mapped["User"] = relationship(back_populates="transaction_histories")