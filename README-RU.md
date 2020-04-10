## Ссылки

- English version is available [here](README.md)
- Репозиторий с веб-сайтом, который подключен к API, доступен [здесь](https://github.com/NChechulin/url-shortener-website)

# URL Shortener API

Простое API для сервиса сокращения ссылок, написанное на Python3 + Flask

## Методы API

### Описание

API имеет только 2 основных метода (доступ к обоим осуществляется при помощи GET-запроса):

- **get_url** - Возвращает URL, связанный с `code`.
- **shorten_link** - Возвращает code, который теперь связан с указанным `URL`.

### Примеры:

#### Некорректный shorten_link запрос

`.../api/shorten_link` возвращает ошибку:

```
{"success": false, "message": "sent link is not a valid URL"}
```

#### Корректный shorten_link запрос

`.../api/shorten_link?url=https://github.com/NChechulin` выполняется успешно:

```
{"success": true, "message": "success", "code": "8XYBh1ef"}
```

#### Некорректный get_url запрос

`.../api/get_url` возвращает ошибку:

```
{"success": false, "message": "code could not be found"}
```

#### Корректный get_url запрос

`.../api/get_url?code=8XYBh1ef` выполняется успешно:

```
{"success": true, "message": "success", "url": "https://github.com/NChechulin"}
```

## Развертка

Сначала нужно склонировать репозиторий:
```
git clone https://github.com/NChechulin/url-shortener-api
cd url-shortener-api
```

После того, как вы это сделали, обратитесь к официальной [документации](https://flask.palletsprojects.com/en/1.1.x/tutorial/deploy/), чтобы развернуть приложение на проде.
Если вы хотите запустить отладочную версию, выполните команду:
```
flask run
```
