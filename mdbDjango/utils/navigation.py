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

class Nav2Colums(Navigation) :
    '''Cette contient l'ensemble des éléments nécessaires à l'affichage
    du menu de navigation à deux colonnes. Il ne gère pas le type d'affichage (fixe,
    couleur, etc.), mais simplement les éléments contenus. Le menu généré est à
    deux colonnes (gauche et droite).'''
    _rightElement = []

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

    def ShowHTML(self, idActive) :
        active = ''
        if self._id is idActive :
            active = ' active'
        
        html = '<li class="nav-item{}">\n'.format(active)
        html += '\t<a class="nav-link" id="{}" href="{}">\n'.format(self._id, self._url)
        html += '\t\t{}\n\t</a>\n</li>\n'.format(self._text)
        
        return html