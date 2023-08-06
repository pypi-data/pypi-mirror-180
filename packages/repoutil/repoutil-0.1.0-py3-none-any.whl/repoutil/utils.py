import subprocess
from datetime import datetime


def get_username() -> str:
    """
    Returns the username of the current user.
    """
    name = "<your name here>"

    try:
        result = subprocess.check_output(
            ["git", "config", "user.name"]).decode("utf-8")
    except Exception:
        return name

    if result.strip() == "":
        return name
    else:
        return result


def get_year() -> str:
    """
    Returns the current year.
    """
    return str(datetime.now().year)
