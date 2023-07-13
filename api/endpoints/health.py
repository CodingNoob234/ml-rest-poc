import logging
logger = logging.getLogger(__name__)
from fastapi import APIRouter

router = APIRouter()

@router.get("/readiness")
def readiness():
    # Add your readiness logic here
    return {"status": "ok"}

@router.get("/liveness")
def liveness():
    # Add your liveness logic here
    return {"status": "ok"}