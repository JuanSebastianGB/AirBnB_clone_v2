#!/usr/bin/python3
""" Fabric script that generates a .tgz
archive from the contents of the web_static folder
"""

import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """Create the tar gzipped archive."""
    current_date = datetime.now().strftime("%Y%m%d%H%M%S")
    created_file = "versions/web_static_{}.tgz".format(current_date)

    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(created_file)).failed is True:
        return None
    return created_file
