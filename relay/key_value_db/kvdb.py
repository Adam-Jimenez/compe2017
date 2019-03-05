import pickle
import uuid
import sys
import json

'''
    Il reste à faire les deux updates et le db info.
'''

# load DB from file
with open('database', 'rb') as f:
    database = pickle.load(f)


# DB commands
command = sys.argv[1]
content = sys.argv[2]

if command == 'insert':
    key = str(uuid.uuid4())
    database[key] = content
    print({'key': str(key)})

elif command == 'insert-with-key':
    value = json.loads(content)
    key = value['key']
    del value['key']
    database[key] = value

elif command == 'select-by-key':
    key = content
    value = database[key]
    print(value)

elif command == 'select-by-field':
    field, value = content.split('=')

    selected_elements = []
    for key in database:
        element = database[key]
        if field in element and element[field] == value:
            selected_elements.append({'key': key, 'value': database[key]})

    print(selected_elements)


elif command == 'delete-by-key':
    key = content
    del database[key]

elif command == 'delete-by-field':
    field, value = content.split('=')
    keys_to_delete = []
    for key in database:
        element = database[key]
        if field in element and element[field] == value:
            keys_to_delete.append(key)

    for key in keys_to_delete:
        del database[key]

    print(keys_to_delete)

elif command == 'update-by-key':
    pass

elif command == 'update-by-field':
    pass

elif command == 'db-info':
    pass

elif command == 'list': # used only for testing purposes
    print(database)

else:
    print('Unknow command')


# serialize DB
with open('database', 'wb') as f:
    pickle.dump(database, f)
