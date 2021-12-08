from main import Session,engine,Hero


local_session=Session(bind=engine)

hero_to_update=local_session.query(Hero).filter(Hero.alias == 'Iron man').first()

hero_to_update.alias = "Iron man madafaka"


local_session.commit()