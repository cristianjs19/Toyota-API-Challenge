from django.test import TestCase
from ..models import Vehicle, Characteristic

class VehicleModelTestCase(TestCase):
    def setUp(self):
        self.vehicle = Vehicle.objects.create(
            model_name='Toyota Hilux',
            type=1,
            year=2022,
            price=55000,
            active=True
        )

    def test_vehicle_creation(self):
        # Test the creation of a Vehicle instance.
        self.assertEqual(self.vehicle.model_name, 'Toyota Hilux')
        self.assertEqual(self.vehicle.type, 1)
        self.assertEqual(self.vehicle.year, 2022)
        self.assertEqual(self.vehicle.price, 55000)
        self.assertTrue(self.vehicle.active)

    def test_vehicle_str(self):
        # Test the __str__ method of the Vehicle model.
        self.assertEqual(str(self.vehicle), 'Toyota Hilux')

class CharacteristicModelTestCase(TestCase):
    def setUp(self):
        self.characteristic = Characteristic.objects.create(
            title='New Super Engine',
            description='Lorem Ipsum',
        )

    def test_characteristic_creation(self):
        # Test the creation of a Characteristic instance.
        self.assertEqual(self.characteristic.title, 'New Super Engine')
        self.assertEqual(self.characteristic.description, 'Lorem Ipsum')

    def test_characteristic_str(self):
        # Test the __str__ method of the Characteristic model.
        self.assertEqual(str(self.characteristic), 'New Super Engine')