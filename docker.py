import click
import shutil
import os
import subprocess
from git import Repo
from cyverse_ez import ez_modules
from cyverse_ez import debug_msg
from cyverse_ez import echo_msg
from cyverse_ez import EZ_ROOT_DIR

MODULE_NAME='cyverse_ez_docker'
MODULE_REPO='https://github.com/cyverse/cyverse-ez-docker.git'

@click.command('docker',short_help='docker installation')
def ezmodule():
    global EZ_ROOT_DIR

    debug_msg('start docker.ezmodule()')

    module_path = os.path.join(EZ_ROOT_DIR, MODULE_NAME)
    
    debug_msg('\tcreating EZ_ROOT_DIR, if necessary')
    subprocess.call ('/usr/bin/sudo /bin/mkdir -p -m 0777 ' + EZ_ROOT_DIR, shell=True)

    if not os.path.exists(module_path):
        debug_msg("\t" + module_path + " does not exist, cloning repo " + MODULE_REPO)
        Repo.clone_from (MODULE_REPO, module_path)
    else:
      debug_msg("\t" + module_path + " already exists")

    debug_msg('\tcalling ansible-pull')

    debug_msg('end docker.ezmodule()')
