#coding:utf-8
import random
from faker import Factory

from sqlalchemy import create_engine,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import ForeignKey
from sqlalchemy import Column,String,Integer,Text

engine = create_engine('mysql+mysqldb://root@localhost:3306/blog?charset=utf8')

Base = declarative_base()

class User(Base):
	__tablename__ = "users"
	
	id = Column(Integer,primary_key=True)
	username = Column(String(64),nullable=False,index=True)
	password = Column(String(64),nullable=False)
	email = Column(String(64),nullable=False,index=True)
	articles = relationship('Article',backref='author')	
	userinfo = relationship('UserInfo',backref='user',uselist=False)
	
class Article(Base):
	__tablename__ = 'articles'
	
	id = Column(Integer,primary_key = True)
	title = Column(String(255),nullable=False,index=True)
	content= Column(Text)
	user_id=Column(Integer,ForeignKey('users.id'))
	cate_id= Column(Integer,ForeignKey('categories.id'))
	tags= relationship('Tag',secondary='article_tag',backref='articles')
	
class UserInfo(Base):
	__tablename__ = 'userinfos'

	id = Column(Integer,primary_key = True)
	name = Column(String(64))
	qq = Column(String(11))
	phone = Column(String(11))
	link = Column(String(64))
	user_id = Column(Integer,ForeignKey('users.id'))

class Category(Base):
	__tablename__ = 'categories'
	
	id = Column (Integer,primary_key = True)
	name = Column(String(64),nullable=False,index=True)
	articles=relationship('Article',backref='category')


article_tag = Table(
	'article_tag',Base.metadata,
	Column('article_id',Integer,ForeignKey('articles.id')),
	Column('tag_id',Integer,ForeignKey('tags.id'))
)

class Tag(Base):
	__tablename__ = 'tags'
	
	id = Column(Integer,primary_key = True)
	name = Column(String(64),nullable=False,index=True)

	
if __name__ == '__main__':
	Base.metadata.create_all(engine)

