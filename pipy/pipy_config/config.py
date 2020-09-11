from ..package import package
from ..custom import missing_package


class PipyConfig:

    def __init__(self):
        self.packages_installed = []
        self.packages = {
            'p1': {
              '1.0.0': package.Package('p1', 'description p1', '1.0.0'),
              '1.0.1': package.Package('p1', 'description p1', '1.0.1'),
              '1.0.2': package.Package('p1', 'description p1', '1.0.2'),
            },
            'p2': {
                "1.0.0": package.Package('p2', 'description p2', '1.0.0'),
                "1.0.1": package.Package('p2', 'description p2', '1.0.1', depends=["p1==1.0.0"]),
                "1.0.2": package.Package('p2', 'description p2', '1.0.2'),
            },

            'p3': {
                "1.0.0": package.Package('p3', 'description p3', '1.0.0', depends=["p2==1.0.1"]),
                "1.0.1": package.Package('p3', 'description p3', '1.0.1'),
                "1.0.2": package.Package('p3', 'description p3', '1.0.2'),
            },

            'p4': {
                "1.0.0": package.Package('p4', 'description p4', '1.0.0', depends=["p1==1.0.0", "p3==1.0.0"]),
                "1.0.1": package.Package('p4', 'description p4', '1.0.1')
            }
        }

    # search for package in list
    def search(self, package=None):
        # handle no package name
        if package is None or package == '':
            return "\n".join(self.packages.keys())

        # handle package with version
        if "==" in package:
            (pack_name, pack_version) = package.split(sep="==")
            try:
                return self.packages[pack_name][pack_version]
            except Exception as e:
                raise missing_package.MissingPackage

        # handle package without version
        return "\n".join(self.packages[package].keys())

    def installed(self):
        if len(self.packages_installed) == 0:
            return "No packages installed"

        all_installed = ''
        for p in self.packages_installed:
            all_installed += p.get_name() + "\n"
        return all_installed

    def _install_depends(self, package):
        (pack_name, pack_version) = package.split(sep="==")
        try:
            for dep in self.packages[pack_name][pack_version].get_depends():
                print("DEBUG: Found dependency: " + dep + " in " + pack_name + "==" + pack_version)
                (dep_pack_name, dep_pack_version) = package.split(sep="==")
                dep_pack_obj = self.packages[dep_pack_name][dep_pack_version]
                if dep_pack_obj not in self.packages_installed:
                    self.install(dep)
        except Exception as e:
            raise missing_package.MissingPackage

    # install package and its dependence
    def install(self, package):
        if package is None or package == '':
            raise missing_package.MissingPackage

        (pack_name, pack_version) = package.split(sep="==")
        package_obj = self.packages[pack_name][pack_version]
        if "==" in package:
            if package_obj in self.packages_installed:
                return

            self._install_depends(package)
            try:
                self.packages_installed.append(package_obj)
            except Exception as e:
                raise missing_package.MissingPackage





