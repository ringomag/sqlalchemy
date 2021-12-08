from main import Session,engine,Hero


local_session=Session(bind=engine)


hero_to_delete=local_session.query(Hero).filter(Hero.alias=="Iron Man").first()

local_session.delete(hero_to_delete)

local_session.commit()