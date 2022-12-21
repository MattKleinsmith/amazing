from app.models import db, User
from app.seeds.upload import upload_image_to_bucket_from_url


def seed_all():
    db.session.add(User(
        fullname="Demo Smith",
        email="email@email.com",
        password="password"
    ))
    db.session.commit()


def undo_seed():
    db.session.execute("TRUNCATE TABLE users RESTART IDENTITY CASCADE;")
    db.session.commit()
