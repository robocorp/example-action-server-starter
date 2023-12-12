from robocorp.actions import action


@action
def get_birth_date(first_name: str):
    """Returns the borth date of a person.

    Keyword arguments:
    first_name -- First name of the person
    """
    return "1986"
