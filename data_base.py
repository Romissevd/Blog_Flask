__author__ = 'Roman Evdokimov'
__email__ = 'Romissevd@gmail.com'

from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.blog
# admin = {'login': 'admin',
#          'password': 'admin',
#         }
# db.admins.save(admin)
