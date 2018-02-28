from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String, DateTime, BLOB
from sqlalchemy.orm import sessionmaker
import config
Session = sessionmaker()

engine = create_engine(f'mysql+pymysql://{config.USERNAME}:{config.PASSWORD}@{config.HOST}:{config.PORT}/{config.SCHEMA}', 
                        echo=True)
Base = declarative_base()
print(engine)

Session.configure(bind=engine)
session = Session()

class CMS(Base):
    __tablename__ = 'cms'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    slug = Column(String)
    date = Column(DateTime)
    type = Column(String)
    content = Column(BLOB)

    @property
    def text(self):
        return str(self.content, 'utf-8')

    @text.setter
    def text(self, val):
        self.content = val

    @classmethod
    def get_by_slug(cls, slug):
        return session.query(cls).filter_by(slug=slug).first()

    def __repr__(self):
        return f'<CMS {self.id} - {self.title} - {self.slug} - {self.date} - {self.type}>'


