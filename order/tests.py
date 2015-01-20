from django.test import TestCase
from django.contrib.auth.models import User
from Car.models import Car, Model_, Mark, Dealer
from order.models import Order
from datetime import date, datetime
# Create your tests here.


class OrderTest(TestCase):
    def test_order_confirm(self):
        user1 = User.objects.create(
            username='ooo',
            password='999',
            email='r@mail.ru',
            first_name='ff',
            last_name='ll'
        )
        mark1 = Mark.objects.create(name='mark11')
        model = Model_.objects.create(name='model11', mark=mark1)
        dealer = Dealer.objects.create(address='address', country='country1')
        car = Car.objects.create(
            price=23.00,
            description='the best car',
            color='black',
            mark=mark1,
            model=model,
            dealer=dealer,
            man_year=1990,
            complectation=Car.COMPLECTATION_BASE,
            car_img='win.png'
        )
        order1 = Order.objects.create(
            user=user1,
            vehicle=car,
            date_created=datetime(2014, 11, 12).date(),
            date_completed=date(2014, 11, 12),
            status=Order.STATUS_ACCEPTED,
            )
        order1.confirm()
        self.assertEqual(order1.status, Order.STATUS_CONFIRMED)



