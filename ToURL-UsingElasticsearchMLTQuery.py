#!/usr/bin/env python

from elasticsearch import Elasticsearch
from MaltegoTransform import *
import os

phrase = sys.argv[1]
m = MaltegoTransform()

try:
 es = Elasticsearch('http://127.0.0.1:9200')

 res = es.search(
  index="crawl",
  doc_type="tor",
  body =
   {"query":
    {"more_like_this" :
     {"like" : phrase,
      "min_term_freq" : 0,
      "max_query_terms" : 25
     }
    }
   })

# print("%d documents found" % res['hits']['total'])

 for doc in res['hits']['hits']:

   ent = m.addEntity('maltego.URL', doc['_source']['url'])

   #ent = m.addEntity('maltego.Person', ', '.join(doc['_source']['entities']['persons']).decode('utf-8', 'ignore'))

   #ent = m.addEntity('maltego.Location', ', '.join(doc['_source']['entities']['locations']).decode('utf-8', 'ignore'))


except Exception as e:
 m.addUIMessage(str(e))

m.returnOutput()

