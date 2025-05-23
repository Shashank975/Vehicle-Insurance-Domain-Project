# from src.logger import logging

# logging.debug("This is for the test2")
import sys
from src.logger import logging
from src.exception import MyException  # ✅ Correct import

try:
    1 / 0
except Exception as e:
    raise MyException(str(e), sys)

