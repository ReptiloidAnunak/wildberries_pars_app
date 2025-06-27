import logging

from wb_pars_api_server.settings import LOGS_API, LOGS_PARSER


def set_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if logger.hasHandlers():
        logger.handlers.clear()

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    class FolderFilter(logging.Filter):
        def __init__(self, folder_names):
            super().__init__()
            self.folder_names = folder_names

        def filter(self, record):
            pathname = record.pathname
            return any(folder_name in pathname for folder_name in self.folder_names)

    api_handler = logging.FileHandler(LOGS_API, mode='w')
    # api_handler.setLevel(logging.DEBUG)
    api_handler.setFormatter(formatter)
    # api_handler.addFilter(FolderFilter(["product"]))

    parser_handler = logging.FileHandler(LOGS_PARSER, mode='w')
    # parser_handler.setLevel(logging.DEBUG)
    parser_handler.setFormatter(formatter)
    parser_handler.addFilter(FolderFilter(["bot_tg_sender"]))

    logger.addHandler(api_handler)
    logger.addHandler(parser_handler)

    return logger



log_api = set_logger("API")
log_parser = set_logger("PARSER")




