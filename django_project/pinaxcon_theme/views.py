from __future__ import unicode_literals

from django.shortcuts import render, redirect

from account.decorators import login_required

@login_required
def purchased_item(request):
    user = request.user
    return render(request,"shop/purchased_items.html")