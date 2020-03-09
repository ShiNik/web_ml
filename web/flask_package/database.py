from datetime import datetime
from flask_package import db
import pandas as pd

from flask_sqlalchemy import SQLAlchemy

# Saving Data To Database Storage
class FileContents(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(300), nullable=False)
	modeldata = db.Column(db.String(300), nullable=False)
	report = db.Column(db.String(1000), nullable=False)
	data = db.Column(db.LargeBinary, nullable=False)
	date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
	def __repr__(self):
		return f"Ml name('{self.name}', '{self.date}', '{self.modeldata}')"


def get_results():
	query_result = db.session.query(FileContents).all()
	results = {}
	for row in query_result:
		result = {"id":row.id,"file":row.name,"result":row.modeldata,"date":row.date, "report":row.report}
		results[row.id]=result
	return results


def get_result(id):
	query_result = db.session.query(FileContents).filter(FileContents.id == id)
	for row in query_result:
		result = {"id":row.id,"file":row.name,"result":row.modeldata,"date":row.date,"report":row.report}
	return result