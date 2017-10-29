# -*- coding: utf-8 -*-

import json
import datetime

nobel_winners = [
    {
        'category': 'Physics',
        'name': 'Albert Einstein',
        'nationality': 'Swiss',
        'sex': 'male',
        'year': 1921,
    },
    {
        'category': 'Physics',
        'name': 'Paul Dirac',
        'nationality': 'British',
        'sex': 'male',
        'year': 1933
    },
    {
        'category': 'Chemistry',
        'name': 'Marie Curie',
        'nationality': 'Polish',
        'sex': 'female',
        'year': 1911
    }
]


def dump_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_json(filename):
    with open(filename):
        data = json.load(filename)
        print("data", data)


def datetime_to_json(filename):
    print(datetime.now())
    json.dumps(datetime.now())


class JSONDataTimeEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()
        else:
            return json.JSONEncoder.default(self, obj)


def dumps(obj):
    return json.dumps(obj, cls=JSONDataTimeEncoder)


# dump_json(nobel_winners, 'data/nobel_winners.json')
# j = open('data/nobel_winners.json').read()
# load_json("data/nobel_winners.json")

print(dumps({'time': datetime.datetime.now()}))

# datetime_to_json('data/datetime.json')


