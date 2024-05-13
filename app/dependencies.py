from .db.databases import session_maker


def get_db_session():
    with session_maker() as session:
        yield session
