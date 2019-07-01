from peewee import *


class Channel(Model):
	
	chan = CharField()

	class Meta:
		database = SqliteDatabase('jan.db')


class Event(Model):

	event = CharField()
	ch_rel = ForeignKeyField(Channel, related_name='events')

	class Meta:
		database = SqliteDatabase('jan.db')