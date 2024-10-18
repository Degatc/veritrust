# Verytrust application

## Back-end

### Installation of dependencies

```
pip install -r requirements.txt
```

### Creation of environnement file

Create a .env file with your authentication token and the database URL

```
#.env file
# Twitter configuration
TWITTER_BEARER_TOKEN="..."

# Instagram configuration
INSTAGRAM_BEARER_TOKEN="..."

# BDD 
DATABASE_URL="..."
```

### Start verytrust back-end

```
python3 verytrust-backend/app.py 
```

## Front-end

### Move to the front-end folder
```
cd verytrust-frontend/
```

### Installation of dependencies

```
npm install
```

### Start verytrust front-end

```
npm start 
```
