"""
Update Rollout Manager API [URM-API]

A Decentralized Package Manager.
Made by NoKodaAddictions, NoKoda
"""

from json import JSONDecodeError, dump, load
from os import makedirs
from os import name as platform
from os import remove, removedirs, rmdir, scandir, system
from os.path import dirname, exists, join
from uuid import UUID, uuid4
from subprocess import Popen
from requests import RequestException, Response, get
from termcolor import colored

__version__ = "1.2"
__accepted_versions__ = [
    "1.2"
]
__directory__ = dirname(__file__)

class Exceptions:
    """
    Exceptions class
    """
    class FragmentedInstallationWarning(Warning):
        """
        Raised if
        - The package is not installed correctly
        - Files were not created properly
        """
        
    class DeprecatedPackageWarning(Warning):
        """
        Raised if
        - The package is no longer supported by the author/vendor
        """

    class UnsupportedPackageError(Exception):
        """
        Raised if 
        - The package config versions do not match the URM-API version
        """
    
    class PackageConfigError(Exception):
        """
        Raised if
        - The package could not be read correctly
        - The package config is missing essential data
        """

    class UninstalledPackageError(PackageConfigError):
        """
        Raised if
        - The package is not installed
        """
        
class Ledger:
    """
    Manages the ledger JSON file.
    """
    
    ledger:dict = None
    location:str = None
    
    def __init__(self):
        self.location = join(__directory__, "ledger.json")
        try:
            with open(self.location, 'r', encoding="utf8") as r:
                self.ledger = load(r)
        
        except FileNotFoundError:
            self.ledger = {}
            self.implement()

        except JSONDecodeError:
            self.ledger = {}
            self.implement()

    def search_id(self, uuid:str=None) -> str:
        """
        Returns the package information for the given UUID

        :param: uuid: string
        
        if found
        :return: string, dict

        if not found
        :return: None, None
        """

        if uuid is not None:
            for package in self.ledger:
                if package == uuid:
                    return package, self.ledger[package]

            return None, None

        else:
            raise TypeError("UUID not specified.")

    def search_name(self, name:str=None) -> dict:
        """
        Returns the package information for the given name

        :param: name: string
        
        if found
        :return: string, dict

        if not found
        :return: None, None
        """
        if name is not None:
            for package in self.ledger:
                if self.ledger[package]["name"] == name:
                    return package, self.ledger[package]

            return None, None

        else:
            raise TypeError("Name not specified.")
            
    def add(self, name:str=None, location:str=None, version:str=None) -> None:
        """
        Adds package information to ledger JSON file

        :param: name: string
        :param: location: string
        :param: version: string

        :return: None
        """
        if name is None or location is None or version is None:
            raise TypeError("Some parameters are None.")
        
        else:
            generated = False

            while not generated:
                uuid = str(uuid4())

                if uuid in self.ledger:
                    pass
                else:
                    generated = True
                    
            self.ledger.update({
                uuid:{
                    "name":name,
                    "location":location,
                    "version":version, #URMAPI version this was installed in, not the package version
                }
            })
        
        self.implement()

    def remove(self, uuid:str=None) -> None:
        """
        Removes package information from ledger JSON file

        :param: uuid: string

        :return: None
        """
        self.ledger.pop(uuid)
        self.implement()

    def replace(self, uuid:str=None, name:str=None, location:str=None, version:str=None) -> None:
        """
        Replaces package information in ledger JSON file

        :param: uuid: string
        :param: name: string
        :param: location: string
        :param: version: string

        :return: None
        """
        if uuid is None or name is None or location is None or version is None:
            raise TypeError("Some parameters are None.")

        else:
            self.ledger.update({
                uuid:{
                    "name":name,
                    "location":location,
                    "version":version #URMAPI version this was installed in, not the package version
                }
            })
        
            self.implement()

    def scan(self) -> None:
        """
        Verifies that all packages in the ledger are installed

        :return: None
        """
        for package_id, package_data in self.ledger.copy().items():
            print(f"{package_data['name']} Scanning...")
            
            if exists(package_data["location"]) and exists(join(package_data["location"], "config.urmapi.json")):
                print(colored(f"{package_data['name']}: Exists", "green"))

            else:
                print(colored(f"{package_data['name']}: Could not be found. Removing...", "red"))
                self.remove(package_id)

        print("Scan completed. Implementing changes...")
        self.implement()

    def implement(self) -> None:
        """
        Updates the ledger JSON file

        :return: None
        """
        with open(join(__directory__, "ledger.json"), 'w', encoding="utf8") as w:
            dump(self.ledger, w, indent=4)

