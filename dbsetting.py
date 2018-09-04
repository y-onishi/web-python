import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#DB作成用
Base = declarative_base()
conn = sa.create_engine('postgres://wvgugralmjwxxs:7f1f08506d3d04801067bb02ee92f806c8aac35bbba1680ef00ab9e59b7b024e@ec2-54-163-245-44.compute-1.amazonaws.com:5432/d6qg27fj5opkk1')
#conn = sa.create_engine('postgresql://y_onishi:@localhost/test1')

#レコードクラス（作成するDBの形式）
class LinkRecord(Base):
    __tablename__ = 'linktable'
    title = sa.Column('title',sa.String,primary_key=True)
    link = sa.Column('link',sa.String)
    def __init__(self, contents):
        self.title = contents[0]
        self.link = contents[1]
    def __repr__(self):
        return "<linktable({},{})>".format(self.title,self.link)

#session関連
Session = sessionmaker(bind=conn)
session = Session()
