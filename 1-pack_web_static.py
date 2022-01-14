#!/usr/bin/python3
# Fabric script that generates a .tgz
# archive from the contents of the web_static folder

import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """Create the tar gzipped archive."""
    current_date = datetime.utcnow()
    created_file = f"versions/web_static_{current_date.year}\
        {current_date.month}\
        {current_date.day}\
        {current_date.hour}\
        {current_date.minute}\
        {current_date.second}.tgz"

    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(created_file)).failed is True:
        return None
    return created_file
