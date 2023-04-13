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
    fname = f'tester{n}'
    email = f'user{n}@test.com' 
    password = 'test'

    user = crud.create_user(fname, email, password)
    model.db.session.add(user)

model.db.session.commit()