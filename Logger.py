import logging.config
import logging
import time
import os

# Create logger folder
log_folder = os.path.join(os.getcwd(), "logs")
# check log_folder exist or not
if not os.path.exists(log_folder):
    os.makedirs(log_folder)


##Create a file and setting its format
logdatetime = time.strftime("%Y-%m-%d_%H:%M:%S")

# ##Create a new log file each time and file name added current time
logging.basicConfig(level=logging.DEBUG, filename=os.path.join(log_folder, f"task_"+ logdatetime + ".log"), filemode='w', format='%(asctime)s - %(levelname)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

##Print the log on terminal, so use streamhandler, then setting its format
console = logging.StreamHandler()
console.setLevel(logging.INFO)
handler_format = logging.Formatter("%(asctime)s %(levelname)s: Line %(lineno)d: %(message)s")
console.setFormatter(handler_format)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(console)