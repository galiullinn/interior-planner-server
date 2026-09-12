from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.database import Base
from src.core.mixins import IntPkMixin, TimestampMixin, UuidPkMixin


class Category(IntPkMixin, TimestampMixin, Base):
    """Модель категории мебели."""

    __tablename__ = "categories"

    name: Mapped[str] = mapped_column(String(100))
    slug: Mapped[str] = mapped_column(String(200), unique=True)
    description: Mapped[str | None] = mapped_column(String(512))

    parent_id: Mapped[int | None] = mapped_column(ForeignKey("categories.id", ondelete="SET NULL"))
    parent: Mapped["Category | None"] = relationship(
        remote_side="Category.id",
        back_populates="children",
    )
    children: Mapped[list["Category"]] = relationship(back_populates="parent")

    furniture_items: Mapped[list["Furniture"]] = relationship(back_populates="category")

    def __repr__(self) -> str:
        return f"<Category(id={self.id}, name={self.name!r})>"


class Furniture(UuidPkMixin, TimestampMixin, Base):
    """Модель мебели."""

    __tablename__ = "furniture"

    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[str | None] = mapped_column(String(512))
    model_key: Mapped[str] = mapped_column(String(512))
    thumbnail_key: Mapped[str | None] = mapped_column(String(512))

    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id", ondelete="RESTRICT"))
    category: Mapped["Category"] = relationship(back_populates="furniture_items")

    def __repr__(self) -> str:
        return f"<Furniture(id={self.id}, name={self.name!r})>"
