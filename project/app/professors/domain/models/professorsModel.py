from project.shared.config.database import Base

from datetime import datetime, timezone
from sqlalchemy import Column, String, Integer, TIMESTAMP


class professorModel(Base):
    __tablename__ = "professors"

    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String(100), nullable=False)
    identification_card = Column(Integer, unique=True, nullable=False, index=True)
    department = Column(String(50), nullable=False)
    program = Column(String(80), nullable=False)
    highest_education_level = Column(String(20), nullable=False)
    degree_obtained = Column(String(100), nullable=False)
    undergraduate_degree = Column(String(80), nullable=False)
    partnership = Column(String(15), nullable=False)
    institutional_email = Column(String(100), unique=True, nullable=False)
    personal_email = Column(String(100), unique=True, nullable=False)
    email_with_domain = Column(String(100), unique=True, nullable=False)
    faculty_location = Column(String(150), nullable=True)
    created_at = Column("created_at", TIMESTAMP, nullable=True, default=datetime.now(timezone.utc))
    updated_at = Column(
        "updated_at",
        TIMESTAMP,
        nullable=True,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc)
    )
    deleted_at = Column("deleted_at", TIMESTAMP, nullable=True)
