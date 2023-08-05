from injectable import injectable


@injectable
class UtilsClass:
    def get_full_class_name(self, obj):
        module = obj.__class__.__module__
        if module is None or module == str.__class__.__module__:
            return obj.__class__.__name__
        return module + '.' + obj.__class__.__name__
