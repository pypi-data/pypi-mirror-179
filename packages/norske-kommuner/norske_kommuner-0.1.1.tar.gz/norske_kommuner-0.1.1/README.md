# Norske Kommuner
![PyPI - Status](https://img.shields.io/pypi/status/norske-kommuner)
[![Download Stats](https://img.shields.io/pypi/dm/norske-kommuner)](https://pypistats.org/packages/poetry)

Pydantic models on Norwegian municipalities (Norske kommuner).

```python
from norske_kommuner import kommuner, get_kommune_by_nr

#  Loop over all kommuner:
for kommune in kommuner.values():
    print(kommune)

#  Get kommunenummer
print (kommuner['Stavanger'].kommunenummer) # 1103

# Can also get kommune by kommunenr
print(get_kommune_by_nr('1103')) #  Stavanger

# Each kommune is a pydantic model and have pydantic functionality like exporting to json
print(kommuner['Stavanger'].json())

```

Last line will output
```json
{
    "avgrensningsboks": {
        "coordinates":  [[[5.49903313381, 58.884658939559], [5.49903313381, 59.312103554166], [6.131310442607, 59.312103554166], [6.131310442607, 58.884658939559], [5.49903313381, 58.884658939559]]],
        "crs": {
            "properties": {
                "name": "EPSG:4258"
            },
            "type": "name"
        },
        "type": "Polygon"
    },
    "fylkesnavn": "Rogaland",
    "fylkesnummer": "11",
    "gyldigeNavn": [
        {
            "navn": "Stavanger",
            "prioritet": 1,
            "sprak": "Norwegian"
        },
        {
            "navn": null,
            "prioritet": 2,
            "sprak": null
        },
        {
            "navn": null,
            "prioritet": 3,
            "sprak": null
        }
    ],
    "kommunenavn": "Stavanger",
    "kommunenavnNorsk": "Stavanger",
    "kommunenummer": "1103",
    "punktIOmrade": {
        "coordinates": [
            5.712610778068,
            59.10201328799
        ],
        "crs": {
            "properties": {
                "name": "EPSG:4258"
            },
            "type": "name"
        },
        "type": "Point"
    },
    "samiskForvaltningsomrade": false
}
```

>Uses data and models from "[Åpent API fra Kartverket for administrative enheter](https://ws.geonorge.no/kommuneinfo/v1/)"