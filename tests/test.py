import unittest
import pandas as pd

from transform import (
        transform_fuelups,
        transform_services,
        transform_car_data
        )


class TestTransformFuelUps(unittest.TestCase):

    def setUp(self):
        self.filename = 'tests/data/test_fuelups.csv'
        self.df = pd.read_csv(self.filename)

    def test_transform_fuelups(self):
        pass


class TestTransformServices(unittest.TestCase):

    def setUp(self):
        self.filename = 'tests/data/test_services.csv'
        self.df = pd.read_csv(self.filename)

    def test_transform_car(self):
        pass


class TestTransformCarData(unittest.TestCase):

    def setUp(self):
        self.filename = 'tests/data/test_services.csv'
        self.df = pd.read_csv(self.filename)
        self.result = transform_car_data(self.filename)

    def test_transform_car_data(self):
        car_name = self.result.iloc[0]['car__name']
        mileage = self.result.iloc[0]['initial_mileage']
        car_id = self.result.iloc[0]['_id']

        self.assertTrue(len(self.result) == 1)
        self.assertEqual(car_name, 'Cuore 2008')
        self.assertEqual(mileage, 165088)
        self.assertEqual(car_id, 1)


if __name__ == '__main__':
    unittest.main()

