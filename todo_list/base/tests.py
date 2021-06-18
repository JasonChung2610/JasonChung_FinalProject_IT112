from django.test import TestCase
from django.contrib.auth.models import User
from .models import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, CustomLoginView, RegisterPage
import datetime
from .forms import MeetingForm
from django.urls import reverse_lazy, reverse

# Create your tests here.

class Task(TestCase):
    def setUp(self):
        self.user=User(username='jason')
        self.Task=Task(title='Pay Bill', description="$1000", description="")

    def test_typestring(self):
        self.assertEqual(str(self.tittle), 'Pay Bill')

    def test_tablename(self):
        self.assertEqual(str(Task._meta.db_table), 'complete')
    
    def BooleanField(self):
        self.assertFTrue(complete)


class New_Resource_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='jason', password='@Soxsox123')
        self.task=Task.objects.create(title='Pay Bill', description="$1000", description="")

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('login'))
        self.assertRedirects(response, '/base/login/')