from decimal import Decimal
from typing import TYPE_CHECKING, Optional
from sqlalchemy import CheckConstraint, ForeignKey, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

if TYPE_CHECKING:
    from app.models.product_category import ProductCategory
    from app.models.production import Production
    from app.models.transaction import Transaction
    from app.models.stock import Stock

class Product(Base):
    __tablename__ = "products"
    __table_args__ = (
        CheckConstraint("selling_price > 0", name="chk_products_selling_price"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    selling_price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    category_id: Mapped[int] = mapped_column(
        ForeignKey("products_categories.id", onupdate="CASCADE", ondelete="RESTRICT", name="fk_products_category"),
        nullable=False,
    )

    category: Mapped["ProductCategory"] = relationship(back_populates="products")
    productions: Mapped[list["Production"]] = relationship(back_populates="product")
    transactions: Mapped[list["Transaction"]] = relationship(back_populates="product")
    stock: Mapped[Optional["Stock"]] = relationship(back_populates="product", uselist=False)