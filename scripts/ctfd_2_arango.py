import os
import sys
sys.path.append("..")
import json
import argparse
from ctfdarango.arangohandler import ArangoHandler



def get_arguments():
    usage = """Ingest CTFd json log files into ArangoDB."""

    arguments = argparse.ArgumentParser(
        description=usage
    )

    arguments.add_argument(
        "-p", "--path",
        dest="path",
        action="store",
        required=True,
        help="The path to the json files."
    )

    subparsers = arguments.add_subparsers(
        dest="subparser_name"
    )
    arango_parser = subparsers.add_parser('arangodb')
    set_arango_parser(arango_parser)

    return arguments


def set_arango_parser(arango_parser):
    arango_parser.add_argument(
        "--host",
        dest="host",
        action="store",
        required=False,
        default='localhost',
        type=str,
        help="The ArangoDB host."
    )

    arango_parser.add_argument(
        "--port",
        dest="port",
        action="store",
        required=False,
        default=8529,
        type=int,
        help="The ArangoDB port."
    )

    arango_parser.add_argument(
        "--database",
        dest="database",
        action="store",
        required=True,
        help="The ArangoDB database to use."
    )


def process_log(location, arango_handler):
    """Process a ctfd json logfile.

    :param location:
    :param arango_handler:
    :return:
    """
    collection_name = os.path.basename(
        location
    )
    collection_name = collection_name.split(".", 1)[0]
    arango_handler.ensure_collection(
        collection_name
    )

    with open(location, "r") as logfile_fh:
        file_dict = json.load(logfile_fh)
        record_list = file_dict['results']

        for record in record_list:
            arango_handler.insert_dict(
                collection_name,
                record
            )


def main():
    arguments = get_arguments()
    options = arguments.parse_args()

    if options.subparser_name != "arangodb":
        raise(Exception("arangodb sub-command required."))

    arango_handler = ArangoHandler(
        options.database,
        host=options.host,
        port=options.port
    )

    if os.path.isdir(options.path):
        for file in os.listdir(options.path):
            full_path = os.path.join(
                options.path, file
            )
            if os.path.isfile(full_path):
                if full_path.lower().endswith(".json"):
                    if os.path.getsize(full_path) > 0:
                        print(full_path)
                        process_log(
                            full_path,
                            arango_handler
                        )
    else:
        raise(Exception("Path must be a directory."))


if __name__ == "__main__":
    main()
