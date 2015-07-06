import json

txt_file = open('rooms001.json', 'r')
json_data = txt_file.read()
parsed_json = json.loads(json_data)
print parsed_json

