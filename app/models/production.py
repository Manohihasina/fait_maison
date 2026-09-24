from datetime import datetime
from typing import TYPE_CHECKING
from sqlalchemy import CheckConstraint, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

if TYPE_CHECKING:
    from app.models.product import Product
    from app.models.user import User

class Production(Base):
    __tablename__ = "production"
    __table_args__ = (
        CheckConstraint("quantity > 0", name="chk_production_quantity"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id", onupdate="CASCADE", ondelete="RESTRICT", name="fk_production_product"),
        nullable=False,
    )
    quantity: Mapped[int] = mapped_column(nullable=False)
    created_by: Mapped[int] = mapped_column(
        ForeignKey("users.id", onupdate="CASCADE", ondelete="RESTRICT", name="fk_production_user"),
        nullable=False,
    )
    production_date: Mapped[datetime] = mapped_column(server_default=func.now(), nullable=False)

    product: Mapped["Product"] = relationship(back_populates="productions")
    creator: Mapped["User"] = relationship(back_populates="productions")