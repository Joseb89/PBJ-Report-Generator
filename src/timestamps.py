import os

from datetime import datetime

from sqlalchemy import create_engine, DateTime, Float, Integer, select, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy.exc import SQLAlchemyError
from file_reader import create_timestamps

class Base(DeclarativeBase):
    pass

class Timestamp(Base):

    __tablename__ = "employee_work_days"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    employee_id: Mapped[str] = mapped_column(String(30), nullable=False)
    clock_in_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    total_hours: Mapped[float] = mapped_column(Float, nullable=False)
    job_code: Mapped[int] = mapped_column(Integer, nullable=False)
    pay_code: Mapped[int] = mapped_column(Integer, nullable=False)

class Database():

    def __init__(self):
        username = os.getenv("MYSQL_USERNAME")
        password = os.getenv("MYSQL_PASSWORD")
        host = os.getenv("MYSQL_HOST")
        database = os.getenv("MYSQL_DATABASE")

        self.databse_url = f"mysql+pymysql://{username}:{password}@{host}:{3306}/{database}"

        self.engine = create_engine(self.databse_url)

    def create_tables(self):
        Base.metadata.create_all(self.engine)

    def insert_timestamps(self):
        with Session(self.engine) as session:
            try:
                timestamps = create_timestamps()

                for timestamp in timestamps:
                    employee_id = timestamp.get("employee_id")
                    clock_in_date = timestamp.get("clock_in_date")
                    total_hours = timestamp.get("total_hours")
                    job_code = timestamp.get("job_code")
                    pay_code = timestamp.get("pay_code")

                    new_timestamp = Timestamp(employee_id=employee_id, clock_in_date=clock_in_date, 
                                              total_hours=total_hours, job_code=job_code, 
                                              pay_code=pay_code)

                    session.add(new_timestamp)
                    session.commit()
            except SQLAlchemyError as e:
                print(e)

    def select_all_timestamps(self):            
        with Session(self.engine) as session:
            try:
                statement = select(Timestamp.employee_id, Timestamp.clock_in_date, Timestamp.total_hours,
                             Timestamp.job_code, Timestamp.pay_code).order_by(Timestamp.employee_id, Timestamp.clock_in_date)
                
                return session.execute(statement)
            except SQLAlchemyError as e:
                print(e)

    def select_timestamps_by_employee_id(self, employee_id: str) -> list[Timestamp]:
        with Session(self.engine) as session:
            try:
                statement = select(Timestamp).where(Timestamp.employee_id == employee_id)

                session.scalars(statement).all()
            except SQLAlchemyError as e:
                print(e)   