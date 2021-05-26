from typing import ClassVar
import urllib.request as urlopen, urllib.parse as urlparse, urllib.error as urlerror
import os, abc



class Updated(abc.ABC):
    def __init__(self, url, version = None, url_version = None):
        self.URL_REPOSITORIO = url
        self.__setVersion(version)
        self.setUrlFileVersion(url_version)
        pass
    
    
    def isNotLastVersion(self):
        return not(self.version + "\n" == self.getLastVersion())
    
    #seta a url do arquivo onde sera consultado a versao atual
    def setUrlFileVersion(self, url):
        if (url is None) or (not isinstance(url, str)):
            self.URL_VERSION_FILE = self.URL_REPOSITORIO+os.sep+"version.txt"
        else:
            self.URL_VERSION_FILE = url

    
    #retorna as linhas contidas no arquivo
    def getLastVersion(self):
        file = urlopen.urlopen(self.URL_VERSION_FILE)
        lines = ""
        for line in file:
            lines += line.decode("utf-8")
        return lines
    
    #metodo privado para setar a versao do prog
    def __setVersion(self, version):
        if (version is None) or (not isinstance(version, str)):
            self.version = "0.0.1"
        else:
            self.version = version
        pass
    
    #seta a versao corrente do app
    def setCurrentVersion(self, version):
        self.__setVersion(version)
    
    
    #metodo abstrato para fazer download de um arquivo, por padrao ele utiliza o metodo padrao de download
    #pode ser reescrito utilizando chaves de repositorios sem alterar o funcionamento normal da classe
    @abc.abstractmethod
    def downloadFile(self, nameFile):
        try:
            urlopen.urlretrieve(self.URL_REPOSITORIO+os.sep+nameFile, nameFile)
            print("Arquivo baixado com sucesso")
        except urlerror:
            print("deu erro HTTP")
        except Exception:
            print("deu erro")
    
    #metodo abstrato para fazer download de uma lista de arquivo, por padrao ele utiliza o metodo padrao de download
    #pode ser reescrito utilizando chaves de repositorios sem alterar o funcionamento normal da classe
    @abc.abstractmethod
    def downloadFiles(self, *kargs):
        for file in kargs:
            try:
                urlopen.urlretrieve(self.URL_REPOSITORIO+os.sep+file, file)
                print("O arquivo "+file+" foi baixado com sucesso")
            except urlerror:
                print("Deu erro HTTP no arquivo "+ file)
            except Exception:
                print("Deu erro no arquivo "+ file)
        print("Download finalizado")