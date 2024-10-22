import json

with open('training.json', 'r') as json_file:
    json_object = json.load(json_file)

print('Training Data Length: ' + str(len(json_object)))

with open('validation.json', 'r') as json_file:
    json_object = json.load(json_file)

print('Validation Data Length: ' + str(len(json_object)))

with open('test.json', 'r') as json_file:
    json_object = json.load(json_file)

print('Testing Data Length: ' + str(len(json_object)))