#!/usr/bin/env python

from elasticsearch import Elasticsearch
from MaltegoTransform import *
import os

phrase = sys.argv[1]
m = MaltegoTransform()

try:
 es = Elasticsearch('http://127.0.0.1:9200')

 res = es.search(index="crawl", doc_type="tor", body={"query": {"match": {"url": phrase}}})
 for doc in res['hits']['hits']:
  m.addEntity('maltego.Person', ', '.join(doc['_source']['entities']['persons']).decode('utf-8', 'ignore'))

except Exception as e:
 m.addUIMessage(str(e))

m.returnOutput()
