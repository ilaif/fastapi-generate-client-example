PYTHON_PACKAGE_NAME="my_server_client"

scripts_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
client_dir=${scripts_dir}/..
root_dir=${client_dir}/..
schema_path=${client_dir}/out/server-openapi-schema.json

cd ${root_dir}

python -m client.scripts.generate_openapi_schema --out ${schema_path}

docker run --rm \
    -v ${PWD}:/local openapitools/openapi-generator-cli generate \
    -i local/client/out/server-openapi-schema.json \
    --package-name ${PYTHON_PACKAGE_NAME} \
    -g python \
    -o /local/client/out/python

# rm server-openapi-schema.json

cd ${client_dir}

pip install ./out/python
