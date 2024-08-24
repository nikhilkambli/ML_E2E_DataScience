import logging
import os
import sys
from datetime import datetime
from src.exception import * 

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path=os.path.join(os.getcwd(),'logs',LOG_FILE)
os.makedirs(log_path,exist_ok=True)
#exist _ok --even there is file keep an upending

LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)
print("pATH IS "+LOG_FILE_PATH)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

    