from django.core.urlresolvers import reverse
from django.test import TestCase
from Car.models import Car, Comments, Mark


class CommentsTest(TestCase):
    def test_add_comment_view(self):
        mark = Mark.objects.create(name='mark1')
        car = Car.objects.create(price=23.00, description='the best car', color='black', mark=mark)
        data = dict(comments_text='test comment')
        self.client.post(reverse('add_comment', kwargs=dict(car_id=car.id)), data=data)
        comment = Comments.objects.get()
        self.assertEquals(comment.comments_text, 'test comment')
        self.assertEquals(comment.comments_car, car)
#и с ошибками что неправильно ввели