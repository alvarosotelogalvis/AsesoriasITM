from project.shared.config.database import Base

from datetime import datetime, timezone
from sqlalchemy import Column, String, Integer, TIMESTAMP, ForeignKey, Text
from werkzeug.security import generate_password_hash, check_password_hash

class UserModel(Base):
    __tablename__ = "logged-in_users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(80), unique=True, nullable=False)
    hash_password = Column(Text, nullable=False)
    professor_id = Column(Integer, ForeignKey("professors.id"), nullable=False)
    created_at = Column("created_at", TIMESTAMP, nullable=True, default=datetime.now(timezone.utc))
    updated_at = Column(
        "updated_at",
        TIMESTAMP,
        nullable=True,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc)
    )
    deleted_at = Column("deleted_at", TIMESTAMP, nullable=True)

    def set_password(self, password):
        self.hash_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hash_password, password)
