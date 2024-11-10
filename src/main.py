from fastapi import FastAPI
from router import api_router

from config import global_settings

app = FastAPI()

app.include_router(api_router,
                   prefix=global_settings.API_V1_STR)

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("main:app",
                host=global_settings.BACKEND_HOST,
                port=global_settings.BACKEND_PORT,
                log_level='info', reload=True,)