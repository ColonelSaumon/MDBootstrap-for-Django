#################################################
#   mdbDjango/utils/navigation.py
#   =============================
#   AUTHOR : Godefroy Borduas
#   EMAIL : pro@godefroyborduas.ca
#   DATE : 30 avril 2019
#   LICENCE : MIT
#################################################
from enum import Enum
#################################################
#   ENUMERATION
#################################################
class ALIGN(Enum) :
    LEFT = 1
    CENTER = 2
    RIGHT = 3

class NAV_TYPE(Enum) :
    TEXT = 1
    ICON = 2
    TEXT_ICON = 3

class ICON(Enum) :
    SOLID = 1
    BRANDS = 2

    def __str__(self) :
        if self.value is 1 :
            return "fas"
        else :
            return "fab"

#################################################
#   NAVIGATION
#################################################
class Navigation() :
    ''' Cette classe générique permet de décrire la base de fonctionnement
    des classes de navigation. Cette classe n'est pas à être utilisée
    directement. '''
    _navTitle = ""
    _homeLink = "#"
    _navElements = []

    def __init__(self, title, link) :
        self._navTitle = title
        self._homeLink = link

    def AddElement(self, element) :
        ''' Permet d'ajouter un élément de navigation de type
        "NavElement" au menu de navigation. '''
        self._navElements.append(element)

    def GetElementsList(self) :
        return self._navElements

class Nav1Colums(Navigation) :
    ''' Cette contient l'ensemble des éléments nécessaires à l'affichage
    du menu de navigation à deux colonnes. Il ne gère pas le type d'affichage (fixe,
    couleur, etc.), mais simplement les éléments contenus. Le menu généré est à
    une colonne. '''
    _align = ALIGN.LEFT

    def __init__(self, title, link, align = ALIGN.LEFT) :
        self._align = align
        Navigation.__init__(self, title, link)

class Nav2Colums(Navigation) :
    '''Cette contient l'ensemble des éléments nécessaires à l'affichage
    du menu de navigation à deux colonnes. Il ne gère pas le type d'affichage (fixe,
    couleur, etc.), mais simplement les éléments contenus. Le menu généré est à
    deux colonnes (gauche et droite).'''
    _rightElement = []

    def __init__(self, title, link) :
        Navigation.__init__(self, title, link)

    def AddElement(self, element, atLeft = True) :
        if atLeft :
            self._navElements.append(element)
        else :
            self._rightElement.append(element)

    def GetElementsList(self) :
        ''' Retourne la liste gauche et la liste droite. '''
        return self._navElements, self._rightElement

#################################################
#   ELEMENTS OF NAVIGATION
#################################################
class NavElement() :
    '''Cette classe représente un élément simple des menus de navigation.
    Il contient un ID, un texte et un url.'''
    _text = ""
    _id = None
    _url = "#"

    def __init__(self, text, url, id = None) :
        self._text = text
        self._id = id
        self._url = url

    def ShowHTML(self, idActive) :
        active = ''
        if self._id is idActive :
            active = ' active'
        
        html = '<li class="nav-item{}">\n'.format(active)
        html += '\t<a class="nav-link" id="{}" href="{}">\n'.format(self._id, self._url)
        html += '\t\t{}\n\t</a>\n</li>\n'.format(self._text)
        
        return html

class TextElement(NavElement) :
    pass

class TextIconElement(NavElement) :
    _icon = ""
    _type = ICON.SOLID

    def __init__(self, text, icon, url, iconType = ICON.SOLID, id = None) :
        self._icon = icon
        self._type = iconType
        NavElement.__init__(self, text, url, id)

    def ShowHTML(self, idActive) :
        active = ''
        if self._id is idActive :
            active = ' active'
        
        html = '<li class="nav-item{}">\n'.format(active)
        html += '\t<a class="nav-link" id="{}" href="{}">'.format(self._id, self._url)
        html += '<i class="{} fa-{}>{}</i></a>\n</li>\n'.format(self._type, self._icon, self._text)
        
        return html

class IconElement(TextIconElement) :
    def __init__(self, icon, url, iconType = ICON.SOLID, id = None) :
        TextIconElement.__init__(self, "", icon, url, iconType, id)