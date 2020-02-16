import requests
import faker
import json
from pages.base_page import BasePage


f = faker.Faker()
email = f.email()
name = f.name()
URL2 = "https://foo:bar@test.grinfer.com/api/auth/swagger-ui.html"
URL = "https://foo:bar@test.grinfer.com/api/auth/create"
data = {"email": email,
        "externalAuthToken": "string",
        "externalAuthType": "string",
        "firstName": name,
        "grantType": "string",
        "lastName": name,
        "password": "QWEasd123",
        "rememberMe": 'true'}

response = requests.get(URL2)
#print(response.content)
print(response.headers)
