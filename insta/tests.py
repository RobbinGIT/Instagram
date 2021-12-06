from django.test import TestCase
from . models import Image,Comment
from django.contrib.auth.models import User

class TestImages(TestCase):
  '''
  Class where we write our image models tests
  '''
  def setUp(self):
    '''
    function that runs before others
    '''
    self.test_user = User(username = 'Githimbo')
    self.test_user.save()
    self.image = Image(image = 'Githimbo.jpeg',name = 'Githimbo',caption = 'Githimbo',user = self.test_user)
    self.comments = Comment(comment = 'awesome',image = self.image,user = self.test_user)

  def test_instance(self):
    self.assertTrue(isinstance(self.image,Image))

  def test_save_image(self):
    self.image.save_image()
    image = Image.objects.all()
    self.assertTrue(len(image)>0)

def test_delete_image(self):
    self.image2 = Image(image = 'mwangi.jpeg',name = 'mwangi',caption = 'mwangi',user = self.test_user)
    self.image2.save_image()
    self.image.save_image()
    self.image.delete_post()
    images = Image.objects.all()
    self.assertEqual(len(images),1) 