from django.shortcuts import render



def main(request):
    context = {
        'user_list': [
            {
                'first_name': 'Konstantin',
                'last_name': 'Uskov',
                'age': 31
            },
            {
                'first_name': 'konstantin1',
                'last_name': 'uskov1',
                'age': 311
            },
            {
                'first_name': 'Konstantin2',
                'last_name': 'Uskov2',
                'age': 312
            }

        ]
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    links_menu = [
        {'href': 'products_all', 'title': 'все'},
        {'href': 'products_home', 'title': 'дом'},
        {'href': 'products_office', 'title': 'офис'},
        {'href': 'products_modern', 'title': 'модерн'},
        {'href': 'products_classic', 'title': 'классика'},
    ]

    context = {
        'links_menu': links_menu

    }
    return render(request, 'mainapp/products.html', context)


def contact(request):
    return render(request, 'mainapp/contact.html')


'''def index(request):
   return render(request, 'mainapp/index.html')'''