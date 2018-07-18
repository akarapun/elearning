import setup
setup.pathSetup()

import db
from db import db_session
db.init_db()

import os
from flask import Flask
from flask_graphql import GraphQLView
import graphene

# import schema_models._schema as schema
import schema as rootSchema
schema = rootSchema.get()

app = Flask(__name__)
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True # for having the GraphiQL interface
    )
)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    # app.run(debug=True)

    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)