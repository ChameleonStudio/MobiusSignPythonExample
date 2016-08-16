"""
MobiusSign Python usage Example

with public data

"""

import requests
import json


# compose you sign request:
sign_request = {
    'object_id': '0',
    'consumer_id': '1',
    'data_url': 'http://example.site/document.html',
    'data_note': 'Example of MobiusSign usage',
    'data_block': 'The Ultimate Question of Life, the Universe, and Everything:42',
}

# sending request
result = requests.post("http://mobiussign.com/api/sign", json=sign_request)

# decode answer
result_data = json.loads(result.content.decode())
print(result_data)


if result.status_code == 200:
    # handling successful response
    print('Your data was signed successfully')
    print('MobiusSign:', result_data['mobius_sign'])
    print('MobiusSign ID:', result_data['sign_id'])
elif 'result'in result_data:
    # handling known error
    print('Error occurred:', result_data['result'])
else:
    # handling rest of errors
    print('Something went wrong')