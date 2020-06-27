# Zenser Assignment
 
Use below username and password

>**Username/password** :- **admin/admin**


## How to Use 

- **Custom Command**

```python
./manage.py createpartner <Number of recored want to create>
```

- **REST API**

    **GET request**
    
    To get access token for API
```
python manage.py drf_create_token admin

```
```python
import requests, json, pprint
p = requests.get('http://localhost:8000/api/', headers=headers)
print(p.content)

Above code gives you all api routes
```
   
   **List all routers**
```python
import requests, json, pprint
headers = {
    'authorization': "f4117ce38efa9c0a70f7c426f17d27222a22447b",
    'cache-control': "no-cache",
    }
p = requests.get('http://localhost:8000/api/router/', headers=headers)
print(p.content)

```
   
   **Create routers**
```python
import requests, json, pprint
headers = {
    'authorization': "f4117ce38efa9c0a70f7c426f17d27222a22447b",
    'cache-control': "no-cache",
    }
p = requests.post('http://localhost:8000/api/router/', headers=headers,data=json.dumps({
   'sapid':<Value>,
   'hostname': <Value>,
   'loopback': <Value>,
   'mac_address': <Value>,
   }))
print(p.content)

```
   
   **Get single router**
```python
import requests, json, pprint
headers = {
    'authorization': "f4117ce38efa9c0a70f7c426f17d27222a22447b",
    'cache-control': "no-cache",
    }
p = requests.put('http://localhost:8000/api/router/<int:id>', headers=headers)
print(p.content)

```
   
   **Update router**
```python
import requests, json, pprint
headers = {
    'authorization': "f4117ce38efa9c0a70f7c426f17d27222a22447b",
    'cache-control': "no-cache",
    }
p = requests.put('http://localhost:8000/api/router/<int:id>', headers=headers,data=json.dumps({
   'sapid':<Value>,
   'hostname': <Value>,
   'loopback': <Value>,
   'mac_address': <Value>,
   }))
print(p.content)

```
   
   **Delete router**
```python
import requests, json, pprint
headers = {
    'authorization': "f4117ce38efa9c0a70f7c426f17d27222a22447b",
    'cache-control': "no-cache",
    }
p = requests.delete('http://localhost:8000/api/router/<int:id>', headers=headers)
print(p.content)

```

   **Delete router By IP**
```python
import requests, json, pprint
headers = {
    'authorization': "f4117ce38efa9c0a70f7c426f17d27222a22447b",
    'cache-control': "no-cache",
    }
p = requests.delete('http://localhost:8000/api/router/delete_base_on_ip?ip=<str:ip>', headers=headers)
print(p.content)

```


