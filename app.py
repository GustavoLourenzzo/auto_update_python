import AutoUpdate, os
from urllib.request import urlopen
from shutil import copyfileobj

URL_REPOSITORIO = "http://localhost:9090/files/"

AutoUpdate.set_url("http://localhost:9090/version.txt")
AutoUpdate.set_current_version("0.0.1")
if not AutoUpdate.is_up_to_date():
    with urlopen(URL_REPOSITORIO) as in_stream, open('ee.txt.zip', 'wb') as out_file:
    #copyfileobj(in_stream, out_file)
        print(out_file)