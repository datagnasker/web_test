import os
import uuid
from flask import Flask

app = Flask(__name__)
app.config.update(
    FLAG=os.getenv('FLAG', 'FLAG_PLACEHOLDER'),
    SECRET=uuid.uuid4()
)

import bitbibliotek.views
