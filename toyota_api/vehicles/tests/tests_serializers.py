from django.test import TestCase
from ..models import Vehicle, Characteristic
from ..serializers import VehicleListSerializer, VehicleDetailSerializer

class VehicleSerializerTestCase(TestCase):
    def setUp(self):
        self.vehicle = Vehicle.objects.create(
            model_name='Toyota Hilux',
            type=1,
            year=2022,
            price=20000,
            active=True
        )
        self.characteristic = Characteristic.objects.create(
            title='Test Characteristic',
            description='Test description for characteristic',
        )
        self.vehicle.characteristics.add(self.characteristic)

    def test_vehicle_list_serializer(self):
        serializer = VehicleListSerializer(instance=self.vehicle)
        expected_data = {
            'id': self.vehicle.id,
            'model_name': 'Toyota Hilux',
            'year': 2022,
            'type': 'Autos',
            'price': 20000,
            'image': '',
        }
        self.assertEqual(serializer.data, expected_data)

    def test_vehicle_detail_serializer(self):
        serializer = VehicleDetailSerializer(instance=self.vehicle)
        expected_data = {
            'id': self.vehicle.id,
            'model_name': 'Toyota Hilux',
            'year': 2022,
            'type': 'Autos',
            'price': 20000,
            'image': '',
            'subtitle': '',
            'description': None,
        }
        expected_characteristics = {
            'title': 'Test Characteristic',
            'image': '',
            'description': 'Test description for characteristic'
        }
        data = serializer.data
        dict_data = dict(data)
        characteristics = dict_data.pop('characteristics')
        dict_characteristics = dict(characteristics[0])
        self.assertEqual(dict_data, expected_data)
        self.assertEqual(dict_characteristics, expected_characteristics)

    # Add more tests as needed for serializer validation, edge cases, etc.