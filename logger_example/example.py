"""default logger"""

# The logging module provides you with a default logger that allows to get started

# import logging

# logging.debug("This is a debug msg.")
# logging.info("This is an info msg.")
# logging.warning("This is a warning msg.")
# logging.error("This is an error msg.")
# logging.critical("This is an critical msg.")


"""Example output

WARNING:root:This is a warning msg.
ERROR:root:This is an error msg.
CRITICAL:root:This is an critical msg.
"""



# import logging

# logging.basicConfig(level=logging.DEBUG)

# logging.debug("This is a debug msg.")
# logging.info("This is an info msg.")
# logging.warning("This is a warning msg.")
# logging.error("This is an error msg.")
# logging.critical("This is an critical msg.")

"""Exampe output

DEBUG:root:This is a debug msg.
INFO:root:This is an info msg.
WARNING:root:This is a warning msg.
ERROR:root:This is an error msg.
CRITICAL:root:This is an critical msg.
"""


import logging

# ====  This function can only be called once. -======= #
# logging.basicConfig(
#     filename="app.log",
#     filemode="w",
#     format="%(name)s - %(levelname)s - %(message)s"
# )


# logging.basicConfig(format="%(asctime)s-%(process)d-%(levelname)s-%(message)s")

# logging.warning("This is a testing warning.")

# try:
#     a = 1 / 0

# except Exception as e:
#     # logging will not break program
#     logging.error("Exception occurred.", exc_info=True)
#     # logging.exception("Exception occurred.")

# logging.warning("Next MSG")





# logger = logging.getLogger("Example Logger")
# logger.warning("THis is a warning.")

"""
Again, unlike the root logger, a custom logger can’t be configured using basicConfig(). You have to configure it using Handlers and Formatters:
"""


logger = logging.getLogger(__name__)

# handle
c_h = logging.StreamHandler()
f_h = logging.FileHandler("file_h.app")




c_h.setLevel(logging.INFO)
f_h.setLevel(logging.DEBUG)

# format
c_f = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
f_f = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
c_h.setFormatter(c_f)
f_h.setFormatter(f_f)

logger.addHandler(c_h)
logger.addHandler(f_h)

logger.warning("This is a warning")
logger.error("This is an error.")






