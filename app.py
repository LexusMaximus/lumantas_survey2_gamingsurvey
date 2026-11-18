import hashlib

from sqlmodel import Session

from database import create_db_and_tables, engine
from models import GamingSurvey, Users


def main():
    create_db_and_tables()

    demo_user = Users(
        name="demo",
        password=hashlib.sha256("demo123".encode()).hexdigest(),
    )

    survey1 = GamingSurvey(
        in_game_name="Lexus",
        gpu_brand="NVIDIA",
        gpu_model="RTX 4070",
        vram="12GB",
        console="PC",
        favorite_game="Valorant",
        genre="FPS",
        resolution="1440p",
        mouse="Logitech G Pro X Superlight",
        keyboard="Wooting 60HE",
    )
    survey2 = GamingSurvey(
        in_game_name="LetMeSoloHer",
        gpu_brand="AMD",
        gpu_model="RX 7800 XT",
        vram="16GB",
        console="PS5",
        favorite_game="Elden Ring",
        genre="Action RPG",
        resolution="4K",
        mouse="Razer Viper V3 Pro",
        keyboard="Keychron Q1",
    )
    survey3 = GamingSurvey(
        in_game_name="DarkShadow",
        gpu_brand="NVIDIA",
        gpu_model="RTX 3060",
        vram="12GB",
        console="Nintendo Switch",
        favorite_game="The Legend of Zelda: Tears of the Kingdom",
        genre="Adventure",
        resolution="1080p",
        mouse="Pulsar X2",
        keyboard="Royal Kludge RK61",
    )

    with Session(engine) as session:
        session.add(demo_user)
        session.add(survey1)
        session.add(survey2)
        session.add(survey3)
        session.commit()


if __name__ == "__main__":
    main()