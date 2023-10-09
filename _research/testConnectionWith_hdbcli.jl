using ConfigEnv
@show dotenv(".env")

using PythonCall

dbapi = pyimport("hdbcli.dbapi")
getpass = pyimport("getpass")

hana_conn = dbapi.connect(
    address=ENV["AIRMS_HOST"],
    port=ENV["AIRMS_PORT"],
    user=ENV["AIRMS_USER"],
    databaseName= ENV["AIRMS_DATABASE"],
    password = getpass.getpass("Enter your password:"),
    encrypt=ENV["AIRMS_ENCRYPT"]
)
@show hana_conn