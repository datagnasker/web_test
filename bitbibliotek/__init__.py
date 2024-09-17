import os
import uuid
from flask import Flask

app = Flask(__name__)


def create_app():
    app.config.update(
            FLAG=os.getenv('FLAG', 'FLAG_PLACEHOLDER'),
            USERNAME=os.getenv('NAME', 'datagnasker'),
            PASSWORD=os.getenv('PASS', 'kodeord1'),
            SECRET=uuid.uuid4()
            )
    return app

import bitbibliotek.views