class API:
    """
    Main class for fetching and downloading packages.
    """
    server:str = None
    config:str = None
    response:Response = None
    location:str = None
    success:int = None
    fails:int = None
    
    package_data:dict = None
    package_name:str = None
    package_version:str = None
    package_config_version:str = None
    package_server:str = None
    package_license:str = None
    package_license_description:str = None
    package_license_url:str = None
    package_authors:list = None
    package_os_support:list = None
    package_keywords:list = None
    package_install_message:str = None
    package_vendor_name:str = None
    package_vendor_email:str = None
    package_vendor_phone:str = None
    package_start_file_after_install:str = None
    package_deprecated:bool = None
    
    package_content_install:dict = None
    package_content_delete:dict = None
    
    package_data_old:str = None
    package_name_old:str = None
    package_version_old:str = None
    package_config_version_old:str = None
    package_server_old:str = None    
    
    ledger:Ledger = Ledger()

    def __init__(self, server:str=None, config:str=None):
        self.server = server
        self.config = config
        
        if self.server is None:
            if self.config is None:
                raise TypeError("Please specify a link or config.urmapi.json file.")
                
            else:
                with open(config, 'r', encoding="utf8") as r:
                    self.package_data_old = load(r)
                    self.package_name_old = self.package_data_old["HEAD"]["package"]["name"]
                    self.package_version_old = self.package_data_old["HEAD"]["package"]["version"]
                    self.package_config_version_old = self.package_data_old["HEAD"]["config"]["version"]
                    self.package_server_old = self.package_data_old["HEAD"]["package"]["package_url"]
                    
                    self.response = get(f"{self.package_server_old}/config.urmapi.json", timeout=10)
                    self.location = dirname(self.config)
                
        else:
            self.response = get(f"{self.server}/config.urmapi.json", timeout=10)
                
        
        if self.response.status_code != 200:
            raise RequestException(f"Error: {self.response.status_code}")

        else:
            self.package_data = self.response.json()
            self.package_name = self.package_data["HEAD"]["package"]["name"]
            self.package_version = self.package_data["HEAD"]["package"]["version"]
            self.package_config_version = self.package_data["HEAD"]["config"]["version"]
            self.package_server = self.package_data["HEAD"]["package"]["package_url"]
            self.package_os_support = self.package_data["HEAD"]["package"]["os_support"]
            self.package_deprecated = self.package_data["HEAD"]["package"]["deprecated"]
            self.package_license = self.package_data["HEAD"]["package"]["license"]
            self.package_license_description = self.package_data["HEAD"]["package"]["license_description"]
            self.package_license_url = self.package_data["HEAD"]["package"]["license_url"]
            self.package_authors = self.package_data["HEAD"]["package"]["authors"]
            self.package_keywords = self.package_data["HEAD"]["package"]["keywords"]
            self.package_install_message = self.package_data["HEAD"]["package"]["install_message"]
            self.package_vendor_name = self.package_data["HEAD"]["package"]["vendor_name"]
            self.package_vendor_email = self.package_data["HEAD"]["package"]["vendor_email"]
            self.package_vendor_phone = self.package_data["HEAD"]["package"]["vendor_phone"]
            self.package_start_file_after_install = self.package_data["HEAD"]["package"]["start_file_after_install"]
            
            self.package_content_install = self.package_data["CONTENT"]["install"]
            self.package_content_delete = self.package_data["CONTENT"]["delete"]
            

    def is_installed(self) -> bool:
        """
        Checks if package is already installed.

        :return: bool
        """
        package_id = self.ledger.search_name(self.package_name)[0]

        if package_id is not None:
            return True
        
        return False
            
    def is_compatible(self) -> bool:
        """
        Checks compatibility between packages, before installing or updating.

        :return: bool
        """
        try:
            if self.package_deprecated:
                assert Exceptions.DeprecatedPackageWarning("This package is reported to be deprecated.")
        except KeyError:
            pass

        if self.package_config_version in __accepted_versions__:
            for oss in self.package_os_support:
                if oss in Build.accepted_os:
                    if platform in self.package_os_support:
                        return True
        
        return False
    
    def validate_package(self) -> bool:
        """
        Ensures that package has installed or updated correctly

        :return: bool
        """
        self.success = 0
        self.fails = 0

        for file, path in self.package_content_install.items():
            if path != "here":
                if exists(join(path, file)):
                    self.success+=1

                else:
                    self.fails+=1
            else:
                if exists(join(self.location, file)):
                    self.success+=1

                else:
                    self.fails+=1
                    
        if self.fails == 0 and self.success == len(self.package_content_install):
            return True

        else:
            return False

    def download(self, file:str=None, location:str=None) -> None:
        """
        Fetches file, and downloads to specified directory

        :param: file: string
        :param: location: string

        :return: None
        """
        if file is not None and location is not None:
            print(f"{file}: Fetching...")
            print(f"{file}, {location}")
            
            frs = get(f"{self.package_server}/{file}", timeout=10)
            
            if frs.status_code == 200:
                print(colored(f"{file}: Downloading...", "green"))
                path = dirname(file)
                if location != "here":
                    if path != "":
                        try:
                            makedirs(join(location, path))
                        except FileExistsError:
                            pass

                    with open(join(location, file), "wb") as w:
                        w.write(frs.content)
                else:
                    if path != "":
                        try:
                            makedirs(join(self.location, path))
                        except FileExistsError:
                            pass
                    with open(join(self.location, file), "wb") as w:
                        w.write(frs.content)
            else:
                print(colored(f"{file}: Could not fetch", "red"))
    
    def delete(self, file:str=None, location:str=None) -> None:
        """
        Deletes a file in a specified directory

        :param: file: string
        :param: location: string

        :return: None
        """
        
        if file is not None and location is not None:
            print(f"{file}: Deleting...")
            if location != "here":
                try:
                    remove(join(location, file))
                    path = dirname(file)
                    if path != "":
                        removedirs(join(location, path))
                except FileNotFoundError:
                    print(colored(f"{file}: Could not delete", "red"))
                
                else:
                    print(colored(f"{file}: Deleted", "green"))
                
            else:
                try:
                    remove(join(self.location, file))
                    path = dirname(file)
                    if path != "":
                        removedirs(join(self.location, path))
                except FileNotFoundError:
                    print(colored(f"{file}: Could not delete", "red"))
                
                else:
                    print(colored(f"{file}: Deleted", "green"))

        else:
            raise TypeError("Please specify file name and location.")

    def install(self, location:str=None) -> None:
        """
        Installs the files from the server

        :param: location: string

        :return: None
        """

        if self.is_installed():
            print(f"{self.package_name}: Package is already installed.")
        
        else:
            print(f"{self.package_name}: Checking compatibility...")
            if self.is_compatible():
                print(colored(f"{self.package_name}: Package is compatible", "green"))

                try:
                    if self.package_install_message != "":
                        print(f"{self.package_name}: Now, a message from this package's creator.")
                        print(self.package_install_message)

                except KeyError:
                    pass

                print(f"{self.package_name}: Creating package folder...")
                if location is not None:
                    try:
                        makedirs(join(location, self.package_name))
                    except FileExistsError:
                        pass

                    self.location = join(location, self.package_name)

                else:
                    raise TypeError("Package install location is required.")

                print(f"{self.package_name}: Downloading package...")
                self.package_content_install.update({"config.urmapi.json":"here"})
                
                for file, install in self.package_data["CONTENT"]["install"].items():
                    self.download(file, install)

                print(f"{self.package_name}: Validating package...")
                if self.validate_package():
                    print(f"{self.package_name}: Package validated. Successfully installed package")
                
                else:
                    assert Exceptions.FragmentedInstallationWarning(f"{self.package_name_old}: Fragmented package installation")

                
                print("Updating Ledger...")
                ledger = Ledger()
                
                ledger.add(name=self.package_name, location=self.location, version=__version__)
                
                print(colored(f"{self.package_name}: Done!"))

            else:
                raise Exceptions.UnsupportedPackageError(f"{self.package_name}: Package is not compatible. Please check the config version and os support. URM-API supports: {__accepted_versions__}")
    
    def uninstall(self) -> None:
        """
        Uninstalls the package

        :return: None
        """
        
        if self.is_installed():
            print(f"{self.package_name}: Uninstalling package...")

            print(f"{self.package_name_old}: Reading files...")
            self.package_content_install.update({"config.urmapi.json":"here"})
            for file, path in self.package_content_install.items():
                self.delete(file, path)
                
            rmdir(join(self.location))

            print(f"{self.package_name_old}: Verifying uninstallation...")
            if not self.validate_package():
                if self.fails == len(self.package_content_install):
                    print(f"{self.package_name_old}: Successfuly uninstalled package")

            print(f"{self.package_name_old}: Updating ledger...")
            self.ledger.remove(self.ledger.search_name(self.package_name)[0])

            print(f"{self.package_name_old}: Done!")

        else:
            raise Exceptions.UninstalledPackageError(f"{self.package_name_old}: Package is not installed")

    def update(self) -> None:
        """
        Compares versions, makes neccessary changes.

        :return: None
        """
        
        if self.package_data_old is not None:
            ledger = Ledger()
            package_id, package_info = ledger.search_name(self.package_name_old)

            if package_id is not None:
                print(colored(f"{self.package_name_old}: Package is verified to be installed", "green"))
                location = package_info["location"]

                if self.package_version_old != self.package_version:
                    print(colored(f"{self.package_name_old}: Update is available"), "green")

                    print(f"{self.package_name}: Checking compatibility...")
                    if self.package_data["HEAD"]["config"]["version"] in __accepted_versions__:
                        print(colored(f"{self.package_name_old}: Package is compatible", "green"))

                        self.location = self.ledger.search_name(self.package_name)[1]["location"]

                        print(f"{self.package_name_old}: Reading steps...")
                        print(f"{self.package_name_old}: Installing/Updating files...")
                        for file, install in self.package_data["CONTENT"]["install"].items():
                            self.download(file, install)

                        print(f"{self.package_name_old}: Removing files...")
                        for file, delete in self.package_data["CONTENT"]["delete"].items():
                            self.delete(file, delete)
                        
                        print(f"{self.package_name}: Updating config.urmapi.json...")
                        with open(join(location, "config.urmapi.json"), "w", encoding="utf8") as w:
                            dump(self.package_data, w, indent=4)
                            
                        print(f"{self.package_name}: Validating package...")
                        if self.validate_package():
                            print(f"{self.package_name}: Package validated. Successfully updated package")
                        
                        else:
                            assert Exceptions.FragmentedInstallationWarning(f"{self.package_name_old}: Fragmented package installation")

                        print(f"{self.package_name}: Updating ledger...")
                        ledger.replace(package_id, self.package_name, location, __version__)

                        print(f"{self.package_name}: Finished")

                    else:
                        raise Exceptions.UnsupportedPackageError(f"{self.package_name_old}: Package versions do not match. This version of URM-API supports {__accepted_versions__}")

                    
                else:
                    print(f"{self.package_name_old}: Is up to date.")
            else:
                raise Exceptions.UninstalledPackageError("Package is not installed. Installed this package first before updating")        
        else:
            raise TypeError("Update function requires a config.urmapi.json file.")

