from django import template
from django.utils.safestring import mark_safe
from django.utils.html import format_html

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