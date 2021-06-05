from goli.constants import languages, topics


def validate_args(*args) -> bool:
    """ validate user input args """
    for arg in args:
        if arg not in topics or arg not in languages:
            return False
    return True
