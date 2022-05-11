# from multiprocessing import context
from django.shortcuts import render, redirect
from django.views import View
from customer.models import OrderModel
from django.utils.timezone import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin

# Create your views here.


class Dashboard(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, *args, **kwargs):
        today = datetime.today()
        orders = OrderModel.objects.filter(
            created_on__year=today.year, created_on__month=today.month, created_on__day=today.day)
        total_revenue = 0

        for order in orders:
            total_revenue += order.price

        context = {
            'orders': orders,
            'total_revenue': total_revenue,
            'total_orders': len(orders)
        }

        return render(request, 'restaurant/dashboard.html', context)
    
    def test_func(self):
        return self.request.user.groups.filter(name='Staff').exists()
