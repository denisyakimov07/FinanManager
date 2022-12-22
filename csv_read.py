import codecs
from ofxparse import OfxParser
from streamlit.runtime.uploaded_file_manager import UploadedFile

from db_core import Bank_Transaction


def serialize_bofa_csv_data(uploaded_file: UploadedFile):
    with codecs.open(f'tempDir/{uploaded_file.name}') as fileobj:
        ofx = OfxParser.parse(fileobj)
    for transaction in ofx.account.statement.transactions:
        new_bank_transaction = Bank_Transaction()
        new_bank_transaction.date_time = transaction.
        new_bank_transaction.description = Column(Text)
        new_bank_transaction.amount = Column(Integer)
        new_bank_transaction.category = relationship('Transaction_Category', back_populates='bank_transaction')
        new_bank_transaction.account_institution_organization = Column(String(500))
        new_bank_transaction.account_institution_fid = Column(String(500))
        new_bank_transaction.account_account_id = Column(String(500))
        new_bank_transaction.account_number = Column(String(500))
        new_bank_transaction.account_routing_number = Column(String(500))
        new_bank_transaction.account_branch_id = Column(String(500))
        new_bank_transaction.account_type = Column(String(500))
        new_bank_transaction.account_statement = Column(String(500))
        new_bank_transaction.memo = Column(String(500))
        new_bank_transaction.payee = Column(String(500))
        new_bank_transaction.type = Column(String(500))
        new_bank_transaction.date = Column(String(500))
        new_bank_transaction.user_date = Column(String(500))
        new_bank_transaction.sic = Column(String(500))
        new_bank_transaction.mcc = Column(String(500))
        new_bank_transaction.checknum = Column(String(500))


account = ofx.account
# print(account.institution.organization)        # The account number
# print(account.institution.fid)        # The account number
# print(account.account_id)        # The account number
# print(account.number)       # The account number (deprecated -- returns account_id)
# print(account.routing_number)    # The bank routing number
# print(account.branch_id)         # Transit ID / branch number
# print(account.type)              # An AccountType object
# print(account.statement)        # A Statement object
# print(account.institution)       # An Institution object


# print(ofx.account.statement.transactions)
# print(ofx.account.account_id)
# print(ofx.account.routing_number)
# print(ofx.account.routing_number)







    print(x.memo)
    print(x.payee)
    print(x.type)
    print(x.date)
    print(x.user_date)
    print(x.sic)
    print(x.mcc)
    print(x.checknum)
    print('***************************')