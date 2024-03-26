#!/bin/bash
from utils.utils import run_command
from tools.image import Image

WINSCP_PATH = r'C:\SVN\Automation\Externals\WinScp\SftpGet.bat'
SSH_LOADER_PATH = r'C:\SVN\Automation\Lib\Loader\Adapters\SshLoader.py -i 192.168.0.2 -u root -p scqr!1368 --osType RHEL'
class Creator(Image):
    
    def __init__(self, image_args)->None:
        super().__init__(image_args)
        self.docker_env = image_args.docker_env
    
    def document_release(self) -> None:
        pass
        
        
    def get_benchmarks_doc(self):
        pass
        
    def create_release(self) -> None:
        base_command = f'{SSH_LOADER_PATH} -c C:\\SQR-Content-Installation-Tool\\ini_files\\create_target_image.ini'
        release_args = f' -m IMAGE_TAG={self.tag} -m IMAGE_CONFIG={self.docker_env} -m ACTIVITY={self.activity} -m PRODUCT={self.product} -m CHOP={self.chop}'
        run_command(base_command + release_args)