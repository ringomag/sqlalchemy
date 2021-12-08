from main import Session, Hero, engine
from sqlalchemy import desc


local_session = Session(bind=engine)
munja=local_session.query(Hero).all()
print(munja)


# get_id_1 = local_session.query(Hero).get(1)
# filter_thor = local_session.query(Hero).filter('alias'=='Thor).first()

#ascending order
heroes_asc=local_session.query(Hero).order_by(Hero.id).all()
print(heroes_asc)

#descending order
heroes_dsc=local_session.query(Hero).order_by(desc(Hero.id)).all()
print(heroes_dsc)