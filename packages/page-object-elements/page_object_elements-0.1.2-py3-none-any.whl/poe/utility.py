import inspect


def get_all_methods_and_properties(clazz):
    return [name for name, value in inspect.getmembers(clazz)]


def get_methods_and_properties(clazz, dont=False, starts_with=''):
    if starts_with == '':
        return [name for name, value in inspect.getmembers(clazz)]
    if not dont:
        return [name for name, value in inspect.getmembers(clazz) if name.startswith(starts_with)]
    else:
        return [name for name, value in inspect.getmembers(clazz) if not name.startswith(starts_with)]
