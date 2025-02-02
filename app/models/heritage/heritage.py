from sqlalchemy import (
    Column, 
    Integer, 
    String, 
    Float, 
    DECIMAL, 
    Text, 
    DateTime,
    ForeignKey
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base

class Heritage(Base):
    __tablename__ = 'heritages'
    id = Column(Integer, primary_key=True, index=True)
    heritage_type_id = Column(Integer, ForeignKey('heritage_types.id'))
    name = Column(String(100))
    description = Column(Text)
    location = Column(String(255))
    latitude = Column(DECIMAL(10, 8))
    longitude = Column(DECIMAL(11, 8))
    radius = Column(Float)
    image_url = Column(String(255))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    heritage_types = relationship("HeritageType", back_populates="heritages")
    chat_sessions = relationship("ChatSession", back_populates="heritages")
    buildings = relationship("HeritageBuilding", back_populates="heritages")
    routes = relationship("HeritageRoute", back_populates="heritages")
    bookmarks = relationship("UserBookmark", back_populates="heritages")