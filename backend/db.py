from databricks import sql

# Databricks Configuration
DATABRICKS_SERVER_HOST = "your-databricks-host"
DATABRICKS_HTTP_PATH = "your-http-path"
DATABRICKS_ACCESS_TOKEN = "your-access-token"

def get_db_connection():
    conn = sql.connect(
        server_hostname=DATABRICKS_SERVER_HOST,
        http_path=DATABRICKS_HTTP_PATH,
        access_token=DATABRICKS_ACCESS_TOKEN
    )
    return conn
