from main import engine, Base


#Drop table
Base.metadata.drop_all(engine)