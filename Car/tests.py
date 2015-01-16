from django.core.urlresolvers import reverse
from django.test import TestCase
from Car.models import Car, Comments, Model_, Mark, Dealer


class CommentsTest(TestCase):
    def test_add_comment_view(self):
        mark1 = Mark.objects.create(name='mark1')
        model = Model_.objects.create(name='model1', mark=mark1)
        dealer = Dealer.objects.create(address='address', country='country1')
        car = Car.objects.create(price=23.00, description='the best car', color='black', mark=mark1, model=model,
                                 dealer=dealer, man_year=1990, complectation=Car.COMPLECTATION_BASE, car_img='D://win.png')
        data = dict(ctext='test comment')
        self.client.post(reverse('add_comment', kwargs=dict(car_id=car.id)), data=data)
        comment = Comments.objects.get()
        self.assertEquals(comment.ctext, 'test comment')
        self.assertEquals(comment.comments_car, car)
#и с ошибками что неправильно ввели