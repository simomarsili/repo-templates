"""kagtools package."""
import os
import pkg_resources

SEP = os.path.sep
package_path = os.path.dirname(os.path.abspath(__file__))
package_name = package_path.split(SEP)[-1]
__version__ = pkg_resources.require(package_name)[0].version
