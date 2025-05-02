from sqlalchemy import Boolean, Integer, String, TIMESTAMP, func
from sqlalchemy.orm import DeclarativeBase, mapped_column, validates

class Base(DeclarativeBase):
    pass

class Note(Base):
    __tablename__ = "notes"

    id = mapped_column(Integer, primary_key=True)
    content = mapped_column(String(200))
    is_done = mapped_column(Boolean, default=False)
    created_at = mapped_column(TIMESTAMP, server_default=func.now())

    def to_dict(self):
        return {
            "id": self.id,
            "content": self.content,
            "is_done": self.is_done,
            "created_at": self.created_at
        }
    
    @validates("content")
    def validates_content(self, key, value):
        if not len(value) >= 10 :
            raise ValueError(f'{key} must be at least 5 characters long')
        return value