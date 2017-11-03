__author__ = 'Roman Evdokimov'
__email__ = 'Romissevd@gmail.com'

from pymongo import MongoClient

connection = MongoClient('localhost', 27017)

db = connection.blog
# admin = {'login': 'admin',
#          'password': 'admin',
#         }
# db.admins.save(admin)
