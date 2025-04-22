from scholarly import scholarly
import jsonpickle
import json
from datetime import datetime
import os

author: dict = scholarly.search_author_id('23XDhOwAAAAJ')
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author['publications']}
print(json.dumps(author, indent=2))
with open(f'gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}

shieldio_data2 = {
  "schemaVersion": 1,
  "label": "num_pub",
  "message": f"{len(author['publications'])-1}",
}

with open(f'gs_data_shieldsio1.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)

with open(f'gs_data_shieldsio2.json', 'w') as outfile:
    json.dump(shieldio_data2, outfile, ensure_ascii=False)
