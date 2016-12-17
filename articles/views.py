from django.template import loader, Context
from django.http import Http404, HttpRequest
from django.db.models import Q

# Create your views here.

from django.shortcuts import render_to_response
from articles.models import Article, Excursions, Image, Gallery, Map

def main(request):
	content = Article.objects.filter(id=1)
	excursions = Excursions.objects.filter(main=True).order_by("-id")[0:5]
	map = Map.objects.all()
	return render_to_response('main.html',
    	{'excursions':excursions,
    	'text':content,
    	'map':map}
    )

def excursions(request):
	excursions = Excursions.objects.all()
	return render_to_response('excursions.html',
    	{'excursions':excursions}
    )

def one_excursion(request, offset):
	excursion = Excursions.objects.filter(id=offset)
	images = Image.objects.filter(title_id=offset)
	return render_to_response('base.html',
    	{'article':excursion,
    	'images':images}
    )

def tasting(request):
	text = Article.objects.filter(id=2)
	return render_to_response('base.html',
    	{'article':text}
    )

def contacts(request):
	text = Article.objects.filter(id=3)
	return render_to_response('base.html',
    	{'article':text}
    )

def live(request):
	gallery = Gallery.objects.all()
	return render_to_response('live.html',
    	{'gallery':gallery}
    )