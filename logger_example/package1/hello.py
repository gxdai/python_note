from utils import create_logger

logger = create_logger(__name__, "hello.log")

def hello():
    logger.warning("Hello world")
    logger.error("test error")
    logger.info("info")