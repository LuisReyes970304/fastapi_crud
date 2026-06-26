from db.fake_db import fake_db, document
import json

async def data_management():
    with open(document, "w") as file:
        json.dump(fake_db, file, indent=4)