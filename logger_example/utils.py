import logging

def create_logger(
    name: str,
    filename: int
    ):

    logger = logging.getLogger(name)
    # NOTE: remember to set level for the logger, default is warninig....
    logger.setLevel(logging.DEBUG)
    s_h = logging.StreamHandler()
    f_h = logging.FileHandler(filename)

    s_f = logging.Formatter("%(levelname)s:%(name)s:%(message)s")
    f_f = logging.Formatter("%(levelname)s:%(name)s:%(message)s")
    s_h.setLevel(logging.NOTSET)
    f_h.setLevel(logging.NOTSET)

    s_h.setFormatter(s_f)
    f_h.setFormatter(f_f)

    logger.addHandler(s_h)
    logger.addHandler(f_h)


    return logger
