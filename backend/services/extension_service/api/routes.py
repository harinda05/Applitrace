from main import app
from models.advertin_model import AdvertIn 

@app.get("/")
async def base_route():
    return {"Hello world"}


@app.post("/create-my-job", status_code=201)
def create_jobboard_entry(_advertIn: AdvertIn):
    ## todo implement
    print(_advertIn)
    return {}