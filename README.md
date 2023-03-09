# jwt-auth

Project realized for studies purpose by implemeting API authentication using JWT.

### Built With
- Python
- Flask
- JWT authentication

### Installation

1. Clone the repo
```sh
git clone https://github.com/warzinnn/jwt-auth.git
```

2. Install requirements
```sh
pip install -r requirements
```

3. Generating an RSA key pair
This projects uses the asymmetric algorithm RS256, so you will need to generate a public/private key pair.
```bash
mkdir .ssh
ssh-keygen -t rsa
```
Note: You will also be asked to type in the file name to save the key and then a passphrase.

   
4. Set environment variable. Update (or create) the .env file with the following information:  
PS: KEY_PASS will be the passphrase you created in the previous step, and the SECRET is a passphrase used in the algorithm HS256, so type in a pass of your choise. 
Also type in a postgres user and password of your choice.
```sh
CONFIG_ENV=config.DevelopmentConfig
KEY_PASS=CHANGE_THIS
POSTGRES_USER=CHANGE_THIS
POSTGRES_PASSWORD=CHANGE_THIS
POSTGRES_DB=login
POSTGRES_URL="postgresql+psycopg2://${POSTGRES_USER}:${POSTGRES_PASSWORD}@localhost:5432/${POSTGRES_DB}"
```

5. Docker (Set up Postgresql)
```sh 
docker-compose up
```

### Usage
- Go to project folder. 
    - Run:  
        `python3 app.py` or `flask run --port 5001`
    - Access:  
        `http://127.0.0.1:5001/`

- Credentials information:
```
- Admin Access
Email: admin@email.com 
Password: pass_a

- User access
Email: user@email.com 
Password: pass_u

- Backoffice access
Email: backoffice@email.com
Password: pass_b
```



### API Endpoints
- There's a postman collection in the project files with the list of the resources and their respective parameters.
    `jwt-auth.postman_collection.json`

#### Obtain a JWT Token

```http
  GET /api/auth/login
```

| Method   | Parameters         | Description                      |
| :---------- | :--------- | :----------------------------------   |
| `POST` | `email, password` | `authentication credentials` |

#### API endpoint protected by authentication

```http
  GET /api/secret
```


| Method   | Parameters         | Description                      |
| :---------- | :--------- | :----------------------------------   |
| `GET` | `Authorization (JWT Token)`  | `Authorization bearer header` |


Note: Use the request header 'Authorization' with the JWT obtained in the `/api/auth/login` endpoint to access this resource.

#### API endpoint protected by authentication and role verification

```http
  GET /api/secret/admin
```


| Method   | Parameters         | Description                      |
| :---------- | :--------- | :----------------------------------   |
| `GET` | `Authorization (JWT Token)`  | `Authorization bearer header` |


Note: Use the request header 'Authorization' with the JWT obtained in the `/api/auth/login` endpoint to access this resource.
In this case you will need to be authenticated with admin credentials.