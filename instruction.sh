# lunch env
python -m venv venv
.\venv\Scripts\activate
# migration
flask db init
flask db migrate -m "Initial migration"
flask db upgrade