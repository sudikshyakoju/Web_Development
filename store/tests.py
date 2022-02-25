from django.test import TestCase

# Create your tests here.
from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from store import views
from store.views import *
# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_case_index_url(self):
        url=reverse('address')
        self.assertEquals(resolve(url).func,detail)

    def test_case_orders_url(self):
        url=reverse('categories')
        self.assertEquals(resolve(url).func,all_categories)

    def test_case_showcart_url(self):
        url=reverse(''accounts/logout/')
        self.assertEquals(resolve(url).func,category_products)

    def test_case_cotton_url(self):
        url=reverse('accounts/register/')
        self.assertEquals(resolve(url).func,RegistrationView)

    def test_case_jeans_url(self):
        url=reverse('accounts/login/')
        self.assertEquals(resolve(url).func,remove_address)

    def test_case_device_url(self):
        url=reverse('accounts/profile/')
        self.assertEquals(resolve(url).func,RegistrationView)

    def test_case_checkout_url(self):
        url=reverse('accounts/add-address/')
        self.assertEquals(resolve(url).func,checkout)

class Testviews(TestCase):
    def test_views_indbhex(self):
        client=Client()
        url=reverse('app:ProductDetailView')
        response=client.post(url)