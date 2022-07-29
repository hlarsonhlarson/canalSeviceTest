from sqlalchemy import create_engine, MetaData, Column, Table, Integer, Date, Float, BigInteger
from environment import user, password, hostname, database_name


engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{hostname}/{database_name}')

with engine.connect() as connection:
    if not engine.dialect.has_table(connection, database_name):
        metadata = MetaData(engine)
        # Create a table with the appropriate Columns
        Table(database_name, metadata,
              Column('Id', Integer, primary_key=True, nullable=False),
              Column('Our Number', Integer),
              Column('Delivery time', Date),
              Column('Order Number', BigInteger),
              Column('Price USD', Float),
              Column('Price RUB', Float))
        metadata.create_all()
