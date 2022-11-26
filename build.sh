# shellcheck disable=SC2046
# shellcheck disable=SC2005
echo $(python -m grpc_tools.protoc -I=./proto \
  --python_out=./slugs \
  --pyi_out=./slugs \
  --grpc_python_out=./slugs \
  ./proto/*.proto)
