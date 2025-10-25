from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String



class Foo(Model):
    __tablename__ = "foo"
    id = Column(Integer, primary_key=True)
    field = Column(String(20))
    def __repr__(self):
        return f"id = {id}, field = {self.field}" 