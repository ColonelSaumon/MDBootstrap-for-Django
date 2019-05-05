#################################################
#   mdbDjango/navigation/fields.py
#   =============================
#   AUTHOR : Godefroy Borduas
#   EMAIL : pro@godefroyborduas.ca
#   DATE : 5 mai 2019
#   LICENCE : MIT
#################################################
import copy

from mdbDjango.navigation.widgets import Widget
from mdbDjango.navigation.widgets import (
    Input, BrandInput, TextInput, LinkInput,
    IconInput
)

__all__ = ('Fields', 'BrandField', 'LinkField',
          'IconField', 'DropdownField', 'TextField')

#################################################
#   BASE CLASS
#################################################
class Field :
    widget = Input
    
    def __init__(self, label, url = '#', is_disabled = False,
                widget = None) :
        self.label = label
        self.url = url
        self.is_disabled = is_disabled
        widget = widget or self.widget
        if isinstance(widget, type) :
            widget = widget()
        else :
            widget = copy.deepcopy(widget)

        extra_attrs = self.widget_attrs(widget)
        if extra_attrs :
            widget.attrs.update(extra_attrs)

    def widget_attrs(self, widget) :
        return {'url' : self.url,
                'is_isabled' : self.is_disabled,
                'label' : self.label }

class BrandField(Field) :
    def __init__(self, label, url = '#',
                is_disabled = False) :
        super().__init__(self, label, url,
                        False,
                        widget=BrandInput)

class LinkField(Field) :
    def __init__(self, label, url = '#',
                is_disabled = False) :
        super().__init__(self, label, url,
                        is_disabled,
                        widget=LinkInput)

class IconField(Field) :
    def __init__(self, label, url = '#',
                is_disabled = False) :
        super().__init__(self, label, url,
                        is_disabled,
                        widget=IconInput)

class DropdownField(Field) :
    def __init__(self, label, elementsFieldList = [], url = '#',
                is_disabled = False) :
        self.elementsFieldList = elementsFieldList
        super().__init__(self, label, url,
                        is_disabled,
                        widget=IconInput)

    def widget_attrs(self, widget) :
        attrs = super().widget_attrs(widget)
        if not self.elementsFieldList :
            attrs['elements'] = self.elementsFieldList

        return attrs

class TextField(Field) :
    def __init__(self, label, url = '#',
                is_disabled = False) :
        super().__init__(self, label, url,
                        is_disabled,
                        widget=TextInput)