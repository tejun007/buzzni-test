import sys

from web.config import Config
from web.main import create_app

app = create_app(Config)

if __name__ == '__main__':
    app.run(
        host='::',
        port=int(sys.argv[1]) if len(sys.argv) > 1 else 5000,
        threaded=True,
        debug=True)
