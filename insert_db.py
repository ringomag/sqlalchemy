from main import Hero, Session, engine


#Insert in table
heroes=[
    {
        "hero_name":"Tony Stark",
        "alias":"Iron man",
    },
    {
        "hero_name":"Bruce Banner",
        "alias":"Hulk",
    },
    {
        "hero_name":"Steve Rogers",
        "alias":"Captain America",
    },
]

local_session = Session(bind=engine)

for hero in heroes:
    new_user = Hero(hero_name=hero['hero_name'], alias=hero["alias"])
    local_session.add(new_user)
    local_session.commit()

    print(f"Added {hero['hero_name']}")



