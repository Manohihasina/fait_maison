from datetime import datetime
from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

if TYPE_CHECKING:
    from app.models.expense import Expense
    from app.models.user import User

class ExpenseHistory(Base):
    __tablename__ = "expense_history"

    id: Mapped[int] = mapped_column(primary_key=True)
    expense_id: Mapped[int] = mapped_column(
        ForeignKey("expenses.id", onupdate="CASCADE", ondelete="CASCADE", name="fk_expense_history_expense"),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), nullable=False)
    created_by: Mapped[int] = mapped_column(
        ForeignKey("users.id", onupdate="CASCADE", ondelete="RESTRICT", name="fk_expense_history_user"),
        nullable=False,
    )

    expense: Mapped["Expense"] = relationship(back_populates="histories")
    creator: Mapped["User"] = relationship(back_populates="expense_histories")