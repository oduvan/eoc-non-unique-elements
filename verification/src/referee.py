from checkio_referee import RefereeRank


import settings_env
from tests import TESTS


class Referee(RefereeRank):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "checkio"
    FUNCTION_NAMES = {
        "python_3": "non_unique_elements",
        "js_node": "nonUniqueElements"
    }