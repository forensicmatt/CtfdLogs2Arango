import uuid
from arango import ArangoClient


class ArangoHandler(object):
    def __init__(self, database, protocol='http', host='localhost', port=8529, username='root', password=''):
        """Initialize an ArangoDB Handler to handle all arangodb operations.

        :param database: (str) The database name to use
        :param protocol: (str) The protocol
        :param host: (str) The host
        :param port: (int) The port
        :param username: (str)
        :param password:
        """
        self._database = database
        self.username = username
        self.password = password
        self.client = ArangoClient(
            protocol=protocol,
            host=host,
            port=port
        )
        self._system_db = self.client.db(
            '_system',
            username=self.username,
            password=self.password
        )

        if not self._system_db.has_database(self._database):
            self._system_db.create_database(self._database)

        self._database = self.client.db(
            self._database,
            username=self.username,
            password=self.password
        )
        self.collections = {}

    def ensure_collection(self, collection):
        if not self._database.has_collection(collection):
            self._database.create_collection(collection)

    def get_system_db(self):
        return self._system_db

    def insert_dict(self, collection, record):
        if collection not in self.collections:
            arango_collection = self._database.collection(
                collection
            )
            self.collections[collection] = arango_collection
        else:
            arango_collection = self.collections[collection]

        insert_record = record
        insert_record["_key"] = uuid.uuid4().hex

        arango_collection.insert(
            insert_record
        )
