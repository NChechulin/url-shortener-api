## Links

- :ru: [Версия на русском языке](README-RU.md)
- [Website which connects to API](https://github.com/NChechulin/url-shortener-website)

# URL Shortener API

Simple API for URL shortener written in Python3 + Flask

## API Methods

### Descriptions

Api has only 2 main methods (both are accessed with get request):

- **get_url** - Returns URL associated with `code`.
- **shorten_link** - Returns code which is now associated with specified `URL`.

### Examples:

#### Incorrect shorten_link request

`.../api/shorten_link` returns Error:

```
{"success": false, "message": "sent link is not a valid URL"}
```

#### Correct shorten_link request

`.../api/shorten_link?url=https://github.com/NChechulin` returns Success:

```
{"success": true, "message": "success", "code": "8XYBh1ef"}
```

#### Incorrect get_url request

`.../api/get_url` returns Error:

```
{"success": false, "message": "code could not be found"}
```

#### Correct get_url request

`.../api/get_url?code=8XYBh1ef` returns Success:

```
{"success": true, "message": "success", "url": "https://github.com/NChechulin"}
```

## Deploy

### Cloning the repo

Firstly, you have to clone the repo:

```
git clone https://github.com/NChechulin/url-shortener-api
cd url-shortener-api
```

### Requirements

You have to install Flask:

```
pip install -r requirements.txt
```

Also you have to created a SQLite database called `urls.db` in directory where `app.py` is located

### Running

After you did this, you can follow official [documentation](https://flask.palletsprojects.com/en/1.1.x/tutorial/deploy/) to deploy the app to production.
If you want to run debug version, run:

```
flask run
```
