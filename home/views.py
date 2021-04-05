from django.shortcuts import render
from django.views.generic.base import View
from .models import *
# Create your views here.
class BaseView(View):
    views = {}
class HomeView(BaseView):
    def get(self,request):
        self.views['categories'] = Category.objects.filter(status='active')
        self.views['sliders'] = Slider.objects.filter(status='active')
        self.views['brands'] = Brand.objects.filter(status='active')
        self.views['ads1'] = Ad.objects.all()
        self.views['hots'] = Item.objects.filter(label='hot')
        self.views['news'] = Item.objects.filter(label='new')
        self.views['sales'] = Item.objects.filter(label='sale')
        self.views['defaults'] = Item.objects.filter(label='')

        return render(request,'index.html',self.views)
class ItemDetailView(BaseView):
    def get(self,request,slug):
        self.views['item_detail'] = Item.objects.filter(slug=slug)
        self.views['brand'] = Brand.objects.filter(status= 'active')
        self.views['count'] = []
        for i in self.views['brand']:
            count_food = Item.objects.filter(brand=i.id).count()
            print(i.name,count_food)
            d = {'name':i.name,'count':count_food}
            self.views['count'].append(d)
            print(d)

        self.views['count_cat'] = Category.objects.filter(status= 'active')
        self.views['cat_count'] = []
        for i in self.views['count_cat']:
            count_food = Item.objects.filter(category=i.id).count()
            print(i.name,count_food)
            d = {'name':i.name,'image':i.image,'cat_count':count_food}
            self.views['cat_count'].append(d)
            print(d)

        cat = Item.objects.get(slug = slug).category_id
        self.views['catitems'] = Item.objects.filter(category=cat)
        return render(request,'product-detail.html',self.views)
class CategoryView(BaseView):
    def get(self,request,slug):
        cat_id = Category.objects.get(slug = slug).id
        self.views['catdetail'] = Item.objects.filter(slug = slug)
        return render(request, 'product-list.html', self.views)



class SearchView(BaseView):
    def get(self,request):
        # query = request.GET.get('search',None)
        if request.method == 'GET':
            query = request.GET['search']
            self.views['search_product'] = Item.objects.filter(title__icontains=query)
            return render(request,'search.html',self.views)
        return render(request,'search.html')