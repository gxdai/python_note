from utils import create_logger
from package1.hello import hello


logger = create_logger(__name__, "main.log")

def main():
    import pdb; pdb.set_trace()
    logger.debug("test debug.")
    logger.info("test info: ")
    logger.warning("test warning")
    hello()


if __name__ == "__main__":
    main()