from django.shortcuts import render
from django.urls import reverse
from mdbDjango.utils.navigation import Nav2Colums, TextElement, IconElement, ICON

# Create your views here.
def home(request) :
    navigation = Nav2Colums('mdbDjango Sample Page', 'longueuildesign.ca')
    
    navigation.AddElement(TextElement("Home", "#", "home"), atLeft=True)
    navigation.AddElement(TextElement("Page 1", "#", "page1"), atLeft=True)
    navigation.AddElement(TextElement("Page 2", "#", "page2"), atLeft=True)
    navigation.AddElement(TextElement("Page 2", "#", "page2"), atLeft=True)

    navigation.AddElement(IconElement("faceboor-f", "facebook.com", ICON.BRANDS), atLeft=False)
    navigation.AddElement(IconElement("twitter", "twitter.com", ICON.BRANDS), atLeft=False)
    navigation.AddElement(IconElement("instagram", "instagram.com", ICON.BRANDS), atLeft=False)

    return render(request, 'sample/home.html', {
        'nav' : navigation,
        'idactive' : 'home'
    })