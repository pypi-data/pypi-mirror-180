# Imports
import os
import sys
import uuid
import time
import socket
import argparse
import threading
import subprocess
import logging
import nbformat as nbf


def validate_path(datadir,destfolder):
    destfolder = destfolder.strip("/")
    subfolders = destfolder.split('/')
    if(len(subfolders)>1):
        current_dir = datadir
        for subfolder in subfolders:
            current_dir = os.path.join(current_dir, subfolder)
            if not os.path.exists(current_dir):
                os.makedirs(current_dir)

####---from mpi4py import MPI
def createCopyDataNotebook(fname,folders):
    nb = nbf.v4.new_notebook()
    text = """\
# Copy Required Data from Datastore."""
    code1 = """\
import azureml.core
from azureml.core import Workspace, Datastore

ws = Workspace.from_config()
datastore = ws.get_default_datastore()"""

    code_entries = ["datastore.download('./', '{0}', overwrite=False, show_progress=True)".format(x) for x in folders] 
    
    nb['cells'] = [nbf.v4.new_markdown_cell(text),
               nbf.v4.new_code_cell(code1)]
    
    nb['cells'].extend([nbf.v4.new_code_cell(code) for code in code_entries])
    
    with open(fname, 'w') as f:
        nbf.write(nb, f)

def createUploadDataNotebook(fname,folder):
    nb = nbf.v4.new_notebook()
    text = """\
# Upload Data to Datastore."""
    code1 = """\
import azureml.core
from azureml.core import Workspace, Datastore

ws = Workspace.from_config()
datastore = ws.get_default_datastore()"""

    nb['cells'] = [nbf.v4.new_markdown_cell(text),
               nbf.v4.new_code_cell(code1)]
    
    nb['cells'].append(nbf.v4.new_code_cell("datastore.upload('./', '{0}', overwrite=False, show_progress=True)".format(folder)))

    with open(fname, 'w') as f:
        nbf.write(nb, f)

def install(package,upgrade=False):
    if upgrade:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package,"--upgrade"])
    else:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def flush(proc, proc_log):
    while True:
        proc_out = proc.stdout.readline()
        if proc_out == "" and proc.poll() is not None:
            proc_log.close()
            break
        elif proc_out:
            sys.stdout.write(proc_out)
            proc_log.write(proc_out)
            proc_log.flush()

def evaluate_cmd(cmd, logFileName):
    cmd_log = open(logFileName, "a")
    cmd_proc = subprocess.Popen(
        cmd.split(),
        universal_newlines=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )

    cmd_flush = threading.Thread(target=flush, args=(cmd_proc, cmd_log))
    cmd_flush.start()
    flush(cmd_proc, cmd_log)
    return cmd_proc

def mount(dataset,mnt_root,rel_mnt_path):
    mounted_path = os.path.join(mnt_root,rel_mnt_path)
    mount_context = dataset.mount(mounted_path)
    mount_context.start()
    return mounted_path

if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    install("azureml-sdk")
    install("notebook")

    from azureml.core import Run
    from notebook.notebookapp import list_running_servers

    ### PARSE ARGUMENTS
    parser = argparse.ArgumentParser()
    parser.add_argument("--jupyter_token", default=uuid.uuid1().hex)
    parser.add_argument("--jupyter_port", default=8888)
    parser.add_argument("--use_gpu", default=False)
    parser.add_argument("--n_gpus_per_node", default=0)
    parser.add_argument('--output_path', dest='output_path', required=True)
    parser.add_argument('--ws_config', dest='ws_config', required=True)
    parser.add_argument('--folders', dest='folders', required=True)
    args, unparsed = parser.parse_known_args()

    ### CONFIGURE GPU RUN
    GPU_run = args.use_gpu

    if GPU_run:
        n_gpus_per_node = eval(args.n_gpus_per_node)

    ip = socket.gethostbyname(socket.gethostname())

    data = {
        "jupyter": ip + ":" + str(args.jupyter_port),
        "token": args.jupyter_token,
    }

    jupyter = data["jupyter"]
    token = data["token"]

    logger.debug("- args: ", args)
    logger.debug("- unparsed: ", unparsed)
    logger.debug("- my ip is ", ip)

    ####---# if rank == 0:
    running_jupyter_servers = list(list_running_servers())
    logger.debug("- running jupyter servers", running_jupyter_servers)

    ### if any jupyter processes running
    ### KILL'EM ALL!!!
    if len(running_jupyter_servers) > 0:
        for server in running_jupyter_servers:
            os.system(f'kill {server["pid"]}')

    ### RECORD LOGS
    run = Run.get_context()

    run.log("jupyter", jupyter)
    run.log("token", token)

    workspace_name = run.experiment.workspace.name.lower()
    run_id = run.get_details()["runId"]

    #mount_point = f"/mnt/batch/tasks/shared/LS_root/jobs/{workspace_name}/azureml/{run_id.lower()}/mounts/"
    mount_point = os.path.dirname(args.output_path)
    os.makedirs(mount_point, exist_ok=True)
    print("mount_point : " + mount_point)

    cmd = (
        f" jupyter lab --ip 0.0.0.0 --port {args.jupyter_port}"
        f" --NotebookApp.token={token}"
    )
    cmd += f" --notebook-dir={mount_point}"
    cmd += f" --allow-root --no-browser"

    jupyter_log = open("jupyter_log.txt", "a")
    jupyter_proc = subprocess.Popen(
        cmd.split(),
        universal_newlines=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    
    f = open(os.path.join(mount_point, "config.json"), "w")
    f.write(args.ws_config)
    f.close()

    fname = os.path.join(mount_point, 'CopyData.ipynb')
    folders = args.folders.split()
    createCopyDataNotebook(fname,folders)

    for folder in folders:
        validate_path(mount_point,folder)
        fname = os.path.join(mount_point, folder)
        f = open(os.path.join(fname,"config.json"), "w")
        f.write(args.ws_config)
        f.close()
        fname = os.path.join(fname, 'UploadData.ipynb')
        createUploadDataNotebook(fname,folder)
    
    #datastore = run.experiment.workspace.get_default_datastore()
    #rel_datastore_path = "clara"
    #datastore_paths = [(datastore, rel_datastore_path)]
    #dataset = Dataset.File.from_files(path=datastore_paths)
    #print("Mounting " + rel_datastore_path + " on " + mount_point)
    #mount(dataset,mount_point,rel_datastore_path)

    jupyter_flush = threading.Thread(target=flush, args=(jupyter_proc, jupyter_log))
    jupyter_flush.start()

    while not list(list_running_servers()):
        time.sleep(5)

    jupyter_servers = list(list_running_servers())
    assert len(jupyter_servers) == 1, "more than one jupyter server is running"

    flush(jupyter_proc, jupyter_log)

    if jupyter_proc:
        jupyter_proc.kill()

    run.complete()
    run.cancel()
