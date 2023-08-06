from mstk.errors import SchedulerError
from .scheduler import Scheduler


class Local(Scheduler):
    '''
    A fake job scheduler that run jobs on the local machine.

    It is designed for generate simulation files locally for debugging purpose.

    Parameters
    ----------
    n_proc : int
    n_gpu : int
    env_cmd : str

    Attributes
    ----------
    n_proc : int
    n_gpu : int
    env_cmd : str
    sh : str
    username : str
    '''

    #: Whether or not this is a remote job scheduler
    is_remote = False

    def __init__(self, n_proc, n_gpu, env_cmd=None, **kwargs):
        super().__init__(n_proc=n_proc, n_gpu=n_gpu, env_cmd=env_cmd, **kwargs)
        self.sh = '_job_local.sh'

    def is_working(self):
        return True

    def generate_sh(self, workdir, commands, name=None, sh=None, **kwargs):
        if sh is None:
            sh = self.sh
        with open(sh, 'w') as f:
            f.write(f'#!/bin/sh\n\n'
                    f'cd {workdir}\n'
                    f'{self.env_cmd}\n'
                    )
            for cmd in commands:
                f.write(cmd + '\n')

    def submit(self, sh=None):
        raise SchedulerError('Not supported on localhost')

    def is_running(self, name):
        raise SchedulerError('Not supported on localhost')

    def kill_job(self, name):
        raise SchedulerError('Not supported on localhost')

    def get_all_jobs(self):
        return []
