#################################################
#   mdbDjango/navigation/navigation.py
#   =============================
#   AUTHOR : Godefroy Borduas
#   EMAIL : pro@godefroyborduas.ca
#   DATE : 30 avril 2019
#   LICENCE : MIT
#################################################
import copy

from django.utils.html import html_safe

__all__ = ()

#################################################
#   METACLASS
#################################################
class DeclarativeFieldsMetaClass(type) :
    """Collect Fields declared on the base classes."""
    def __new__(mcs, name, bases, attrs):
        current_fields = []
        for key, value in list(attrs.items()):
            if isinstance(value, Field):
                current_fields.append((key, value))
                attrs.pop(key)
        attrs['declared_fields'] = dict(current_fields)

        new_class = super(DeclarativeFieldsMetaclass, mcs).__new__(mcs, name, bases, attrs)

        declared_fields = {}
        for base in reversed(new_class.__mro__):
            if hasattr(base, 'declared_fields'):
                declared_fields.update(base.declared_fields)

           for attr, value in base.__dict__.items():
                if value is None and attr in declared_fields:
                    declared_fields.pop(attr)

        new_class.base_fields = declared_fields
        new_class.declared_fields = declared_fields

        return new_class

@html_safe
class BaseNavigation:
    pass