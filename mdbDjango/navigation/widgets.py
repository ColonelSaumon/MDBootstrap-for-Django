#################################################
#   mdbDjango/navigation/widgets.py
#   =============================
#   AUTHOR : Godefroy Borduas
#   EMAIL : pro@godefroyborduas.ca
#   DATE : 5 mai 2019
#   LICENCE : MIT
#################################################
import copy

from django.forms import widgets

__all__ = ('Input', 'BrandInput', 'LinkInput', 
    'IconInput', 'DropdownInput', 'TextInput')
#################################################
#   Widget
#################################################
class Widget(widgets.Widget) :
    def __init__(self, attrs = None, url = '#') :
        if 'url' is not in attrs :
            attrs = attrs.copy()
            attrs['url'] = url
        super().__init__(attrs)

#################################################
#   INPUT
#################################################
class Input(Widget) :
    """
    Permet de définir l'ensemble des type d'éléments
    dans une barre de navigation.
    """
    input_type = None
    template_name = 'mdbDjango/navigation/widgets/input.html'
    url_context = '#'
    is_disabled = False

    def __init__(self, attrs = None)
        if attrs is not None :
            attrs = attrs.copy()
            self.input_type = attrs.pop('type', self.input_type)
            attrs['is_disabled'] = is_disabled
        super().__init__(attrs)

    def get_context(self, name, value, attrs) :
        context = super().get_context(name, value, attrs)
        context['widget']['type'] = self.input_type
        return context

class BrandInput(Input) :
    input_type = 'brand'
    template_name = 'mdbDjango/navigation/widgets/brand.html'

class LinkInput(Input) :
    input_type = 'link'
    template_name = 'mdbDjango/navigation/widgets/input.html'

class IconInput(Input) :
    input_type = 'icon'
    template_name = 'mdbDjango/navigation/widgets/input.html'

class DropdownInput(Input) :
    input_type = 'dropdown'
    template_name = 'mdbDjango/navigation/widgets/dropdown.html'
    elements = None

    def __init__(self, attrs = None) :
        if attrs is not None :
            attrs = attrs.copy()
            attrs['elements'] = elements
        super().__init__(attrs)

class TextInput(Input) :
    input_type = 'text'
    template_name = 'mdbDjango/navigation/widgets/text.html'