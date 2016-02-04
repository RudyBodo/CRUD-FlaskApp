from app.core.helper import create_app
from app.core.db import db
from app.crud.views import crud_views

# Development Config
config = 'config.dev'
# Production Config
# config = 'config.Prod'

app = create_app(config)
db.init_app(app)

# register blueprint
app.register_blueprint(crud_views)
