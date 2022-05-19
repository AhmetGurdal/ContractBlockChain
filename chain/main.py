#from chain.src.chain import Chain
from fastapi import FastAPI, Request
import asyncio

#docChain = Chain()
app = FastAPI()


@app.post("/logini")
async def login(request : Request):
    return request.json()


@app.post("/signUp/")
async def _signUp(firstname: str, lastname: str, password: str, ss : str, email : str, phone : str):
    # - firstname
    # - lastname
    # - social security number
    # - phone
    # - email
    # - password
    # - private_key
    # - public_key
    # - last_login_at
    # - created_at
    #error  HTTPException(status_code=400, detail="Blockchain is not valid")
    pass

@app.post("/forgot/")
async def _forgot(email: str):
    pass

# @app.get("/chain/")
# async def _get_chain():
#     return docChain.chain


# @app.get("/docs/{user_id}")
# async def _get_user_docs():
#     return docChain.chain

# @app.get("/docs/{doc_id}")
# async def _get_doc():
#     return docChain.chain

# @app.get("/notifications/{user_id}")
# async def _get_notifications():
#     return docChain.chain


# @app.post("/doc/approve")
# async def _get_notifications():
#     # UserID
#     # Password
#     # DocID

#     return docChain.chain
