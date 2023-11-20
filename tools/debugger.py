#!/bin/bash
from utils.utils import run_command

#Constants declaration
SSH_LOADER_PATH = r'C:\SVN\Automation\Lib\Loader\Adapters\SshLoader.py -i 192.168.0.2 -u root -p scqr!1368 --osType RHEL'

class Debugger():
    
    def __init__(self,image_args) -> None:
        self.tag_name = image_args.tag_name
        self.container_name = image_args.container_name
    
    def check_debugging_env(self) -> bool:
        check_cmd = f'{SSH_LOADER_PATH} -c C:\\ReleaseTool\\ini_files\\check_debugging_env.ini'
        checked_env = run_command(check_cmd)
        if checked_env:
            print('Optimal debugging environment set up. Found: /systemqnr, /SVN, /benchmarks and /systemqnr/Dockerfile for debugging process.')
        else:
            print('Target does not have all the componentes for debugging process.')
            print('Please check you have the following components: \n1./systemqnr\n2./SVN\n3./benchmarks\n4./systemqnr/Dockerfile')
        return checked_env
    
    def set_up_debugging_env(self) -> bool:
        env_enabled = self.check_debugging_env()
        set_up_succesful = True
        if env_enabled:
            base_command = f'{SSH_LOADER_PATH} -c C:\\ReleaseTool\\ini_files\\debug_image.ini'
            release_args = f' -m IMAGE_TAG={self.tag_name} -m CONTAINER_NAME={self.container_name}'
            set_up_succesful = run_command(base_command + release_args)
        elif set_up_succesful is False:
            print('There was an error setting up the debugging environment. Please check logs at C:\\Logs\\Auto\\')
            set_up_succesful = False
        return set_up_succesful