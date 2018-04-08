from django.test.utils import setup_test_environment
from django.test import TestCase
from django.test import Client
from django.urls import reverse
from datetime import datetime

# Create your tests here.

client = Client() 
class FibonacciViewTests(TestCase):
    def input_zero(self):
        '''
            For input 0 should return 0 
        '''
        response = self.client.post(reverse('fibonacci:resp'), {'num': 0})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(int(response.context['res']), 0)

    def corret_value(self):
        '''
            This TestCase to ensure generated fibonacci value is correct for given number.
        '''
        response = self.client.post(reverse('fibonacci:resp'), {'num': 6})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(int(response.context['res']), 8)
    
    def incorret_value(self):
        '''
            This TestCase to ensure generated fibonacci value is incorrect for given number.
        '''
        response = self.client.post(reverse('fibonacci:resp'), {'num': 6})
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(int(response.context['res']), 3)

    def duration(self):
        '''
            This test case to ensure that query time is less than process time.
        '''
        response = self.client.post(reverse('fibonacci:resp'), {'num': 6})
        self.assertEqual(response.status_code, 200)
        time = response.context['time'].total_seconds()
        response1 = self.client.post(reverse('fibonacci:resp'), {'num': 6})
        time1 = response1.context['time'].total_seconds()
        self.assertLess(time1, time)
