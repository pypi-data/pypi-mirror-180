import os
import subprocess
from subprocess import Popen, PIPE
from pathlib import Path
from mstk import logger
from mstk.errors import SchedulerError
from . import Slurm


class RemoteSlurm(Slurm):
    '''
    Slurm job scheduler running on a remote machine.

    Parameters
    ----------
    queue : str
        The jobs will be submitted to this partition.
    n_proc : int
        The CPU cores a job can use.
    n_gpu : int
        The GPU card a job can use.
    host : str
        The IP address of the remote host that is running Slurm
    username : str
        The username for logging in the remote host
    remote_dir : str
        The default directory to use on the remote host for running calculation
    port : int
        The SSH port for logging in the remote host
    n_node : int
        The nodes a job can use. If 0, then will be decided by slurm.
    env_cmd : str, Optional
        The commands for setting up the environment before running real calculations.
        It will be inserted on the top of job scripts.

    Attributes
    ----------
    queue : str
        The jobs will be submitted on this queue.
    n_proc : int
        The CPU cores a job can use.
    n_gpu : int
        The GPU card a job can use.
    n_node : int
        The nodes a job can use. If 0, then will be decided by slurm.
    env_cmd : str
        The commands for setting up the environment before running real calculations.
    sh : str
        The default name of the job script
    host : str
        The IP address of the remote host that is running Slurm
    username : str
        The username for logging in the remote host
    remote_dir : str
        The default directory to use on the remote host for running calculation
    port : int
        The SSH port for logging in the remote host
    max_running_hour: int
        The wall time limit for a job in hours.
    cached_jobs_expire : int
        The lifetime of cached jobs in seconds.
    submit_cmd : str
        The command for submitting the job script.
        If is `sbatch` by default. But extra argument can be provided, e.g. `sbatch --qos=debug`.
    '''

    #: Whether or not this is a remote job scheduler
    is_remote = True

    def __init__(self, queue, n_proc, n_gpu, host, username, remote_dir, port=22, n_node=0, env_cmd=None):
        super().__init__(queue=queue, n_proc=n_proc, n_gpu=n_gpu, n_node=n_node, env_cmd=env_cmd)

        self.host = host
        self.port = port
        self.username = username
        self.remote_dir = remote_dir

        # be careful about the port option. -p in ssh, -P in scp
        self._ssh_cmd = f'ssh -o ConnectTimeout=5 -o BatchMode=yes -o StrictHostKeyChecking=no -p {self.port} {self.username}@{self.host}'
        self._scp_cmd = f'scp -o ConnectTimeout=5 -o BatchMode=yes -o StrictHostKeyChecking=no -P {self.port}'
        # require rsync 3.1.0 or above
        self._rsync_cmd = f'rsync --human-readable --recursive --links --perms --executability --times --info=progress2 --rsh="ssh -p {self.port}"'

        if not self.is_working():
            raise SchedulerError('Cannot connect to Slurm @ %s' % host)

    def is_working(self) -> bool:
        '''
        Check whether or not Slurm is working normally on the remote machine.

        It calls `sinfo --version` and check the output.

        Returns
        -------
        is : bool
        '''
        logger.info(f'Connecting to Slurm on {self.host}')
        cmd = f'{self._ssh_cmd} sinfo --version'
        sp = Popen(cmd.split(), stdout=PIPE, stderr=PIPE)
        stdout, stderr = sp.communicate()

        return stdout.decode().startswith('slurm')

    def upload(self, remote_dir=None):
        '''
        Upload all the files in current local directory to remote directory.

        Parameters
        ----------
        remote_dir : dir, optional
            If not set, will use the default :attr:`remote_dir`.

        Returns
        -------
        successful : bool
            Whether or not the upload is successful
        '''

        remote_dir = remote_dir or self.remote_dir

        logger.info(f'Uploading to {remote_dir}')

        mkdir_cmd = f'{self._ssh_cmd} mkdir -p {remote_dir}'
        if subprocess.call(mkdir_cmd, shell=True) != 0:
            return False

        rsync_cmd = f'{self._rsync_cmd} ./ {self.username}@{self.host}:{remote_dir}/'
        if subprocess.call(rsync_cmd, shell=True) != 0:
            return False

        return True

    def download(self, remote_dir=None) -> bool:
        '''
        Upload all the files in remote directory to current local directory.

        Parameters
        ----------
        remote_dir : dir, optional
            If not set, will use the default :attr:`remote_dir`.

        Returns
        -------
        successful : bool
            Whether or not the download is successful
        '''
        remote_dir = remote_dir or self.remote_dir

        logger.info(f'Downloading from {remote_dir}')
        rsync_cmd = f'{self._rsync_cmd} {self.username}@{self.host}:{remote_dir}/ ./'
        if subprocess.call(rsync_cmd, shell=True) != 0:
            return False

        return True

    def submit(self, sh=None, remote_dir=None, local_dir=None):
        '''
        Submit a job script to the Slurm scheduler on the remote machine.

        Before calling `sbatch`, the script file on the remote machine should be processed.
        Because the job script is generated locally, the path are for local machine.
        In order to run it successfully on the remote machine, the path are replaced with the corresponding path on the remote machine.
        That is the purpose of arguments `remote_dir` and `local_dir`.

        Parameters
        ----------
        sh : str
            The job script to be submitted.
        remote_dir : str
            The directory to submit the script on the remote machine.
        local_dir : str
            The local directory used for generating the job script.

        Returns
        -------
        successful : bool
        '''
        sh = sh or self.sh
        remote_dir_path = Path(remote_dir or self.remote_dir).absolute()
        local_dir_path = Path(local_dir or os.getcwd()).absolute()

        sh_name = Path(sh).name
        remote_sh_name = sh_name + '.remote'
        remote_sh_path = remote_dir_path / remote_sh_name

        with open(sh) as f:
            content = f.read()
        with open(remote_sh_name, 'w') as f:
            f.write(content.replace(local_dir_path.as_posix(), remote_dir_path.as_posix()))

        logger.info(f'Uploading slurm script to {remote_dir_path}')

        mkdir_cmd = f'{self._ssh_cmd} "mkdir -p {remote_dir_path}"'
        if subprocess.call(mkdir_cmd, shell=True) != 0:
            return False

        scp_cmd = f'{self._scp_cmd} {remote_sh_name} {self.username}@{self.host}:{remote_sh_path}'
        if subprocess.call(scp_cmd, shell=True) != 0:
            return False

        # Be careful. Use "" for several commands over ssh
        sbatch_cmd = f'{self._ssh_cmd} "cd {remote_dir_path}; {self.submit_cmd} {remote_sh_path}"'
        if subprocess.call(sbatch_cmd, shell=True) != 0:
            return False

        return True

    def kill_job(self, name) -> bool:
        job = self.get_job_from_name(name)
        if job is None:
            return False

        cmd = f'{self._ssh_cmd} scancel {job.id}'
        return subprocess.call(cmd, shell=True) == 0

    def get_all_jobs(self):
        # Show all jobs. Then check the user
        logger.info(f'Queuing jobs on remote Slurm')

        cmd = f'{self._ssh_cmd} scontrol show job'
        sp = Popen(cmd.split(), stdout=PIPE, stderr=PIPE)
        stdout, stderr = sp.communicate()
        if sp.returncode != 0:
            logger.error(stderr.decode())
            return []

        jobs = []
        for job_str in stdout.decode().split('\n\n'):  # split jobs
            if job_str.startswith('JobId'):
                job = self._get_job_from_str(job_str)
                # Show all jobs. Then check the user
                if job.user == self.username:
                    jobs.append(job)
        return jobs
