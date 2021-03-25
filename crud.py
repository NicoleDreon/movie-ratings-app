"""CRUD operations."""

from model import db, User, Movie, Ratings, connect_to_db


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=self.email, password=self.password)

    db.session.add(user)
    db.session.commit()

    return user


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
