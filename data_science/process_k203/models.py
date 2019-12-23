from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Investment(Base):
    __tablename__ = "investments_k203"
    
    
