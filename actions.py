from datetime import datetime

from robocorp.actions import action


@action
def get_current_date() -> str:
    """
    Returns the current date in ISO format.
    """
    return datetime.now().isoformat()
