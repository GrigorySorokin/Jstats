from peewee import *
from db import orm


print('1123')
def init_db():

	orm.Channel.create_table()
	orm.Event.create_table()