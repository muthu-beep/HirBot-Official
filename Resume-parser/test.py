import json
from pyresparser import ResumeParser

data = ResumeParser('/home/adi/sample.pdf').get_extracted_data()
print(data)
with open('data.json', 'w') as fp:
    json.dump(data, fp)

