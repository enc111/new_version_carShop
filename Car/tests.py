from django.core.urlresolvers import reverse
from django.test import TestCase
from Car.models import Car, Comments


class CommentsTest(TestCase):
    def test_add_comment_view(self):
        car = Car.objects.create(car_price=23.00, car_description='the best car', car_color='black', car_mark=)
        data = dict(comments_text='test comment')
        self.client.post(reverse('add_comment', kwargs=dict(car_id=car.id)), data=data)
        comment = Comments.objects.get()
        self.assertEquals(comment.comments_text, 'test comment')
        self.assertEquals(comment.comments_car, car)