class Build:
    """
    Builds the config.urmapi.json file for your package
    """
    
    package_data:dict = {}    
    accepted_os:list = ["nt", "posix", "linux"]
    
    def __init__(self):
        return
    
    def setup(self,
    name:str,
    version:str,
    authors:list,
    package_url:str,
    os_support:list=accepted_os,
    force_os_support:bool = False,
    description:str = None,
    license:str = None,
    license_description:str = None,
    license_url:str = None,
    vendor_name:str = None,
    vendor_email:str = None,
    vendor_phone:str = None,
    keywords:list = None,
    install_message:str = None,
    start_file_after_install:str = None,
    deprecated:bool = False
    ):
        if os_support in self.accepted_os or force_os_support:
            self.package_data = {
            "HEAD":{
                "package":{
                    "name":name,
                    "version":version,
                    "description":description,
                    "license":license,
                    "license_description":license_description,
                    "license_url":license_url,
                    "authors":authors,
                    "package_url":package_url,
                    "os_support":os_support,
                    "keywords":keywords,
                    "install_message":install_message,
                    "vendor_name":vendor_name,
                    "vendor_email":vendor_email,
                    "vendor_phone":vendor_phone,
                    "start_file_after_install":start_file_after_install,
                    "deprecated":deprecated
                },
                "config":{
                    "version":__version__
                }
            },
            "CONTENT":{
                "install":{
                },
                "delete":{
                }
            }
        }
            
        else:
            raise OSError("Specified OS not accepted. To force accept, set force_os_support to True")
    
        
    def scan(self, folder:str, path:str="here"):
        for file in scandir(folder):
            self.package_data["CONTENT"]["install"].update({file.path: path})
    
    def modify(self, file:str, path:str):
        self.package_data["CONTENT"]["install"].update({file: path})