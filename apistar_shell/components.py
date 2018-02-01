from IPython import embed

from apistar import Settings, Component

from .utils import import_module, import_class


class ShellBackend(object):

    def __init__(self, settings: Settings) -> None:
        config = settings.get('APISTAR_SHELL', {})
        self.imports = config.get('PRE_IMPORTS', [])
        self.custom_function = config.get('CUSTOM_FUNCTION')
        self.header = config.get('HEADER', 'Shell')
    
    def get_custom_imports(self):
        module = import_module(self.custom_function['module'])
        function = import_class(module, self.custom_function['function'])
        return function()

    def get_namespace(self):
        namespace = {}
        for item in self.imports:
            module_name = item.get('module')
            module = import_module(item.get('module'))
            imports = item.get('imports')

            if not imports:
                namespace[module_name] = module
            else:
                for klass in imports:
                    namespace[klass] = import_class(module, klass)

        if self.custom_function:
            namespace.update(self.get_custom_imports())

        return namespace


components = [
    Component(ShellBackend),
]
