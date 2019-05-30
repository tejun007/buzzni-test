import sys

from common.config import Config
from common.main import create_app

app = create_app(Config)

if __name__ == '__main__':
    app.run(
        host='::',
        port=int(sys.argv[1]) if len(sys.argv) > 1 else 5001,
        threaded=True,
        debug=True)