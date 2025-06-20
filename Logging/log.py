import logging

# log is short a like print 
logging.basicConfig(
  filename="app.log" ,
  level=logging.ERROR ,
  format= "%(asctime)s - %(levelname)s - %(message)s"
  )


logging.info("this is an info message")
logging.debug("This is a debug message")
logging.critical("This is a critical message")
logging.warning("This is a warning message")
logging.error("This is error message")