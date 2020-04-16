def attr_list_from(attr_str):
    # split on '.' and remove
    # empty strings from resulting list.
    #
    # e.g.
    #           '' => []
    #        'ui' => ['ui']
    # 'ui.widget' => ['ui', 'widget']
    attr_list = attr_str.split('.')
    return list(filter(None, attr_list))


def deep_getattr(start_obj, attr_str):
    attr_list     = attr_list_from(attr_str)

    current_value = start_obj
    for attr_name in attr_list:
        current_value = getattr(current_value, attr_name)
    return current_value


def deep_setattr(start_obj, attr_str, value):
    attr_list = attr_list_from(attr_str)
    obj       = deep_getattr(start_obj, attr_list[:-1])
    setattr(obj, attr_list[-1], value)


# expose an attribute
def expose(attr_str, get_only=False):
    # create getter
    def get(self):
        return deep_getattr(self, attr_str)

    # get only property?
    if get_only:
        return property(get)

    # create setter
    def set(self, value):
        deep_setattr(self, attr_str, value)

    # return property
    return property(get, set)


def expose_via(get_attr_str, set_attr_str=None):
    # getter
    def get(self):
        bound_method = deep_getattr(self, get_attr_str)
        return bound_method()

    if not set_attr_str:
        return property(get)

    def set(self, value):
        bound_method = deep_getattr(self, set_attr_str)
        bound_method(value)

    return property(get, set)


def setter_for_property(name):
    # e.g. currentIndex => setCurrentIndex
    upper_case_name = name[0].upper() + name[1:]
    return f'set{upper_case_name}'


def property_from_main_window(property_name):
    get_attr_str = property_name
    set_attr_str = setter_for_property(property_name)
    return expose_via(get_attr_str, set_attr_str)


def property_from_widget(widget_name, property_name):
    get_attr_str = f'ui.{widget_name}.{property_name}'
    set_attr_str = f'ui.{widget_name}.{setter_for_property(property_name)}'
    return expose_via(get_attr_str, set_attr_str)


def read_only_from_widget(widget_name, attr_str):
    attr_str = f'ui.{widget_name}.{attr_str}'
    return expose(attr_str, get_only=True)


def signal_from_widget(widget_name, signal_name):
    get_attr_str = f'ui.{widget_name}'
    return expose(get_attr_str, get_only=True)
