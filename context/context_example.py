import contextlib
import logging

logging.getLogger().setLevel(logging.INFO)

class ContextExample:

	def __init__(self):
		self.a = 100
		self.b = 200

	def __enter__(self):
		logging.info("Enter context")

		return self.__class__

	def __exit__(self, exc_type, exc_value, track_back):
		logging.info("Exit context")

@contextlib.contextmanager
def gen_example():
	logging.info("Enter __enter__ method")
	yield "returned by __enter__", None

	logging.info("Enter __exit__ method")



if __name__ == "__main__":
	# with ContextExample() as ce:
	# 	logging.info("Hello world")
	# 	logging.info("ce: {}".format(ce))

	with gen_example() as ex:
		logging.info("gen_example: contextmanger")
		logging.info("EX: {}".format(ex))
