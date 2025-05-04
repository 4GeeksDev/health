from ..module_profile_setup.setup_module_profiles import setup_module_profiles
from ..setup import setup_healthcare


def setup_all():
    setup_healthcare()
    setup_module_profiles()
