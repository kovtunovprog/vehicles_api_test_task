from motor.motor_asyncio import AsyncIOMotorClient


async def setup_db():
    # TODO: don't hardcode stuff for local run
    # connection string for docker-compose
    uri = "mongodb://root:example@localhost:27017"
    # connection string for default mongodb installation
    # uri = "mongodb://localhost:27017"
    db = AsyncIOMotorClient(uri).vehicles
    # await db.vehicles.drop()
    return db
