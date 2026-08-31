"""
Schema for repo-tools-data.
"""

from importlib.metadata import PackageNotFoundError, version

from .repo_tools_data_schema import validate_orgs, validate_salesforce_export

try:
    __version__ = version("repo-tools-data-schema")
except PackageNotFoundError:
    __version__ = "unknown"
