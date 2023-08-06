from . import statics

class _RetainTransformation(dict):
    def __init__(self, function, args=None, kwargs=None, func_name=None):
        self['function'] = function
        self['args'] = args
        self['kwargs'] = kwargs
        self['func_name'] = func_name


def _check_same_func(func, kwargs, ignored_functions:list, ignored_kwargs:dict={'_apply_func': ['new_column']}):
    # this is so we get the indexes of the functions we are interested in
    indexes = [i for i, item in enumerate(ignored_functions) if item['function'] == func.__name__]

    for index in indexes:
        for k, v in kwargs.items():
            # data is a reserved word in args so we ignore that argument
            if k in statics.RESERVED_KEYWORDS:
                continue
            # if the kwargs argument exists, get the specific values
            if k == 'kwargs':
                for k2, v2 in kwargs[k].items():
                    cv = ignored_functions[index]['kwargs'].get(k2)
                    if cv != v2:
                        return False
            else:
                # if the key doesnt exist and it is one of the ignored ones, skip
                if k not in ignored_functions[index]['kwargs'] and k in ignored_kwargs[func.__name__]:
                    continue

                cv = ignored_functions[index]['kwargs'].get(k)
                if cv != v:
                    return False
    return True


def _validate_kwargs_reserved_words(kwargs):
    """ensure the kwargs do not contain the resevred keywords"""
    if kwargs:
        for k in statics.RESERVED_KEYWORDS:
            if k in kwargs:
                raise KeyError(f'The keyword argument "{k}" cannot be used in custom functions as it is a reserved keyword. Please change this name and try again. The reserved keywords are: {statics.RESERVED_KEYWORDS}')