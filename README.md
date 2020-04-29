## Wine api
This project consists in an API created with Django and Django Rest Framework 
that retrieves, with pagination and filters, wine reviews. The information
was provided by the [kaggle](https://www.kaggle.com/zynicide/wine-reviews) website 
with the file `winemag-data-130k-v2.csv`.

## Setup

1 - Create a Virtualenv
```
python3.7 -m venv venv
```
2 - Activate the venv
```
source ./venv/bin/activate
```
3 - Install requirements

at the project root directory
```
pip install -r requirements.txt
```

4 - Download the dataset from kaggle and transform it into a Django fixture  
A script was created to do it, just run:    
```
python add_django_fixture.py
```  

5 - Configure your database  
It runs locally with a sqlite database  
In order to do the django migrations just run:
```
python manage.py makemigrations
```
```
python manage.py migrate
```
and to populate the database with the info extracted from the csv just run
```
python manage.py loaddata wines
```
(it can take some minutes)


6 - Now you are able to run your project:
```
python manage.py runserver
```

## Tests
There are tests for the api, to run then:
```
python manage.py test
```

## How to call the api

1 - Get all wine reviews  
`curl http://127.0.0.1:8000/api/wines/`

2 - Filter wine reviews by wine country  
`curl http://127.0.0.1:8000/api/wines/?country=Brazil`

3 - Filter wine reviews by a key word in the wine description  
`curl http://127.0.0.1:8000/api/wines/?description=dry`

4 - Filter wine reviews by the wine price  
`curl http://127.0.0.1:8000/api/wines/?price=80`

5 - Filter wine reviews where the wine price is less then a value  
`curl http://127.0.0.1:8000/api/wines/?price_lt=10`

6 - Filter wine reviews where the wine price is greater then a value  
`curl http://127.0.0.1:8000/api/wines/?price_gt=150`

7 - Filter wine reviews by the wine points  
`curl http://127.0.0.1:8000/api/wines/?points=80`

8 - Filter wine reviews where the wine points is less then a value  
`curl http://127.0.0.1:8000/api/wines/?points_lt=85`

9 - Filter wine reviews where the wine price is greater then a value  
`curl http://127.0.0.1:8000/api/wines/?points_gt=95`

10 - Filter wine reviews by wine variety  
`curl http://127.0.0.1:8000/api/wines/?variety=Champagne+Blend`

and of course is possible to use filters together, like this  
`curl 'http://127.0.0.1:8000/api/wines/?country=Brazil&variety=Champagne+Blend&price_lt=30&price_gt=20&points_gt=85'`

## Response
The json response has a pagination of 10 results per request.
It contains the total count of results, the previous url, the next url
and the results. Example:

```json
{
    "count": 52,
    "next": "http://127.0.0.1:8000/api/wines/?amp=&country=Brazil&page=3",
    "previous": "http://127.0.0.1:8000/api/wines/?amp=&country=Brazil",
    "results": [
        {
            "url": "http://127.0.0.1:8000/api/wines/93689/",
            "country": "Brazil",
            "description": "Hits with barrel resin and not much else. Feels screechy and shrill, with a swath of wood tannin. Acidity pushes it along in the mouth, but this is really all about resiny wood.",
            "designation": "Cuvée Giuseppe",
            "points": 80,
            "price": 25,
            "province": "Vale dos Vinhedos",
            "region_1": "",
            "region_2": "",
            "taster_name": "Michael Schachner",
            "taster_twitter_handle": "@wineschach",
            "title": "Miolo 2009 Cuvée Giuseppe Chardonnay (Vale dos Vinhedos)",
            "variety": "Chardonnay",
            "winery": "Miolo"
        },
        {
            "url": "http://127.0.0.1:8000/api/wines/89728/",
            "country": "Brazil",
            "description": "Candied-raspberry aromas are soapy and strange. This sweet Tannat from Brazil is hollow yet cloying, with candied-cherry flavors that don't cut it. While not undrinkable, this just isn't good.",
            "designation": "Macaw Soft",
            "points": 80,
            "price": 15,
            "province": "Serra Gaúcha",
            "region_1": "",
            "region_2": "",
            "taster_name": "Michael Schachner",
            "taster_twitter_handle": "@wineschach",
            "title": "Casa Perini 2015 Macaw Soft Tannat (Serra Gaúcha)",
            "variety": "Tannat",
            "winery": "Casa Perini"
        },
        {
            "url": "http://127.0.0.1:8000/api/wines/89727/",
            "country": "Brazil",
            "description": "A nose based on candied fruit is pretty much the script for all of the Macaw reds. Like the others, this Merlot is sticky but also acidic. Flavors of raspberry Kool-Aid and foxy plum are mercifully short on the finish.",
            "designation": "Macaw Smooth",
            "points": 81,
            "price": 15,
            "province": "Vale Trentino",
            "region_1": "",
            "region_2": "",
            "taster_name": "Michael Schachner",
            "taster_twitter_handle": "@wineschach",
            "title": "Casa Perini 2016 Macaw Smooth Merlot (Vale Trentino)",
            "variety": "Merlot",
            "winery": "Casa Perini"
        },
        {
            "url": "http://127.0.0.1:8000/api/wines/89723/",
            "country": "Brazil",
            "description": "Sulfur and match stick aromas are less than pleasant and devoid of fruit. A flabby grabby palate deals oaky flavors of stale white fruits. A long but arduous finish doesn't help the situation.",
            "designation": "Da'Divas",
            "points": 82,
            "price": 15,
            "province": "Serra Gaúcha",
            "region_1": "",
            "region_2": "",
            "taster_name": "Michael Schachner",
            "taster_twitter_handle": "@wineschach",
            "title": "Lidio Carraro 2014 Da'Divas Chardonnay (Serra Gaúcha)",
            "variety": "Chardonnay",
            "winery": "Lidio Carraro"
        },
        {
            "url": "http://127.0.0.1:8000/api/wines/87978/",
            "country": "Brazil",
            "description": "Straightforward plum, cherry and tomato aromas lead to a juicy palate that's lacking in structure. Simple slightly sweet plum and black-currant flavors finish with a note of peppery spice. At only 11.5% ABV, this is Merlot is an easy sipper.",
            "designation": "Macaw",
            "points": 85,
            "price": 15,
            "province": "Serra Gaúcha",
            "region_1": "",
            "region_2": "",
            "taster_name": "Michael Schachner",
            "taster_twitter_handle": "@wineschach",
            "title": "Casa Perini 2014 Macaw Merlot (Serra Gaúcha)",
            "variety": "Merlot",
            "winery": "Casa Perini"
        },
        {
            "url": "http://127.0.0.1:8000/api/wines/81077/",
            "country": "Brazil",
            "description": "Dusty medicinal cherry aromas are a touch earthy. This feels flat and low on structure, but at 11.5% ABV that should be expected. Roasted plum flavors finish with a rustic hickory note.",
            "designation": "Macaw",
            "points": 84,
            "price": 15,
            "province": "Serra Gaúcha",
            "region_1": "",
            "region_2": "",
            "taster_name": "Michael Schachner",
            "taster_twitter_handle": "@wineschach",
            "title": "Casa Perini 2014 Macaw Tannat (Serra Gaúcha)",
            "variety": "Tannat",
            "winery": "Casa Perini"
        },
        {
            "url": "http://127.0.0.1:8000/api/wines/79590/",
            "country": "Brazil",
            "description": "Dusty white-fruit aromas are mild and slightly floral. This 100% Chardonnay is sturdy on the palate but a bit foamy. Aged, yeasty flavors of white bread and white fruits are steady on a bready tasting finish.",
            "designation": "Blanc de Blancs Brut",
            "points": 89,
            "price": 45,
            "province": "Pinto Bandeira",
            "region_1": "",
            "region_2": "",
            "taster_name": "Michael Schachner",
            "taster_twitter_handle": "@wineschach",
            "title": "Cave Geisse 2012 Blanc de Blancs Brut Chardonnay (Pinto Bandeira)",
            "variety": "Chardonnay",
            "winery": "Cave Geisse"
        },
        {
            "url": "http://127.0.0.1:8000/api/wines/79282/",
            "country": "Brazil",
            "description": "Briny stone-fruit aromas are sweetened by notes of apple blossom. A full, slightly foamy palate is lively but brusque, while this tastes of yeasty peach and apricot in front of a mildly bitter finish.",
            "designation": "130 Brut",
            "points": 88,
            "price": 33,
            "province": "Brazil",
            "region_1": "",
            "region_2": "",
            "taster_name": "Michael Schachner",
            "taster_twitter_handle": "@wineschach",
            "title": "Casa Valduga NV 130 Brut  (Brazil)",
            "variety": "Champagne Blend",
            "winery": "Casa Valduga"
        },
        {
            "url": "http://127.0.0.1:8000/api/wines/76130/",
            "country": "Brazil",
            "description": "Cherry, plum and earth aromas form a sound bouquet. This Merlot is full, round and well balanced. Flavors of black fruits are helped along by integrated spice and earth tones, while the finish shows ripeness and a smooth texture.",
            "designation": "Agnus",
            "points": 88,
            "price": 15,
            "province": "Serra Gaúcha",
            "region_1": "",
            "region_2": "",
            "taster_name": "Michael Schachner",
            "taster_twitter_handle": "@wineschach",
            "title": "Lidio Carraro 2011 Agnus Merlot (Serra Gaúcha)",
            "variety": "Merlot",
            "winery": "Lidio Carraro"
        },
        {
            "url": "http://127.0.0.1:8000/api/wines/74420/",
            "country": "Brazil",
            "description": "Dry, earthy aromas of baked berry fruits and mushroom set up a tannic, pulpy, full-bodied palate with good balance. This blend of Cabernet Sauvignon, Merlot and Tannat boasts earthy plum, pepper and licorice flavors along with a light, herbal finish. Drink now.",
            "designation": "Talento",
            "points": 87,
            "price": 21,
            "province": "Brazil",
            "region_1": "",
            "region_2": "",
            "taster_name": "Michael Schachner",
            "taster_twitter_handle": "@wineschach",
            "title": "Salton 2009 Talento Red (Brazil)",
            "variety": "Red Blend",
            "winery": "Salton"
        }
    ]
}
```  