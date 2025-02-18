from project.shared.config.database import Base

from datetime import datetime, timezone
from sqlalchemy import Column, String, Integer, TIMESTAMP, ForeignKey


class ScheduleModel(Base):
    __tablename__ = "schedules"

    id = Column(Integer, primary_key=True, index=True)
    group_id = Column(String(15), unique=True, nullable=False, index=True)
    subject = Column(String(80), nullable=False)
    schedule = Column(String(150), nullable=False)
    classroom = Column(String(150), nullable=False)
    academic_program = Column(String(40), nullable=False)
    profesor_id = Column(Integer, ForeignKey("profesors.id"), nullable=False)
    created_at = Column("created_at", TIMESTAMP, nullable=True, default=datetime.now(timezone.utc))
    updated_at = Column(
        "updated_at",
        TIMESTAMP,
        nullable=True,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc)
    )
