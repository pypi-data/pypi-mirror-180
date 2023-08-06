from dda_python_terraform import *
from .digitalocean_terraform_build import DigitaloceanTerraformBuild


def add_digitalocean_backend_properties_mixin_config(config, account_name):
    config.update({'DigitaloceanBackendPropertiesMixin':
                   {'account_name': account_name}})
    return config


class DigitaloceanBackendPropertiesMixin(DigitaloceanTerraformBuild):

    def __init__(self, project, config):
        super().__init__(project, config)
        aws_mixin_config = config['DigitaloceanBackendPropertiesMixin']
        self.account_name = aws_mixin_config['account_name']
        self.backend_config = "backend." + self.account_name + "." + self.stage + ".properties"
        self.additional_tfvar_files.append(self.backend_config)

    def project_vars(self):
        ret = super().project_vars()
        ret.update({'account_name': self.account_name})
        return ret

    def copy_build_resources_from_package(self):
        super().copy_build_resources_from_package()
        self.copy_build_resource_file_from_package(
            'do_backend_properties_vars.tf')
        self.copy_build_resource_file_from_package(
            'do_backend_with_properties.tf')

    def copy_local_state(self):
        pass

    def rescue_local_state(self):
        pass

    def init_client(self):
        tf = Terraform(working_dir=self.build_path(), terraform_semantic_version=self.terraform_semantic_version)
        tf.init(backend_config=self.backend_config)
        self.print_terraform_command(tf)
        if self.use_workspace:
            try:
                tf.workspace('select', self.stage)
                self.print_terraform_command(tf)
            except:
                tf.workspace('new', self.stage)
                self.print_terraform_command(tf)
        return tf
