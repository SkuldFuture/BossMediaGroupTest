import logging
from pygelf import GelfTcpHandler
from uuid import uuid4


class CustomFormatter(logging.Formatter):
    COLORS = [
        '\033[31m',
        '\033[32m',
        '\033[33m',
        '\033[34m',
        '\033[35m',
        '\033[36m',
        '\033[37m',
    ]
    COLOR_MAP = {}

    def format(self, record):
        log_message = super().format(record)
        func_name = record.funcName
        class_name = record.__dict__.get('class_name', None)

        if class_name:
            func_name = f"{class_name}.{func_name}"

        if func_name not in self.COLOR_MAP:
            self.COLOR_MAP[func_name] = self.COLORS[
                len(self.COLOR_MAP) % len(self.COLORS)
            ]

        color = self.COLOR_MAP[func_name]
        return f"{color}{log_message}\033[0m"


class ContextFilter(logging.Filter):
    def filter(self, record):
        record.request_id = str(uuid4())
        return True


logger = logging.getLogger(__name__)

handler = logging.StreamHandler()

formatter = CustomFormatter('%(asctime)s [%(levelname)s] [%(funcName)s] %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)
logger.addHandler(
    GelfTcpHandler(host='81.94.159.8', port=12201, include_extra_fields=True)
)
logger.addFilter(ContextFilter())
logger.setLevel(logging.DEBUG)


class TestClass:
    def test_method(self):
        logger.debug(
            'Тест logger: TestClass.test_method', extra={'class_name': 'TestClass'}
        )


def another_function():
    logger.debug('Тест logger: another_function')


test_instance = TestClass()
test_instance.test_method()
another_function()
