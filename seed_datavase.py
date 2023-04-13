from server import app
import os
import model
import crud

os.system('dropdb reservations')
os.system('createdb reservations')

model.connect_to_db(app)
app.app_context().push()
model.db.create_all()

"""Seeding for test Users"""

for n in range(10):
    email = f'user{n}@test.com' 
    user = crud.create_user(email)
    model.db.session.add(user)

model.db.session.commit()