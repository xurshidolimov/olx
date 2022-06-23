from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from pages.models import Product, Category, Likes


# g'alaba
class HomePageView(View):
    def get(self, request):
        products=Product.objects.all().order_by('-id')
        categorys=Category.objects.all()
        search_query=request.GET.get('q', '')
        if search_query:
            products=products.filter(name__icontains=search_query)
        return render(request, "home.html", {"products":products, "search_query":search_query, "categorys": categorys})

# g'alaba
class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'update.html'
    fields = ['name', 'price', 'description', 'category', 'picture', 'adress', 'username', 'email', 'phone_number', 'active']
    success_url = reverse_lazy('my-products')

# g'alaba
class ProductCreateView(CreateView):
    model = Product
    template_name = 'new.html'
    fields = ['name', 'price', 'description', 'category', 'picture', 'adress', 'username', 'email', 'phone_number']
    success_url = reverse_lazy('home')

# g'alaba
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'delete.html'
    success_url = reverse_lazy('my-products')

# g'alaba
class LikedView(View):
    def get(self, request):
        box = Likes.objects.all()
        liked=[]
        for object in box:
            if object.user==request.user:
                liked.append(object.product)
        return render(request, 'liked.html', {"liked":liked})

# g'alaba
class CategoryView(View):
    def get(self, request, category_id):
        productss=Product.objects.all()
        products=[]
        for object in productss:
            if object.category_id==category_id:
                products.append(object)
        return render(request, 'category.html', {"products":products})

# g'alaba
class ProductDetailView(DetailView):
    def get(self, request, product_id):
        product = Product.objects.get(id=product_id)
        product_category=product.category
        productss = Product.objects.all()
        products = []
        for object in productss:
            if object.category == product_category:
                products.append(object)
        return render(request, 'detail.html', {'product':product, "products":products})

# g'alaba
class MyProductsView(View):
    def get(self, request):
        box = Product.objects.all()
        products=[]
        for object in box:
            if object.username==request.user.username:
                products.append(object)
        return render(request, 'my_products.html', {"products":products})

# mag'lubiyat
class AddLikeView(View):
    def get(self, request, id):
        if isinstance(id, Likes):
            pass
        # box=Likes.objects.all()
        # for object in box:
        #     if object.user==request.user.id and object.product==id:
        #         object.delete()
        #         break
        #     else:
        #         Likes.objects.create(user=request.user, product=id)
        # return render(request, 'home.html')

# qisman g'alaba
class ActivView(View):
    def get(self, request, id):
        if Product.objects.get(id=id).active==False:
            name=Product.objects.get(id=id).name
            description=Product.objects.get(id=id).description
            category=Product.objects.get(id=id).category
            picture=Product.objects.get(id=id).picture
            price=Product.objects.get(id=id).price
            adress=Product.objects.get(id=id).adress
            username=Product.objects.get(id=id).username
            email=Product.objects.get(id=id).email
            phone_number=Product.objects.get(id=id).phone_number
            created_at=Product.objects.get(id=id).created_at
            active=True
            Product.objects.get(id=id).delete()
            Product.objects.create(
                name=name,
                description=description,
                category=category,
                picture=picture,
                price=price,
                adress=adress,
                username=username,
                email=email,
                phone_number=phone_number,
                active=active,
                created_at=created_at,
            )
        else:
            name=Product.objects.get(id=id).name
            description=Product.objects.get(id=id).description
            category=Product.objects.get(id=id).category
            picture=Product.objects.get(id=id).picture
            price=Product.objects.get(id=id).price
            adress=Product.objects.get(id=id).adress
            username=Product.objects.get(id=id).username
            email=Product.objects.get(id=id).email
            phone_number=Product.objects.get(id=id).phone_number
            created_at=Product.objects.get(id=id).created_at
            active=False
            Product.objects.get(id=id).delete()
            Product.objects.create(
                name=name,
                description=description,
                category=category,
                picture=picture,
                price=price,
                adress=adress,
                username=username,
                email=email,
                phone_number=phone_number,
                active=active,
                created_at=created_at,
            )
        box = Product.objects.all()
        products = []
        for object in box:
            if object.username == request.user.username:
                products.append(object)
        return render(request, 'my_products.html', {"products": products})