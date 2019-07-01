from peewee import *
from db import orm


def init_db():
	
	orm.Channel.create_table()
	orm.Event.create_table()