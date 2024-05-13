from sqlalchemy.orm import Session
from .models import IPStats


def get_ips_from_stats(db: Session):
    all_host = db.query(IPStats).all()
    return [host.ip for host in all_host]


def insert_ip_to_stats(db: Session, stats: IPStats):
    db.add(stats)
    db.commit()
    db.refresh(stats)
    return stats
