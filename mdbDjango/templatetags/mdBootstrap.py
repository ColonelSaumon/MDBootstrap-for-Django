#################################################
#   mdbDjango/templatetags/mdBootstrap.py
#   =============================
#   AUTHOR : Godefroy Borduas
#   EMAIL : pro@godefroyborduas.ca
#   DATE : 12 avril 2019
#   LICENCE : MIT
#################################################
from django import template
from django.utils.safestring import mark_safe
from django.utils.html import format_html
# MBDjango import
from mdbDjango.utils.navigation import Nav1Colums

# Enregistrement des tags de l'application
register = template.Library()

#################################################
#   HTML HEADER SECTION
#################################################
@register.simple_tag()
def LoadCSS(bootVersion = '4.3.1', mdbVersion = '4.7.7') :
    ''' Permet de générer les liens d'inclusion CSS pour MDBootstrap 4.7.7 et Bootstrap 4.3.1 ou la version spécifier'''
    # CSS Bootstrap
    link = 'https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/{}/css/bootstrap.min.css'.format(bootVersion)
    source = '<link href="{}" rel="stylesheet">\n'.format(link)
    # CSS MDBootstrap
    link = 'https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/{}/css/mdb.min.css'.format(mdbVersion)
    source += '<link href="{}" rel="stylesheet">'.format(link)

    return format_html(source)

@register.simple_tag()
def LoadJS(jquery = '3.3.1', bootTooltips = '1.14.4', bootVersion = '4.3.1', mdbVersion = '4.7.7') :
    ''' Permet de générer les liens d'inclusion JavaScript pour MDBootstrap 4.7.7, Bootstrap 4.3.1 et JQuery 3.3.1 ou la version spécifier'''
    # JS JQuery
    link = 'https://cdnjs.cloudflare.com/ajax/libs/jquery/{}/jquery.min.js'.format(jquery)
    source = '<script type="text/javascript" src="{}"></script>\n'.format(link)
    # JS Bootstrap Tooltips
    link = 'https://cdnjs.cloudflare.com/ajax/libs/popper.js/{}/umd/popper.min.js'.format(jquery)
    source += '<script type="text/javascript" src="{}"></script>\n'.format(link)
    # JS Bootstrap
    link = 'https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/{}/js/bootstrap.min.js'.format(bootVersion)
    source += '<link href="{}" rel="stylesheet">\n'.format(link)
    # JS MDBootstrap
    link = 'https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/{}/js/mdb.min.js'.format(mdbVersion)
    source += '<link href="{}" rel="stylesheet">'.format(link)

    return format_html(source)

@register.simple_tag
def LoadFontAwesome(faVersion = '5.8.1') :
    ''' Permet de générer les liens d'inclusion CSS pour Font Awesome 5.8.1 ou la version spécifier'''
    link = 'https://use.fontawesome.com/releases/v{}/css/all.css'.format(faVersion)
    source = '<link rel="stylesheet" href="{}">\n'.format(link)

    return format_html(source)

#################################################
#   FONT AWESOME
#################################################
@register.simple_tag
def SolidIcon(iconName, fontSize = "3em", color = "black") :
    ''' Retourne l'icone "Font Awesome" demandé dans sa version Solid. '''
    return format_html('<span style="font-size: {}; color: {};"><i class="fas fa-{}"></i></span>'.format(
        fontSize, color, iconName))

@register.simple_tag
def BrandsIcon(iconName, fontSize = "3em", color = "black") :
    ''' Retourne l'icone "Font Awesome" demandé dans sa version Solid. '''
    return format_html('<span style="font-size: {}; color: {};"><i class="fab fa-{}"></i></span>'.format(
        fontSize, color, iconName))

#################################################
#   NAVIGATIONS
#################################################
@register.inclusion_tag('navigation.html')
def Nav(navigation, color, activeLink = None) :
    ''' Permet d'afficher un menu avec les informations prévus dans
    l'objet navigation. Les couleurs réfèrent à https://mdbootstrap.com/docs/jquery/css/demo/#colors '''
    col1, col2 = None, None
    is1Col = isinstance(navigation, Nav1Colums)
    if not is1Col :
        col1, col2 = navigation.GetElementsList()
    else :
        col1 = navigation.GetElementList()
        col2 = navigation._align
        
    return {'is1Col' : is1Col,
            'color' : color,
            'title' : navigation._navTile,
            'link' : navigation._homeLink,
            'col1' : col1,
            'col2' : col2,
            'idActiveLink' : activeLink}

