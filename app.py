from personal_finance_behavior_analyzer.utils.logger import logging
from personal_finance_behavior_analyzer.utils.exception import CustomException
import sys

if __name__ == "__main__":
    logging.info("Starting the application...")
    try:
        # Add your application logic here
        pass
    except CustomException as e:
        logging.error(e)
    except Exception as e:
        logging.info("An unexpected error occurred: %s", e)
        raise CustomException(e, sys)
    logging.info("Application finished.")