import os

from flask_frozen import Freezer

from andersoldahl import app

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
