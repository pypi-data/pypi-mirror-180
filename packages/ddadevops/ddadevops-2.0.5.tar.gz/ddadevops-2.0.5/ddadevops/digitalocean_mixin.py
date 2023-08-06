from .devops_terraform_build import DevopsTerraformBuild


def add_digitalocean_mixin_config(config, do_api_key, do_s3_id, do_s3_secret):
    config.update({'DigitaloceanMixin':
                   {'do_api_key': do_api_key,
                    'do_s3_id': do_s3_id,
                    'do_s3_secret': do_s3_secret}})
    return config


class DigitaloceanMixin(DevopsTerraformBuild):

    def __init__(self, project, config):
        super().__init__(project, config)
        do_mixin_config = config['DigitaloceanMixin']
        self.do_api_key = do_mixin_config['do_api_key']

    def project_vars(self):
        ret = super().project_vars()
        if self.do_api_key:
            ret['do_api_key'] = self.do_api_key
            ret['do_s3_id'] = self.do_api_key
            ret['do_s3_secret'] = self.do_api_key
        return ret

    def copy_build_resources_from_package(self):
        super().copy_build_resources_from_package()
        self.copy_build_resource_file_from_package('provider_registry.tf')
        self.copy_build_resource_file_from_package('do_provider.tf')
        self.copy_build_resource_file_from_package('do_mixin_vars.tf')
