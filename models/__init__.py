#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

storage = DBStorage() if os.getenv(
        'HBNB_TYPE_STORAGE') == 'db' else FileStorage()

storage.reload()
