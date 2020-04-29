import csv
import json
import shutil
import zipfile
from tempfile import NamedTemporaryFile

import requests


def download_file():
    print('Downloading zip file from kaggle')
    response = requests.get(
        'https://storage.googleapis.com/kaggle-data-sets/1442/8172/compressed/winemag-data-130k-v2.csv.zip?'
        'GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&Expires=1588376467&Signature=jTvA6LF8JTI4Uqs%'
        '2BSQCXrFoOdU3VeEd2o9ZwGKsFg69siZ3spT4trUYfVcM1p7pmis%2FPhD49a%2BnYu0CaIVURWx2dczXRELuMnoIyNuuzyk%2B3aj%'
        '2FZpi6ulHiJe5c6px3RjapA1mw09YhKWVtnuUp5bWrEf1BVcQOGN3pCutt3kw8vpb0VJ%2FrTluWgKiph0wzLWs%2BaxnNGgGCUoltxCzi9'
        'oKGqGafDAFYCnUGymICiavXITIpb%2FTLb4nme0kZb%2FGIn5f5vz%2BiRWc77RcquRmao3I4r%2BCetuh9h%2FZNiwXgvh1eDZOEBuedwUlO'
        'qUwjQLhNw58e24zk06TokBxht3xvPfw%3D%3D&response-content-disposition='
        'attachment%3B+filename%3Dwinemag-data-130k-v2.csv.zip', stream=True)

    temp_zip = NamedTemporaryFile(suffix='.zip', mode='wb')
    with open(temp_zip.name, 'wb') as fd:
        for chunk in response.iter_content(chunk_size=128):
            fd.write(chunk)
    return temp_zip


def extract_file(zip_file_name):
    print('Extracting winemag-data-130k-v2.csv from zipfile')
    temp_csv = NamedTemporaryFile(suffix='.csv')
    with zipfile.ZipFile(zip_file_name) as z:
        with z.open('winemag-data-130k-v2.csv') as zf, open(temp_csv.name, 'wb') as csv_file:
            shutil.copyfileobj(zf, csv_file)
    return temp_csv


def transform_csv_to_django_fixture(csv_file_name):
    print('Transforming csv file into a django json fixture')
    results = []
    with open(csv_file_name, 'r') as csv_file, open('wine_reviews/fixtures/wines.json', 'w') as json_file:
        csv_reader = csv.reader(csv_file)
        # remove headers
        next(csv_reader, None)
        for row in csv_reader:
            wine_dict = {
                'model': 'wine_reviews.wine',
                'pk': int(row[0]) + 1,
                'fields': {
                    'country': row[1],
                    'description': row[2],
                    'designation': row[3],
                    'points': int(row[4]),
                    'price': float(row[5]) if row[5] else None,
                    'province': row[6],
                    'region_1': row[7],
                    'region_2': row[8],
                    'taster_name': row[9],
                    'taster_twitter_handle': row[10],
                    'title': row[11],
                    'variety': row[12],
                    'winery': row[13],
                }
            }
            results.append(wine_dict)

        json.dump(results, json_file, ensure_ascii=False)


def main():
    print('Starting script')
    try:
        zip_file = download_file()
        csv_file = extract_file(zip_file.name)
        transform_csv_to_django_fixture(csv_file.name)
        print('Script finished')
    except Exception as e:
        print(f'Error trying to run script: {e}')


if __name__ == '__main__':
    main()
