from sqlalchemy import Column, ForeignKey, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.types import Integer, Text, String

from environment import get_env

Base = declarative_base()
DATABSE_URI = f'{"mysql"}://{get_env().DB_USER}' \
              f':{get_env().DB_PASSWORD}@{get_env().DB_HOST}' \
              f':{get_env().DB_PORT}/{get_env().DB_DATABASE}'


engine = create_engine(DATABSE_URI, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

class Bank_Transaction(Base):
    __tablename__ = 'bank_transaction'
    id = Column(Integer, primary_key=True)
    date_time = Column(DateTime)
    description = Column(Text)
    amount = Column(Integer)
    category = relationship('Transaction_Category', back_populates='bank_transaction')
    account_institution_organization = Column(String(500))
    account_institution_fid = Column(String(500))
    account_account_id = Column(String(500))
    account_number = Column(String(500))
    account_routing_number = Column(String(500))
    account_branch_id = Column(String(500))
    account_type = Column(String(500))
    account_statement = Column(String(500))
    memo = Column(String(500))
    payee = Column(String(500))
    type = Column(String(500))
    date = Column(String(500))
    user_date = Column(String(500))
    sic = Column(String(500))
    mcc = Column(String(500))
    checknum = Column(String(500))


class Transaction_Category(Base):
    __tablename__ = 'transaction_category'
    id = Column(Integer, primary_key=True)
    description = Column(Text)
    name = Column(String(500))
    bank_transaction = relationship('bank_transaction', back_populates='projects')

Base.metadata.create_all(engine)

def get_bank_transaction_from_db(bank_transaction: Bank_Transaction):
    crash_db = session.query(Bank_Transaction).filter(Bank_Transaction.id == bank_transaction.id,
                                                      Bank_Transaction.amount == bank_transaction.amount).first()
    return crash_db




def save_bank_transaction_to_db(bank_transaction: Bank_Transaction):
    session.add(bank_transaction)
    session.commit()




