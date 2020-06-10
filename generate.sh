python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. transManager.proto
# python generateIndexFile.py --pacs_dir=../data/PACS -s 1