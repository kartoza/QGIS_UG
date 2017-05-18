from __future__ import unicode_literals

from django.shortcuts import render, redirect
from cartridge.shop.models import Order,OrderItem

from account.decorators import login_required

@login_required
def purchased_items(request):
    user = request.user
    orders = Order.objects.select_related().all().filter(user_id = user.id)
    return render(request,"shop/purchased_items.html",{
      "orders" : orders
    })