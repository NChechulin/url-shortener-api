# URL Shortener API

Simple API for URL shortener written on Python3 + Flask

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

Firstly, you have to clone the repo:
```
git clone https://github.com/NChechulin/url-shortener-api
cd url-shortener-api
```

After you did this, you can follow official [documentation](https://flask.palletsprojects.com/en/1.1.x/tutorial/deploy/) to deply the app to production.
If you want to run debug version, run:
```
flask run
```
