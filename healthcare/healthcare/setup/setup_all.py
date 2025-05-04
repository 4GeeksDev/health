from healthcare.setup import setup_healthcare
from healthcare.module_profile_setup.setup_module_profiles import setup_module_profiles


def setup_all():
    setup_healthcare()
    setup_module_profiles()
