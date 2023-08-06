# all licenses

import os
from repoutil.utils import get_username, get_year


def get_license(license) -> str:
    """
    Returns the License file content.
    """
    path = os.path.join(os.path.dirname(__file__),
                        'licenses', license.upper() + '.txt')

    if not os.path.exists(path):
        return ""

    with open(path, 'r', encoding="utf-8") as f:
        return f.read().replace(":NAME:", get_username()).replace(":YEAR:", get_year())
