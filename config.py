import os
import subprocess

final_db_url = 'postgresql://localhost/url_shortener'
if os.environ['FLASK_ENV'] == 'production':
   heroku_app_name = 'rclv5b5'
   raw_db_url = subprocess.run(
      ["heroku", "config:get", "DATABASE_URL", "--app", heroku_app_name],
      capture_output=True
   ).stdout 

   db_url = raw_db_url.decode("ascii").strip()

   final_db_url = "postgresql+psycopg2://" + db_url.lstrip("postgres://")

# for localhost
SQLALCHEMY_DATABASE_URI = final_db_url 
SQLALCHEMY_TRACK_MODIFICATIONS = False