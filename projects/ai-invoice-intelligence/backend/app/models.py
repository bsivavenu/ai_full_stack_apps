from sqlalchemy import Column, Integer, String, Text, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    file_type = Column(String)
    raw_text = Column(Text)
    
    # New Structured Fields
    vendor = Column(String, index=True)
    invoice_number = Column(String)
    date = Column(String)  # Stored as YYYY-MM-DD
    total_amount = Column(Float)
    
    created_at = Column(DateTime, default=datetime.utcnow)