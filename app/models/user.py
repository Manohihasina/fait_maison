from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

if TYPE_CHECKING:
    from app.models.role import Role
    from app.models.production import Production
    from app.models.transaction import Transaction
    from app.models.transaction_history import TransactionHistory
    from app.models.expense import Expense
    from app.models.expense_history import ExpenseHistory
    from app.models.stock_history import StockHistory

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    role_id: Mapped[int] = mapped_column(
        ForeignKey("roles.id", onupdate="CASCADE", ondelete="RESTRICT", name="fk_users_role"),
        nullable=False,
    )

    role: Mapped["Role"] = relationship(back_populates="users")
    productions: Mapped[list["Production"]] = relationship(back_populates="creator")
    transactions_created: Mapped[list["Transaction"]] = relationship(back_populates="creator")
    transaction_histories: Mapped[list["TransactionHistory"]] = relationship(back_populates="creator")
    expenses: Mapped[list["Expense"]] = relationship(back_populates="creator")
    expense_histories: Mapped[list["ExpenseHistory"]] = relationship(back_populates="creator")
    stock_histories: Mapped[list["StockHistory"]] = relationship(back_populates="creator")