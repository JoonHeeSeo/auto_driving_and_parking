
# Installations

## Apollo CLI
npm install -g apollo

## graphql
npm install -g graphql

## graphql-introspection-json-to-sdl
npm install -g graphql-introspection-json-to-sdl


## Schema Steps
apollo schema:download --endpoint=http://127.0.0.1:8000/graphql
./gradlew :app:downloadApolloSchema --endpoint=http://127.0.0.1:8000/graphql --schema=app/src/main/graphql/com/simple/graphql/schema.graphqls
