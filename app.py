import os, sys

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
    
URL_REPOSITORIO = "http://localhost:9090/files/"
URL_VERSION = "http://localhost:9090/version.txt"


if not AutoUpdate.is_up_to_date():
    



