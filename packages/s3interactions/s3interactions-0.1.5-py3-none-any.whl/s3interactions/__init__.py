import pkg_resources

# Fetches the version of the package as defined in pyproject.toml
__version__ = pkg_resources.get_distribution("your_package").version
