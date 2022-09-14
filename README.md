# url-shortener
Flask App with PostgreSQL. Deployed at: https://rclv5b5.herokuapp.com/

References:
- [How To Make a URL Shortener with Flask and SQLite](https://www.digitalocean.com/community/tutorials/how-to-make-a-url-shortener-with-flask-and-sqlite)
- [Create a Web App and Deploy it to the Cloud](https://arctype.com/blog/postgres-heroku/)
- [Step-by-Step Deployment of a Free PostgreSQL Database And Data Ingestion](https://ealizadeh.com/blog/deploy-postgresql-db-heroku)

# steps to run locally
## PostgreSQL
1. Run `psql` in command line to open the psql command line tool.
2. Do `CREATE DATABASE [database_name];` and `\c [database_name]`.
3. Close the psql command line tool with `\q`.

## Flask App
1. Clone this repository and nagivate into it.
2. Create a __.flaskenv__ file at the root.
3. Paste the following  configuration in __.flaskenv__.
```
FLASK_APP=run.py
DATABASE_URL=postgres://localhost/[database_name]
```
4. At the root of the directory, run `pip install -r requirements.txt`.
5. Run `flask db init`.
6. Run `flask db migrate -m "<message>"`.
7. Run `flask db upgrade`.
8. Start the app with `flask run` and go to the address it is running on (most likely localhost:5000) in a browser to view the page.
