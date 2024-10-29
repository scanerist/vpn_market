from sqlalchemy import Column, Integer, String, ForeignKey, BigInteger
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.database.base import Base

class Key(Base):
    __tablename__ = "keys"

    key: Mapped[str] = mapped_column(primary_key=True)
    status: Mapped[str] = mapped_column(String(255))
    user_id : Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship("User", back_populates="keys")
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    number_of_buys: Mapped[int] = mapped_column(Integer)
    number_of_active_keys: Mapped[int] = mapped_column(Integer)
    keys: Mapped[list["Key"]] = relationship("Key", back_populates="user")
