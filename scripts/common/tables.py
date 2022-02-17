from sqlalchemy import Column, Float, Integer, String, Date, cast
from sqlalchemy.orm import declarative_base, column_property

Base = declarative_base()

class SearchTermsAll(Base):
    __tablename__ = "search_terms_all"
    id = Column(Integer, primary_key=True)
    date_of_search = Column(String(55))
    ad_group_id = Column(String(55))
    campaign_id = Column(String(55))
    clicks = Column(Integer)
    cost = Column(Float)
    conversion_value = Column(Float)
    conversions = Column(Integer)
    search_term = Column(String(255))