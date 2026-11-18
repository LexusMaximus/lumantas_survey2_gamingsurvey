from sqlmodel import Field, SQLModel


class Users(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    password: str


class GamingSurvey(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    in_game_name: str
    gpu_brand: str
    gpu_model: str
    vram: str
    console: str
    favorite_game: str
    genre: str
    resolution: str
    mouse: str
    keyboard: str