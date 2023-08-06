# all language gitignores

import os


def get_gitignore(language) -> str:
    """
    Returns the language specific gitignore.
    """
    path = os.path.join(os.path.dirname(__file__),
                        'gitignores', language + '.gitignore')

    if not os.path.exists(path):
        return ""

    with open(path, 'r') as f:
        return f.read()
