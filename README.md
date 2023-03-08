# jwt-auth

Project realized for studies purpose by implemeting API authentication using JWT.

### Built With
- Python
- Flask
- JWT using RS256 algorithm

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
Note: You will be asked to type in the file name to save the key and then a passphrase.

   
3. Set environment variable. Update (or create) the .env file with the following information:  
PS: KEY_PASS will be the passphrase you created in the previous step, and the SECRET is a passphrase used in the algorithm HS256, so type in a pass of your choise. 
```sh
CONFIG_ENV=config.DevelopmentConfig
KEY_PASS=CHANGETHIS
SECRET=CHANGETHIS
```

### Usage
- Go to project folder. 
    - Run:  
        `python3 app.py` or `flask run --port 5001`
    - Access:  
        `http://127.0.0.1:5001/`


### API Endpoints

#### Obtain a JWT Token

```http
  GET /auth
```

| Parameter   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `None` | `None` | `None` |

#### API endpoint protected by authentication

```http
  GET /secret
```

| Parameter (REQUEST HEADER)   | Type       | Description                                   |
| :---------- | :--------- | :------------------------------------------ |
| `Authorization`      | `string` | `Authorization bearer` |

Note: Use the request header 'Authorization' with the JWT obtained in the `/auth` endpoint to access this resource.