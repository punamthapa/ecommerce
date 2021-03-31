from django.shortcuts import render
from django.views.generic.base import View
from .models import *

# Create your views here.
class BaseView(View):
    views = {}

class HomeView(BaseView):
    def get(self, request):
        self.views['categories'] = Category.objects.filter(status='active')
        self.views['slider'] = Slider.objects.filter(status='active')
        self.views['ads'] = Ad.objects.all()
        self.views['hots'] = Item.objects.filter(label='hot')
        self.views['new'] = Item.objects.filter(label='new')
        self.views['sale'] = Item.objects.filter(label='sale')
        self.views['default'] = Item.objects.filter(label='')

        self.views['brands'] = Brand.objects.filter(status='active')
        self.views['items'] = Item.objects.filter(status='active')

        return render(request, 'index.html', self.views)


class ItemDetailView(BaseView):
    def get(self, request, slug):
        self.views['item_detaill']= Item.objects.filter(slug = slug)

        cat = Item.objects.get(slug = slug).category_id
        self.views['catitems'] = Item.objects.filter(category=cat)
        return render(request, 'product-detail.html',self.views)