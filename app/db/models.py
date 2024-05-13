"""
小项目，不将模型分开
"""

from sqlalchemy import Column, String
from .databases import Base


class IPStats(Base):
    __tablename__ = "ip_stats"

    ip = Column(String, primary_key=True, index=True)

    def __repr__(self):
        return self.ip
