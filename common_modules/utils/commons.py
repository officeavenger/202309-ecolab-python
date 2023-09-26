

def members(obj):
    return [member for member in dir(obj) if not member.startswith('__')]