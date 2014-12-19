# db_create.py - sets up and create a database


from project import db


# create the database and the db table
db.create_all()


# commit the changes
db.session.commit()