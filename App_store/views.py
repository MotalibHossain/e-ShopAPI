from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App_store.models import Product, Category, SubCategory


def Home(request):
    all_category=Category.objects.all()
    sub_category=SubCategory.objects.all()

    for category in all_category:
        for subcat in sub_category:
            if(category == subcat.Subcatagory):
                all_sub_category=SubCategory.objects.filter(Subcatagory=category).all()
                # print("man_sub_category***********",man_sub_category)

    print("category========",all_category)
    all_product=Product.objects.all()

    context={
        "all_category":all_category,
        "all_product":all_product,
        "sub_category":sub_category,
        "all_sub_category":all_sub_category,
    }
    return render(request, "Store/index.html", context)


def ProductDetails(request,slug):
    # show all product informations and catagory product
    all_product = Product.objects.all()
    each_product = Product.objects.get(slug=slug)
    print(each_product)

    catagory = each_product.catagory
    context = {
        "each_product": each_product,
        "all_product": all_product,
    }

    return render(request, "Store/product-detail.html",context)
