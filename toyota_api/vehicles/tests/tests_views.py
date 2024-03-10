from django.test import TestCase, Client as TestClient
from django.urls import reverse
from rest_framework.test import APIClient
from ..models import Vehicle

class VehiclesListRetrieveViewTestCase(TestCase):
    def setUp(self):
        self.client = TestClient(HTTP_ORIGIN='https://example.com')

        # Create test data
        Vehicle.objects.create(model_name='Test Vehicle 1', type=1, year=2022, price=20000, active=True)
        Vehicle.objects.create(model_name='Test Vehicle 2', type=2, year=2023, price=25000, active=True)
        Vehicle.objects.create(model_name='Test Vehicle 3', type=3, year=2021, price=18000, active=True)
        Vehicle.objects.create(model_name='Test Vehicle 4', type=1, year=2020, price=30000, active=False)

    def test_list_retrieve_view(self):
        # Test list endpoint
        url = reverse('vehicles:vehicles-list')
        response = self.client.get(url, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        # Return all vehicles
        self.assertEqual(len(response.data), 3)

    def test_filter_by_type(self):
        url = reverse('vehicles:vehicles-list') + '?' + 'type=Autos'
        response = self.client.get(url, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        # only Autos are returned
        self.assertEqual(len(response.data), 1)

    def test_order_by_price(self):
        url = reverse('vehicles:vehicles-list') + '?' + 'order_by=price'
        response = self.client.get(url, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        prices = [vehicle['price'] for vehicle in response.data]

        # Check if the prices are in ascending order
        self.assertEqual(prices, [18000, 20000, 25000])

    def test_order_by_price_inverted(self):
        url = reverse('vehicles:vehicles-list') + '?' + 'order_by=-price'
        response = self.client.get(url, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        prices = [vehicle['price'] for vehicle in response.data]
        # Check if the prices are in descending order
        self.assertEqual(prices, [25000, 20000,18000])

    def test_order_by_year(self):
        url = reverse('vehicles:vehicles-list') + '?' + 'order_by=year'
        response = self.client.get(url, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        years = [vehicle['year'] for vehicle in response.data]
        # Check if the years are in ascending order
        self.assertEqual(years, [2021, 2022, 2023])

    def test_order_by_year_inverted(self):
        url = reverse('vehicles:vehicles-list') + '?' + 'order_by=-year'
        response = self.client.get(url, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        years = [vehicle['year'] for vehicle in response.data]
        # Check if the years are in descending order
        self.assertEqual(years, [2023, 2022, 2021])

    def test_retrieve_detail_view(self):
        vehicle = Vehicle.objects.filter(active=True).first()
        url = reverse('vehicles:vehicles-detail', kwargs={'pk': vehicle.pk})
        response = self.client.get(url, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        # Assert that the returned data matches the expected data for the vehicle
        self.assertEqual(response.data['model_name'], vehicle.model_name)
        self.assertEqual(response.data['type'], 'Autos')
        self.assertEqual(response.data['year'], vehicle.year)
        self.assertEqual(response.data['price'], vehicle.price)

    def test_retrieve_inactive_vehicle(self):
        inactive_vehicle = Vehicle.objects.filter(active=False).first()
        inactive_url = reverse('vehicles:vehicles-detail', kwargs={'pk': inactive_vehicle.pk})
        inactive_response = self.client.get(inactive_url, content_type='application/json')
        # Assert that inactive vehicles return a 404 status code
        self.assertEqual(inactive_response.status_code, 404)

    def test_retrieve_detail_view_structure(self):
        vehicle = Vehicle.objects.filter(active=True).first()
        url = reverse('vehicles:vehicles-detail', kwargs={'pk': vehicle.pk})
        response = self.client.get(url, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        # Assert response structure
        expected_keys = ['id', 'model_name', 'year', 'type', 'price', 'image', 'subtitle', 'description', 'characteristics']
        self.assertEqual(set(response.data.keys()), set(expected_keys))
