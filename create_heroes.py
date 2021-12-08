from main import engine, Base

#Create table
Base.metadata.create_all(engine)