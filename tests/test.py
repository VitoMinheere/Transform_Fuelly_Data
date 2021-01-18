import unittest
import pandas as pd

from transform import (
        transform_fuelups,
        transform_services,
        transform_car_data,
        loop_over_files
        )


class TestTransformFuelUps(unittest.TestCase):

    def setUp(self):
        self.filename = 'tests/data/test_fuelups.csv'
        self.result = transform_fuelups(self.filename)

    def test_find_id(self):
        car_id = self.result.iloc[0]['car_id']
        self.assertEqual(car_id, 1)

    def test_find_(self):
        note = self.result.iloc[0]['note']
        self.assertEqual(note, 'test note')


class TestTransformServices(unittest.TestCase):

    def setUp(self):
        self.filename = 'tests/data/test_services.csv'
        self.result = transform_services(self.filename)

    def test_correct_service_title(self):
        title = self.result.iloc[0]['title']
        self.assertEqual(title, 'car_wash')


class TestTransformCarData(unittest.TestCase):

    def setUp(self):
        self.filename = 'tests/data/test_services.csv'
        self.result = transform_car_data(self.filename)

    def test_get_correct_id(self):
        car_id = self.result.iloc[0]['_id']
        self.assertEqual(car_id, 1)

    def test_find_car_name(self):
        car_name = self.result.iloc[0]['car__name']
        self.assertEqual(car_name, 'Test Car')

    def test_find_start_mileage(self):
        mileage = self.result.iloc[0]['initial_mileage']
        self.assertEqual(mileage, 165088)


# class TestMultipleCars(unittest.TestCase):

#     def setUp(self):
#         directory = 'tests/data'
#         loop_over_files(directory=directory)
#         self.services = pd.read_csv('tests/data/transformed/other_cost.csv')
#         self.fuelups = pd.read_csv('tests/data/transformed/fuelups.csv')
#         self.cars = pd.read_csv('tests/data/transformed/car.csv')

#     def test_added_multiple_cars(self):
#         self.assertTrue(len(self.cars) > 1)


if __name__ == '__main__':
    unittest.main()

