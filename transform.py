# Author Vito Minheere

"""
Transform Fuelly/aCar data into CarReport data
"""
import glob

import pandas as pd


def loop_over_files():
    files = glob.glob('data/*.csv')

    fuelups = []
    services = []
    cars = []

    for filename in files:
        print('Reading ' + filename)
        if 'fuelups' in filename:
            # fuelups.append(transform_fuelups(filename))
            cars.append(transform_car_data(filename))
        elif 'services' in filename:
            # services.append(transform_services(filename))
            pass

    if fuelups:
        fuelups_all = pd.concat(fuelups)
        fuelups_all.to_csv('transformed/fuelups.csv', index=False)

    if services:
        service_all = pd.concat(services)
        service_all.to_csv('transformed/other_cost.csv', index=False)

    if cars:
        cars_all = pd.concat(cars)
        cars_all.to_csv('transformed/car.csv', index=False)
        print('Wrote file to tramsformed/car.csv')


def transform_fuelups(filename: str) -> pd.DataFrame:
    df = pd.read_csv(filename)
    df = df.rename(columns=lambda x: x.strip())

    car_report_cols = [
            '_id', 'date', 'mileage', 'volume',
            'price', 'partial', 'note', 'fuel_type_id', 'car_id'
            ]

    # Copy relevant columns from Fuelly data
    new = df[[
            'odometer', 'km', 'litres', 'price', 'fuelup_date', 'notes',
            'partial_fuelup'
            ]].copy()

    # Rename columns to CarReport names
    new = new.rename(columns={
        'odometer': 'mileage',
        'fuelup_date': 'date',
        'partial_fuelup': 'partial',
        'litres': 'volume',
        'notes': 'note'
        })

    # Set up new data for Car Report
    new['_id'] = new.index + 1
    new['price'] = round(new['price'] * new['volume'], 3)
    new['fuel_type_id'] = 1
    new['car_id'] = 1
    new['partial'] = new['partial'].replace({0: 'FALSE', 1: 'TRUE'})
    new['note'] = new['note'].fillna('')

    # Set columns in CarReport order
    new = new[car_report_cols]
    return new

    # Save without the pandas index column
    new.to_csv('transformed/refueling.csv', index=False)


def transform_services(filename: str) -> pd.DataFrame:
    df = pd.read_csv(filename)
    df = df.rename(columns=lambda x: x.strip())

    car_report_cols = [
            '_id', 'title', 'date', 'mileage', 'price',
            'recurrence_interval', 'recurrence_multiplier',
            'end_date', 'note', 'car_id'
            ]

    new = df[[
        'odometer', 'price', 'service_date',
        'sub_service_types', 'notes'
        ]]

    # Rename columns to CarReport names
    new = new.rename(columns={
        'odometer': 'mileage',
        'service_date': 'date',
        'sub_service_types': 'title',
        'notes': 'note'
        })

    # Set up new data for Car Report
    new['_id'] = new.index + 1
    # Have to set these up in the app itself
    new['recurrence_multiplier'] = 1
    new['recurrence_interval'] = 0

    new['note'] = new['note'].fillna('')
    new['end_date'] = ''
    new['car_id'] = 1

    new = new[car_report_cols]


def transform_car_data(filename: str) -> pd.DataFrame:
    """
    Get the car from the fuelup csv
    """
    df = pd.read_csv(filename)
    df = df.rename(columns=lambda x: x.strip())

    # Get the lowest mileage first
    df = df.sort_values(by=['odometer'], ascending=True)

    # copy only the first row
    new = df[['car_name', 'odometer']].head(1).copy()

    car_report_cols = [
        '_id', 'car__name', 'color', 'initial_mileage', 'suspended_since'
        ]

    new['_id'] = 1
    new['color'] = -33230
    new['suspended_since'] = ''
    new = new.rename(columns={
        'car_name': 'car__name',
        'odometer': 'initial_mileage'
        })

    new = new[car_report_cols]
    return new


loop_over_files()
# transform_car_data('data/services.csv')
