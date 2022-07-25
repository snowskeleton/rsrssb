from sqlalchemy import Column, String, create_engine, Boolean, update, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from parser import parse

import os


# this feels like the wrong way to find the users home foler, but it works for now.
path = 'sqlite:///' + os.path.expanduser('~') + '/.rsrssb/library.db'

Base = declarative_base()

def _bindBook(book: dict):
    engine = create_engine(path)
    Base.metadata.create_all(engine)
    db = sessionmaker(bind=engine)()

    # try:
    db.add(Book(**(book)))
    db.commit()
    # except:
        # logger.info(
        #     "Tried to add duplicate entry. Nothing done."
        # )

def _getBook(asin: str):
    engine = create_engine(path)
    Base.metadata.create_all(engine)
    db = sessionmaker(bind=engine)()
    return db.query(Book).values(asin).one()

def _getSome(author):
    engine = create_engine(path)
    Base.metadata.create_all(engine)
    db = sessionmaker(bind=engine)()
    return db.query(Book).where(Book.authors == author)

def _getAll() -> dict:
    from utils import tsv2json
    a = tsv2json(parse.audible_cli_data())
    return a
    engine = create_engine(path)
    Base.metadata.create_all(engine)
    db = sessionmaker(bind=engine)()
    return db.query(Book).all()


def _updateBook(asin: str, **params) -> None:
    engine = create_engine(path)
    Base.metadata.create_all(engine)
    upd = update(Book).values(params).where(Book.asin == asin)
    engine.execute(upd)


def _burnBook(book: dict) -> None:
    engine = create_engine(path)
    Base.metadata.create_all(engine)
    db = sessionmaker(bind=engine)()
    db.delete(book)
    db.commit()


def _burnLibrary():
    library = _getAll()
    for book in library:
        _burnBook(book)


def rebuildLibrary():
    library = tsv2json(parse.audible_cli_data())
    for book in library:
        path = (book['title'] + ': ' +
                book['subtitle'] if book['subtitle'] != '' else book['title'])
        book['filePath'] = path + '.mp3'
        if book['asin']:
            _updateBook(book['asin'], filePath=book['filePath'])
        else:
            _bindBook(book)


def _is_downloaded(asin) -> bool:
    book = _getBook(asin)
    return book.downloaded if book.downloaded else False


class Book(Base):
    __tablename__ = "book"
    asin               = Column(String, primary_key=True)
    title              = Column(String)
    genres             = Column(String)
    rating             = Column(String)
    authors            = Column(String)
    filePath           = Column(String)
    subtitle           = Column(String)
    narrators          = Column(String)
    cover_url          = Column(String)
    date_added         = Column(String)
    downloaded         = Column(Boolean, default=False)
    description        = Column(String)
    num_ratings        = Column(String)
    is_finished        = Column(String)
    release_date       = Column(String)
    series_title       = Column(String)
    series_sequence    = Column(String)
    percent_complete   = Column(String)
    runtime_length_min = Column(String)
#     attrs = [
# self.asin,
# self.title,
# self.genres,
# self.rating,
# self.authors,
# self.filePath,
# self.subtitle,
# self.narrators,
# self.cover_url,
# self.date_added,
# self.downloaded,
# self.description,
# self.num_ratings,
# self.is_finished,
# self.release_date,
# self.series_title,
# self.series_sequence,
# self.percent_complete',
# self.runtime_length_min',
    # ]
    # def __init__(self, book: dict):
    #     for attr in self.attrs:
    #         attr
