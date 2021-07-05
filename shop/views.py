from django.shortcuts import render


def shop(request):
    """
    render the shop page
    """
    return render(request, 'shop/shop.html')


