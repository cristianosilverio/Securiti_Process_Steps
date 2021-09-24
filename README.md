# Securiti_Process_Steps
This repository is intended to build automation code to Privacy OPerations using Securiti platform.
We're going to read API authorization variables from **tenant.cfg** file, so we can choose different tenants and interact with them
After that, we're going to list ID and names of all configured processess and save them on **processes.csv** file
We also need to list ID, type and names of assets, vendors and institutions, and save them on assets.lst
We 're going to create a CSV (manually at first) to cross reference processes and assets. It's going to be named process_steps.csv
Then we go throuhg the CSV patching the processes on Securiti


When filling up **processes.csv**, use the following reference for stage and scope fields:

Value   Stage            Scope
0       Collection       Data Subject
1       Processing       Internal 
2       Storage          External
3       Exchange
4       Archival

This script relies in getting a table_id for each process. In order to do that, you need to set a process element with "Data Subject" as Source, any asset as Asset and "Document" as destination for each process.
