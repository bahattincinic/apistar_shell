import importlib


def import_module(val):
    try:
        return importlib.import_module('.'.join(val.split('.')))
    except ImportError:
        raise ImportError("Could not import '%s'" % val)


def import_class(module, val):
    try:
        return getattr(module, val)
    except AttributeError:
        raise ImportError("Could not import '%s'" % val)
