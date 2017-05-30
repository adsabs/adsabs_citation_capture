# -*- coding: utf-8 -*-
"""
Models use to define the database

The database is not initiated here, but a pointer is created named db. This is
to be passed to the app creator within the Flask blueprint.
"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import synonym

db = SQLAlchemy() # must be run in the context of a flask application
