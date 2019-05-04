from checkio_referee import RefereeRank, ENV_NAME



import settings_env
from tests import TESTS


class Referee(RefereeRank):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "checkio"
    FUNCTION_NAMES = {
        "python_3": "checkio",
        "js_node": "nonUniqueElements"
    }
    ENV_COVERCODE = {
        ENV_NAME.PYTHON: '''def cover(func, data):
    return list(func(data))
'''
    }