from datetime import datetime
from decimal import Decimal
from typing import TYPE_CHECKING
from sqlalchemy import CheckConstraint, ForeignKey, Numeric, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.expense_history import ExpenseHistory

class Expense(Base):
    __tablename__ = "expenses"
    __table_args__ = (
        CheckConstraint("amount > 0", name="chk_expenses_amount"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    amount: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    expense_date: Mapped[datetime] = mapped_column(server_default=func.now(), nullable=False)
    created_by: Mapped[int] = mapped_column(
        ForeignKey("users.id", onupdate="CASCADE", ondelete="RESTRICT", name="fk_expenses_created_by"),
        nullable=False,
    )

    creator: Mapped["User"] = relationship(back_populates="expenses")
    histories: Mapped[list["ExpenseHistory"]] = relationship(back_populates="expense")