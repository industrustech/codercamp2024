from django.shortcuts import render, get_object_or_404
from .models import Product, Order

# View for product catalog
def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

# View for product details
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})

# View for handling customer orders (simplified)
def place_order(request, pk):
    product = get_object_or_404(Product, pk=pk)
    order = Order(customer=request.user.customer, product=product, quantity=1)
    order.save()
    return render(request, 'shop/order_confirmation.html', {'order': order})
