
import os
import logging
from dotenv import load_dotenv
import traceback
import getpass

from hdbcli import dbapi

# Load Environment Variables
load_dotenv()

# Set logging
logging.basicConfig(
    format="%(asctime)s | %(levelname)s : %(message)s", level=logging.DEBUG
)
LOG = logging.getLogger(__name__)

def connect_db():
    #Establish a connection to AIR.MS
    airms_env_options = {
                "address": os.getenv("AIRMS_HOST"),
                "port": os.getenv("AIRMS_PORT"),
                "user": os.getenv("AIRMS_USER"),
                "databaseName": os.getenv("AIRMS_DATABASE"),
                "password":getpass.getpass("Enter your password:"),
                "encrypt": os.getenv("AIRMS_ENCRYPT"),
                "sslValidateCertificate": os.getenv("AIRMS_SSL_VALIDATE_CERTIFICATE"),
                "sslHostNameInCertificate": os.getenv("AIRMS_SSL_HOSTNAME_IN_CERT"),
                "sslTrustStore": os.getenv("AIRMS_SSL_TRUSTSTORE"),
                "connectTimeout": os.getenv("AIRMS_CONNECT_TIMEOUT")
            }

    try : 
        hana_conn = dbapi.connect(**airms_env_options.copy())
        LOG.info("Initialized AIR.MS Connection :%s ", hana_conn.isconnected())
        return hana_conn
    except Exception as e:
        logging.error(traceback.format_exc())
        raise e
