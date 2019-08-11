import unittest
from gvlswing_app import app, db
from gvlswing_app.models import Administrator


class AdministratorModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'  # database constructed in memory
        db.create_all()

    def tearDown(self):
        db.drop_all()
        db.session.remove()  # remove all database objects from memory

    def test_registration_to_db(self):
        new_user = Administrator(username="testuser", email="test@example.com")
        db.session.add(new_user)
        db.session.commit()

        exists = Administrator.query.filter_by(username="testuser").first()

        self.assertEqual(new_user, exists)


if __name__ == '__main__':
    unittest.main(verbosity=2)

# end tests
