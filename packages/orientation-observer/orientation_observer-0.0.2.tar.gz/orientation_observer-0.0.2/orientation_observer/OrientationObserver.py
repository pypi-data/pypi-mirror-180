# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class OrientationObserver(Component):
    """An OrientationObserver component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.

Keyword arguments:

- id (string; optional)

- orientation (string; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'orientation_observer'
    _type = 'OrientationObserver'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, orientation=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'orientation']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'orientation']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(OrientationObserver, self).__init__(**args)
