from app import app, db
from app.models import *
from flask import jsonify


def db_get_articles():
	articles = Article.query.order_by(Article.id.desc()).limit(3)

	news = []
	for a in articles:
		news.append(vars(a))

	print(news)
	return news


	