import logging

def test_generating_logger():
    logging.basicConfig(
        filename="/Users/harshal/PycharmProjects/PythonProject/PytestPython/Utilities/logfile.log",
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG,  # include debug
        force=True            # ensure reset
    )
    logger = logging.getLogger()
    return logger

logs = test_generating_logger()


logs.info("This is our first log")
logs.error("This is our error")
logs.debug("My debug")
