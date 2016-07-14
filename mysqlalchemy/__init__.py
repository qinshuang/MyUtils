# /usr/bin/python
# -*- coding:utf-8 -*-
"""
    Created by qinshuang on 7/7/16.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column, String, ForeignKey, DateTime, Table
from datetime import datetime
from lib.logutils import logger_init

logger_init(**{'sqlalchemy.engine.base.Engine': {'handler': 'console', 'level': 'debug', 'filename': 'log.log'},})

author_article = Table('author_article', Base.metadata,
                       Column('author_guid', String(32), ForeignKey('author.guid')),
                       Column('article_guid', String(32), ForeignKey('article.guid'))
                       )


class Author(Base):
    __tablename__ = "author"
    guid = Column(String(32), primary_key=True)
    name = Column(String(32), default='')
    create_time = Column(DateTime, default=datetime.now)
    modify_time = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return '<databases.Author %s>' % self.guid


class Article(Base):
    __tablename__ = "article"
    guid = Column(String(32), primary_key=True)
    name = Column(String(32), default='')
    create_time = Column(DateTime, default=datetime.now)
    modify_time = Column(DateTime, default=datetime.now)

    author = relationship("Author", secondary=author_article, backref="article")

    def __repr__(self):
        return '<databases.Article %s>' % self.guid


engine = create_engine('mysql+mysqldb://root:root@localhost:3306/mysqlalchemy?charset=utf8',
                       pool_size=5, pool_recycle=3,
                       isolation_level="READ UNCOMMITTED",
                       echo=True)
db = scoped_session(sessionmaker(bind=engine, autoflush=False))

# 创建所有表格
# Base.metadata.create_all(bind=engine)

# a = Article()
# a.guid = '12334'
# b = Author()
# b.guid = '4232'
# a.author = [b]
# db.add(a)
# db.commit()

rc = db.query(Article)
b = rc.first()
author_list = b.author

# 删除所有表格
# Base.metadata.drop_all(bind=engine)
