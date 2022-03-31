# We must import all submodules here so that they are loaded and plugins are registered.
from . import (
    basic,
    docker,
    form_example,
    from_folder,
    tcp_server,
    web_server,
    knights_and_knaves,
    enigma,
)
__all__ = [
    "basic",
    "docker",
    "form_example",
    "from_folder",
    "tcp_server",
    "web_server",
    "knights_and_knaves",
    "enigma",
]
