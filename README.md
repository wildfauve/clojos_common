## GRPC Common Services

Build them:

```shell
poetry run python -m grpc_tools.protoc --proto_path=. ./clojos_common/service/protobufs/teams_service/teams_service.proto --python_out=. --grpc_python_out=.
```