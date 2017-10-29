# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import sessionmaker

nobel_winners = [
    {
        'category': 'Physics',
        'name': 'Albert Einstein',
        'nationality': 'Swiss',
        'sex': 'male',
        'year': 1921,
    },
    {
        'category': 'Physics',
        'name': 'Paul Dirac',
        'nationality': 'British',
        'sex': 'male',
        'year': 1933
    },
    {
        'category': 'Chemistry',
        'name': 'Marie Curie',
        'nationality': 'Polish',
        'sex': 'female',
        'year': 1911
    }
]

engine = create_engine('sqlite:///data/nobel_prize.db', echo=True)
Base = declarative_base()


class Winner(Base):
    __tablename__ = 'winners'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    year = Column(Integer)
    nationality = Column(String)
    sex = Column(Enum('male', 'female'))

    def __repr__(self):
        return "<Winner(name='%s', category='%s', year='%s')>"%(self.name, self.category, self.year)


def create_db():
    Base.metadata.create_all(engine)


def connect_test():
    Session = sessionmaker(bind=engine)
    session = Session()

    print("nobel_winners[0]", nobel_winners[0])

    albert = Winner(**nobel_winners[0])
    print("albert", albert)
    session.add(albert)
    print("session.new", session.new)
    print("session", session)

    session.expunge(albert)
    print("session.new", session.new)


def insert_winners():
    Session = sessionmaker(bind=engine)
    session = Session()

    winner_rows = [Winner(**w) for w in nobel_winners]
    session.add_all(winner_rows)
    session.commit()


def fetch_test():
    Session = sessionmaker(bind=engine)
    session = Session()
    print("データ件数", session.query(Winner).count())

    # 1. filter_by のテスト
    result = session.query(Winner).filter_by(nationality='Swiss')
    print("1. filter_by 'Swiss'", list(result))

    # 2. カラム毎の条件指定
    result = session.query(Winner).filter(Winner.category == 'Physics', Winner.nationality != 'Swiss')
    print('2. column condition', list(result))

    # 3. ID指定
    result = session.query(Winner).get(3)
    print('3. id', result)

    # 4. order by のテスト
    result = session.query(Winner).order_by('year')
    print('4. order by', list(result))

    # 5. inst_to_dictを使ったdictへの変換
    winner_rows = session.query(Winner)
    nobel_winners = [inst_to_dict(w) for w in winner_rows]
    print("dict ver", nobel_winners)

    # 6. dirtyでdry run
    marie = session.query(Winner).get(3)
    marie.nationality = 'French'
    print("current", inst_to_dict(marie))
    print("dirty", session.dirty)


def inst_to_dict(inst, delete_id=True):
    dat = {}
    print('columns', inst.__table__.columns)
    for column in inst.__table__.columns:
        dat[column.name] = getattr(inst, column.name)
    if delete_id:
        dat.pop('id')
    return dat


def update_query():
    Session = sessionmaker(bind=engine)
    session = Session()
    marie = session.query(Winner).get(3)
    marie.nationality = 'French'
    print("current", inst_to_dict(marie))
    print("dirty", session.dirty)
    session.commit()
    print("current", inst_to_dict(marie))


def delete_query():
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Winner).filter_by(name='Albert Einstein').delete()
    session.commit()


# create_db()
# insert_winners()
# fetch_test()
# update_query()
# delete_query()
Session = sessionmaker(bind=engine)
session = Session()
# delete_query()
print("list", list(session.query(Winner)))


