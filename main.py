import os
import random
import logging
from fastapi import FastAPI

# Configure basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/process-data")
@app.post("/process-data")
def process_data():
    # 20% randomized failure rate
    if random.random() < 0.20:
        logger.error("FATAL: Connection to Redis cache lost. Shutting down.")
        os._exit(1)

    return {"status": "processed"}
