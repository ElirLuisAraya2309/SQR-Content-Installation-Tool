from argparse import ArgumentParser

class ReleaseTool:
    
    def __init__(self) -> None:
        self.parser = ArgumentParser(description="System Q&R Content Installation and Release Tool")
        self.parser.add_argument("--mode", '-m', choices=['release', 'install', 'debug', 'express'], default='debug', help="Mode of the app: Release, install or debug env.")
        self.parser.add_argument("--activity", '-a', choices=['FACR', 'Qual', 'Testing', 'Content'], default='Testing', help="Activity the content will be used for.")
        self.parser.add_argument("--product", '-p',type=str, default=None, help="Codename of the Intel product.")
        self.parser.add_argument("--chop", '-c',type=str, default=None, help="Chop of the Intel product family.")
        self.parser.add_argument("--tag-name",type=str,default=None,help="Tag name of the release to be created. NO UPPERCASE ALLOWED. Mandatory for debug.")
        self.parser.add_argument("--content-name",type=str,default=None,help="Content name. Used when uploading existing containers for content")
        
        #Release Options
        self.release_group = self.parser.add_argument_group('Release Options')
        self.release_group.add_argument("--docker-env",type=str,default=None,help="Name of the docker file to use. Mandatory for debug.")
        
        #Installation Options
        self.install_group = self.parser.add_argument_group('Installation Options')
        self.install_group.add_argument("--container-name",type=str,default=None,help="Name of the docker container.")
        
        #Quick options
        self.quick_group = self.parser.add_argument_group('Express Use Options')
        self.quick_group.add_argument("--compress-path",type=str,default=None,help="Output path file where the selected docker image is going to be compressed. Use it along with '--tag-name' option")
        
    def parse_args(self):
        return self.parser.parse_args()