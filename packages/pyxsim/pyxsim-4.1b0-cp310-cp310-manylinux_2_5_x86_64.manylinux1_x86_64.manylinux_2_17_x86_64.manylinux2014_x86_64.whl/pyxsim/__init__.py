from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("pyxsim")
except PackageNotFoundError:
    # package is not installed
    pass


from pyxsim.event_list import \
    EventList

from pyxsim.photon_list import \
    make_photons, \
    project_photons, \
    project_photons_allsky

from pyxsim.source_models import \
   CIESourceModel, \
   NEISourceModel, \
   LineSourceModel, \
   PowerLawSourceModel, \
   IGMSourceModel

from pyxsim.utils import merge_files, \
    compute_elem_mass_fraction, \
    create_metal_fields
