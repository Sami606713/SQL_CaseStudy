import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO)

project_name="SQL_Case_Study"

list_of_file=[
    "setup.py",
    'requirements.txt',
    "Dockerfile",
    'app.py',
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/utils.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_case_study.py",    
]

for file_path in list_of_file:
    file_path=Path(file_path)

    # print(os.path.split(file_path))
    file_dir,file_name=os.path.split(file_path)

    if(file_dir and not os.path.isdir(file_dir)):
        logging.info(f"Creating Directory {file_dir}")
        os.makedirs(file_dir,exist_ok=True)
    elif(not os.path.isfile(file_path) ):
        with open(file_path,"w") as f:
            pass
            logging.info(f"Creating the empty file{file_path}")
    else:
        logging.info(f"{file_path} already exist")
