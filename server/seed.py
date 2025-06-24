from server.app import create_app
from server.models import db
from server.models.guest import Guest
from server.models.episode import Episode

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    guest1 =Guest(name='levi ', occupation='alive')
    guest2 =Guest(name='muturi', occupation='programmer')

    ep1= Episode(number=1, date='2025-23-01')
    ep2= Episode(number=2, date='2025-24-01')

    db.session.add_all([guest1, guest2, ep1, ep2])
    db.session.commit()

    print("database been seeded")