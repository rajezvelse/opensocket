async def check_authentication(sid, token):
    """
        Auth validation goes here
    """

    if token is None:
        raise PermissionError('Authentication failed')
    return True
