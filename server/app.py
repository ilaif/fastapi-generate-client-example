import typing
import fastapi
import pydantic

app = fastapi.FastAPI()

users = []


class User(pydantic.BaseModel):
    name: str


@app.get('/users', response_model=typing.List[User])
async def get_users():
    return users


@app.post('/users', response_model=User)
async def create_user(
    user: User,
):
    users.append(user)

    return user
