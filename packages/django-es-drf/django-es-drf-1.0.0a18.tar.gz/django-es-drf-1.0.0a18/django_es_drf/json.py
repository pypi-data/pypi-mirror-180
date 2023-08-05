import json
from json import JSONEncoder
from elasticsearch_dsl import Document, AttrList, AttrDict
from elasticsearch_dsl.response import AggResponse
import datetime


def to_plain_json(doc, skip_empty=True):
    return json.loads(es_dump(doc.to_dict(skip_empty=skip_empty)))


class ESEncoderClass(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Document):
            return obj.to_dict()
        if isinstance(obj, AttrList):
            return obj._l_
        if isinstance(obj, AttrDict):
            return obj._d_
        if isinstance(obj, AggResponse):
            return obj.to_dict()
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        if isinstance(obj, datetime.date):
            return obj.isoformat()
        return super().default(obj)


def es_dump(obj, **kwargs):
    return json.dumps(obj, cls=ESEncoderClass, **kwargs)
