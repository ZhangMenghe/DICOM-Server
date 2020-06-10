# DICOM-Server
This is a gRPC server for HELM Android DICOM Viewer. With this server, clients, either working on mobile or desktop platforms, can get the latest pre-processed datasets by connecting to the server through a Remote Procedure Call(RPC) protocol.

##  Pre-request
This server run under conda virtual environment. Install Conda following [Install instruction]([https://docs.conda.io/projects/conda/en/latest/user-guide/install/](https://docs.conda.io/projects/conda/en/latest/user-guide/install/)) for Windows, Mac, or Linux.
Our environment is packed in `server_conda_env.yml`. To create an environment from `.yml`:
Use the terminal or an Anaconda Prompt for the following steps:

1.  Create the environment from the  `server_conda_env.yml`  file:
    
    `conda env create -f server_conda_env.yml`
    
    The first line of the  `yml`  file sets the new environment's name. In our case, the name is `server`

2.  Verify that the new environment was installed correctly:
    `conda env list`
3.  Activate the new environment:  `conda activate server`
    

## Offline Generation
Generate index files for your dicom data before accessing them through network:<br>
- Generate index file for all datasets in pacs
run `python generateIndexFile.py --pacs_dir=<path-to-your-pacs-directory>`. Make sure that your pacs directory contains a `PACS-Index.xlsx` index file.
- Generate index file for a single dataset
	run `python generateIndexFile.py --dir=<path-to-your-ds-directory>`

## Connect to your server
1. Run server
	run `python3 transServer.py --pacs_dir=<path-to-your-pacs-dir> --pacs_index_path=<path-to-pacs-index-file> --config_dir=<path-to-config-directory> --port=<your-port-num>`. See an exmaple in `serverRun.sh`
	
2. Connect to server
Get your public ip address to use via WAN, or your local ip to use it via LAN.  On your Android app side: enter your ip address and port number to connect.
