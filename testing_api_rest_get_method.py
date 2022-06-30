import requests

response = requests.get("https://httpbin.org/get", timeout=5)

print("HTTP Status Code: " + str(response.status_code))
print(response.headers)
print('________________________________________________')
if response.status_code == 200:
    results = response.json()
    for result in results.items():
        print(result)
    print('________________________________________________')
    print('\033[1m' + 'Header Response: ' + '\033[0m')
    for header, value in response.headers.items():
        print(header, '-->', value)
    print('________________________________________________')
    print('\033[1m' + 'Header Request: ' + '\033[0m')
    for header, value in response.request.headers.items():
        print(header, '-->', value)
    print('________________________________________________')
    print('\033[1m' + 'Server: ' + '\033[0m'+ response.headers['server'])
else:
    print("Server:" + response.headers['server'])
