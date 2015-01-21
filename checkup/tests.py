from django.test import TestCase
from checkup.models import Checkup, TypeOfService
from django.contrib.auth.models import User
from Car.models import Car, Model_, Mark, Dealer
from datetime import date, datetime
# Create your tests here.


class CheckupTest(TestCase):
    def test_checkup_make(self):
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
        user1 = User.objects.create(
            username='ooo',
            password='999',
            email='r@mail.ru',
            first_name='ff',
            last_name='ll'
        )
        type_of_service1 = TypeOfService.objects.create(name='checkup', price=23.66)
        checkup1 = Checkup.objects.create(
            date_created=datetime(2014, 11, 12).date(),
            date_completed=date(2014, 11, 12),
            reg_number='e567oo',
            run=956,
            car_man_year=car,
            user=user1,
            type_of_service=type_of_service1
        )

        self.assertEqual(checkup1.price, type_of_service1.price)





    """date_created = models.DateTimeField(default=timezone.now)
    date_completed = models.DateField(null=True, blank=True)
    reg_number = models.CharField(max_length=15)
    run = models.IntegerField()
    car_man_year = models.ForeignKey(Car.man_year)
    user = models.ForeignKey(User)
    type_of_service = models.ForeignKey(TypeOfService)"""