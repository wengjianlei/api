import requests

url = "https://new-app-api-test.ylyk.com/v1/mydesk/overview"

payload = "{\r\n  \"calStartDate\": \"2020-08-27T07:14:06.082+0000\",\r\n  \"calEndDate\": \"2020-08-27T07:14:06.082+0000\",\r\n  \"today\": \"2020-08-27T07:14:06.082+0000\",\r\n  \"targetUserId\": 5466041\r\n}"
headers = {
    'userId': "5466041",
    'token': "ojzmNwCW67xlJN3J1RXU2KgJ6xR;4oamELwXldpOrteNqovFB4egh4Imk$",
    'Content-Type': "application/json",
    'accountId': "ylyk_app",
    'cache-control': "no-cache",
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)