import json

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from wine_reviews.models import Wine


class WineApiTestCase(APITestCase):
    client = APIClient()

    def setUp(self):
        with open('wine_info/fixtures/wines.json') as json_file:
            wines = json.load(json_file)
        wines_object = []
        for wine in wines[:10]:
            fields = wine.pop('fields')
            wines_object.append(Wine(**fields))
        Wine.objects.bulk_create(wines_object)

    def test_get_all(self):
        response = self.client.get('/api/wines/')
        data = dict(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(data['results']), 10)

    def test_country_filter(self):
        response = self.client.get('/api/wines/', {'country': 'France'})
        data = dict(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(data['results']), 2)

    def test_description_filter(self):
        response = self.client.get('/api/wines/', {'description': 'dry'})
        data = dict(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(data['results']), 4)

    def test_price_lt_filter(self):
        response = self.client.get('/api/wines/', {'price_lt': 17})
        data = dict(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(data['results']), 6)

    def test_price_gt_filter(self):
        response = self.client.get('/api/wines/', {'points_gt': 17})
        data = dict(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(data['results']), 10)

    def test_points_lt_filter(self):
        response = self.client.get('/api/wines/', {'points_lt': 80})
        data = dict(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(data['results']), 0)

    def test_points_gt_filter(self):
        response = self.client.get('/api/wines/', {'points_gt': 80})
        data = dict(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(data['results']), 10)

    def test_variety_filter(self):
        response = self.client.get('/api/wines/', {'variety': 'Portuguese Red'})
        data = dict(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(data['results']), 1)

    def test_all_filters_together(self):
        filters = {
            'country': 'US',
            'description': 'herbal',
            'price_lt': 70,
            'price_gt': 60,
            'points_lt': 90,
            'points_gt': 80,
            'variety': 'Pinot Noir'
        }
        response = self.client.get('/api/wines/', filters)
        data = dict(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(data['results']), 1)
