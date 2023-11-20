from tools.image import Image
BOOTSTRAP_DISK = r'\\amr.corp.intel.com\ec\proj\mpe\systemqnr\bootstrap\Tasks\install_docker_content_scripts'
class Installator(Image):
    
    def __init__(self,image_args) -> None:
        super().__init__(image_args)
        self.container_name = image_args.container_name
    
    def generate_installer(self) -> None:
        new_installer_info = open('ini_files\\install_image.ini','r').read()
        #Start replacing values
        replacement_dict = {
            r'{IMAGE_TAG}': self.tag,
            r'{ACTIVITY}': self.activity,
            r'{PRODUCT}': self.product,
            r'{CHOP}': self.chop,
            r'{CONTAINER_NAME}': self.container_name,
            r'{USER}': 'lab_qrsyslab',
            r'{PASSWORD}': '1qnr!1368'
        }
        # Realiza las sustituciones en el texto
        for key, value in replacement_dict.items():
            new_installer_info = new_installer_info.replace(key, value)
        ini_name = f'{BOOTSTRAP_DISK}\\install_{self.activity}_{self.product}_{self.tag}.ini'
        new_installer_file = open(ini_name,'w')
        new_installer_file.write(new_installer_info)
        new_installer_file.close()
        print(f'Ini file created: {ini_name}')