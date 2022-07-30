from sqlalchemy import create_engine, MetaData, Column, Table, Integer, Date, Float, BigInteger, insert
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text as sa_text
from environment import user, password, hostname, database_name
from datetime import datetime


table_name = 'test'
def create_deliveries_instance():
    engine = create_engine(f'postgresql://{user}:{password}@{hostname}/{database_name}')
    Session = sessionmaker(bind=engine)
    session = Session()
    Base = declarative_base()
    class Deliveries(Base):
        __tablename__ = database_name
        id = Column('Id', Integer, primary_key=True, nullable=False)
        our_number = Column('Our_Number', Integer)
        delivery_time = Column('Delivery_time', Date)
        order_number = Column('Order_Number', Integer)
        price_usd = Column('Price_USD', Float)
        price_rub = Column('Price_RUB', Float)

    Base.metadata.create_all(engine)
    return Deliveries, session

def delete_all_previous_info(deliveries_instance, session):
    session.execute(sa_text(f'''TRUNCATE TABLE {table_name} RESTART IDENTITY;''').execution_options(autocommit=False))


def insert_info_db(info, deliveries_instance, session):
    delete_all_previous_info(deliveries_instance, session)
    deliveries = []
    for elem in info:
        delivery = deliveries_instance(our_number=elem[0],
                              delivery_time=elem[1],
                              order_number=elem[2],
                              price_usd=elem[3],
                              price_rub=elem[4])
        deliveries.append(delivery)

    session.add_all(deliveries)
    session.commit()




if __name__ == '__main__':
    deliveries, session = create_deliveries_instance()
    date_time_str = '29.07.2022'
    date_time_obj = datetime.strptime(date_time_str, '%d.%m.%Y')
    info = [['140', date_time_obj, '45645645', '45.123', '456.2']]
    insert_info_db(info, deliveries, session)
