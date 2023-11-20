# !/bin/bash
# Python Imports
import time
#Local Imports
from release_tool import ReleaseTool
from tools.creator import Creator
from tools.installator import Installator
from tools.debugger import Debugger

if __name__ == "__main__":
    release_tool_parser = ReleaseTool()
    tool_args = release_tool_parser.parse_args()
    init_time_stamp = time.time()
    if tool_args.mode == 'release':
        image_creator = Creator(tool_args)
        image_creator.create_release()
        
    elif tool_args.mode == 'install':
        print('Install content image option')
        image_installator = Installator(tool_args)
        image_installator.generate_installer()
    
    elif tool_args.mode == 'debug':
        image_debugger = Debugger(tool_args)
        image_debugger.set_up_debugging_env()
    else:
        print('Please specify a valid mode. Modes: release, install, debug.')
    final_time = int(time.time() - init_time_stamp)
    print(f'Process took: {final_time} seconds. Minutes {final_time / 60}')
    