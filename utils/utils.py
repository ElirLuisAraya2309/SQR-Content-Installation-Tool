import subprocess

def run_command(command : str) -> None:
    try:
        print(f'Running command : {command}')
        subprocess.run(command, shell=True, check=True)
        return True
    except Exception as command_error:
        print(f"There was an error processing command: {command}. Description: {command_error}")
        return False