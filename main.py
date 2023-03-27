from flask import Flask
from decouple import config
# from apis import api


if __name__ == '__main__':
    app = Flask(__name__)
    app.config.from_object(config("APP_SETTINGS"))
    # api.init_app(app)

    app.run(debug=True)
