import csv
import fileinput
import re
import json
import os
from app import app, db
from sqlalchemy.sql import text as sa_text
import datetime


class Item(db.Model):
	__tablename__ = 'items'

	id = db.Column(db.Integer, primary_key=True)
	sku = db.Column(db.String())
	name = db.Column(db.String())
	path = db.Column(db.String())
	preview = db.Column(db.String())
	images = db.Column(db.String())
	docs = db.Column(db.String())
	about = db.Column(db.String())
	description = db.Column(db.String())

	def __init__(self, sku, path, name, description, preview, images, docs, about):
		self.path = path
		self.sku = sku
		self.path = path
		self.name = name
		self.description = description
		self.preview = preview
		self.images = images
		self.docs = docs
		self.about = about

	def __repr__(self):
		return '<Item {}>'.format(self.sku)

	def get_id(self):
		return str(self.id)

	def get_sku(self):
		return str(self.sku)


class Article(db.Model):
	__tablename__ = 'news'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String())
	image = db.Column(db.String())
	text = db.Column(db.String())
	link = db.Column(db.String())
	date = db.Column(db.String())

	def __init__(self, title, image, text, link, date):
		self.title = title
		self.image = image
		self.text = text
		self.link = link
		self.date = date

	def __repr__(self):
		return '<Article {}>'.format(self.id)

	def get_id(self):
		return str(self.id)

db.create_all()
db.session.commit()