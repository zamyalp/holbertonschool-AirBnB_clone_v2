#!/usr/bin/python3
"""This module defines a class User"""
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
<<<<<<< HEAD
    __tablename__ = 'users'
    email = Column(
        String(128), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    password = Column(
        String(128), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    first_name = Column(
        String(128), nullable=True
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    last_name = Column(
        String(128), nullable=True
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    places = relationship(
        'Place',
        cascade="all, delete, delete-orphan",
        backref='user'
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else None
    reviews = relationship(
        'Review',
        cascade="all, delete, delete-orphan",
        backref='user'
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else None
=======
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")
>>>>>>> e8b9892ed9f286b5d44f2bae3c4eb670207c9646
