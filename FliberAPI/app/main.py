import logging
import os
import sys

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from app.api.routes.api import api_router
from app.core.config import settings

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)-s:     "
           "%(asctime)s %(funcName)s() L%(lineno)-2d %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

app = FastAPI()


@app.exception_handler(Exception)
async def exception_callback(request: Request, exc: Exception):
    logger.error(f"path={request.url.path}: {type(exc).__name__} {str(exc.__cause__)}")

    if type(exc).__name__ == "ValueError":
        return JSONResponse({"exception": type(exc).__name__, "detail": str(exc)}, status_code=400)
    if type(exc).__name__ == "IntegrityError":
        return JSONResponse({"exception": type(exc).__name__, "detail": str(exc.__cause__)}, status_code=400)

    return JSONResponse({"exception": type(exc).__name__, "detail": str(exc)}, status_code=500)


# @app.middleware("http")
# async def log_requests(request, call_next):
#     logger.info(f"path={request.url.path}")
#     start_time = time.time()
#
#     response = await call_next(request)
#
#     process_time = (time.time() - start_time) * 1000
#     formatted_process_time = '{0:.2f}'.format(process_time)
#     logger.info(f"completed_in={formatted_process_time}ms status_code={response.status_code}")
#
#     return response


os.environ["TZ"] = settings.TIMEZONE
# time.tzset()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_V1_STR)

if not os.path.exists("images/signature"):
    os.makedirs("images/signature")

if not os.path.exists("files/cas_files"):
    os.makedirs("files/cas_files")

SIGNATURE_FOLDER = os.path.join("static", "images/signature")
app.mount("/image", StaticFiles(directory="images/signature"), name="static")

CAS_FOLDER = os.path.join("static", "files/cas_files")
app.mount("/files", StaticFiles(directory="files/cas_files"), name="static")


@app.get("/")
async def main():
    return {"status": "ok"}


if __name__ == "__main__":
    pass
