# cp-hack-backend
Backend for Christmas Pineapple Hack

## Setup
`brew install pip3`
`pip3 install -r requirements.txt`

## Migrations
Make sure you are running Postgres Server. New Models are recognised and migrations are generated.
`python3 manage.py db migrate`
`python3 manage.py db upgrade`
