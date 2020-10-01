python -m grpc_tools.protoc --proto_path=proto_src/ --python_out=proto/ --grpc_python_out=proto/ common.proto transManager.proto inspectorSync.proto
# python -m grpc_tools.protoc --proto_path=. --python_out=proto/ --grpc_python_out=proto/ proto/common.proto proto/transManager.proto proto/inspectorSync.proto

# python generateIndexFile.py --pacs_dir=../data/PACS -s 1