# CtfdLogs2Arango
Tools and utilities to play with and ingest CTFd logs in ArangoDB.

## scripts/ctfd_2_arango.py
This tool will ingest a folder with CTFd json logs into ArangoDB.

```
CtfdLogs2Arango\scripts>python ctfd_2_arango.py -h
usage: ctfd_2_arango.py [-h] -p PATH {arangodb} ...

Ingest CTFd json log files into ArangoDB.

positional arguments:
  {arangodb}

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  The path to the json files.

CtfdLogs2Arango\scripts>python ctfd_2_arango.py arangodb -h
usage: ctfd_2_arango.py arangodb [-h] [--host HOST] [--port PORT] --database
                                 DATABASE

optional arguments:
  -h, --help           show this help message and exit
  --host HOST          The ArangoDB host.
  --port PORT          The ArangoDB port.
  --database DATABASE  The ArangoDB database to use.
```

## AQL Examples
See [aql_queries](https://github.com/forensicmatt/CtfdLogs2Arango/blob/master/aql/aql_queries.md)
page.