"""
Metaibricks package : MetAIBricks is a package that allows you to easily train a neural
network, by providing the basic development bricks you may need.
"""
from metaibricks._version import __version__
from metaibricks.settings import CLI, Logger, Settings
from metaibricks.extraction import FTPSession, FTPFiles, FTPDir
from metaibricks.extraction.http import HTTPSession, HTTPFiles, HTTPDir
from metaibricks.pipeline import Pipeline

__all__ = [
    "__version__",
    "CLI",
    "Logger",
    "Settings",
    "FTPSession",
    "FTPFiles",
    "FTPDir",
    "Pipeline",
    "HTTPSession",
    "HTTPFiles",
    "HTTPDir",
]
