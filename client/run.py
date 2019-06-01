import sys

from client.web.config import Config
from client.web.main import create_app

app = create_app(Config)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=int(sys.argv[1]) if len(sys.argv) > 1 else 5000,
        threaded=True,
        debug=True)
