# all workflows

import os


def get_workflow(workflow) -> str:
    """
    Returns the github workflow file for the given language.
    """
    if workflow in ["c", "cpp"]:
        workflow = 'c-cpp'

    path = os.path.join(os.path.dirname(__file__),
                        'workflows', workflow + ".yml")

    if not os.path.exists(path):
        return ""

    with open(path, 'r', encoding="utf-8") as f:
        return f.read()
