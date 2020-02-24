import json
import argparse

import server.app


def main():
    parser = argparse.ArgumentParser(description='Generate OpenAPI Schema')
    parser.add_argument('--out', help='Target schema path')
    args = parser.parse_args()

    openapi_schema = server.app.app.openapi()

    with open(args.out, 'w') as f:
        json.dump(openapi_schema, f)


if __name__ == '__main__':
    main()
