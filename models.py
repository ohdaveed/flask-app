import datetime
from peewee import *

DATABASE = SqliteDatabase('plants.sqlite')

class Plant(Model):
	name = CharField()
	scientific_name = CharField(null=True)
	ordr = CharField(null=True)
	image = CharField(null=True)
	created_at = DateTimeField(default=datetime.datetime.now)

	class Meta:
		database = DATABASE

def initialize():
	DATABASE.connect()
	DATABASE.create_tables([Plant], safe=True)
	print("Tables Created")
	DATABASE.close()