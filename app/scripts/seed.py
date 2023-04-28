from app.merchandise.models import Merchandise
from app.extensions.database import db
from app.app import app
from faker import Faker

fake = Faker()

if __name__ == '__main__':
  app.app_context().push()

  for x in range(10):
    merchandise = Merchandise(
      name = fake.name(),
      description = fake.text(),
      price = fake.random_digit_not_null()
    )

    db.session.add(merchandise)

  db.session.commit()