import sys
import os
import subprocess

__version__ = "0.1.1"


files = [
    "tests/"
]

opts = {}

django_opts = dict(
    db="--reuse-db",
)

pytest_xdist_opts = dict(
    num_parallel='-n0'
)

pytest_opts = dict(
    # match='-k test_logs_when_both_repo_and_failsafe_fail_to_persist',
    # last_failed="--lf",
    dbg="--pdb --pdbcls=IPython.terminal.debugger:TerminalPdb",
    use_settrace="-s",
    # coverage="--cov=lib/history --cov-report term",
)

# opts.update(django_opts)
# opts.update(pytest_xdist_opts)
opts.update(pytest_opts)


dependencies = ['ipdb==0.13.9', 'pytest_watch==4.2.0', 'rich==12.5.1', 'textual==0.1.18']


CWD_PATH = os.path.dirname(__file__)
PROJECT_PATH = os.path.join(CWD_PATH)
TESTLOOP_PATH = os.path.abspath(__file__)


def install_dependencies():
    for dep in dependencies:
        print(f'Installing {dep}')
        pkg, version = dep.split('==')
        install_cmd = f'python -c "import {pkg}" || pip install {pkg}=={version}'
        subprocess.run(install_cmd.format(pkg), shell=True)


def test_command():
    command_parts = ["pytest", "-v"] + list(opts.values()) + files
    return ' '.join(command_parts)


def test():
    """Run test command"""
    print(f'testloop: cwd={PROJECT_PATH} ')
    print(f'testloop: running test_command=`{test_command()}`')

    os.chdir(PROJECT_PATH)
    os.system(test_command())


def loop_command():
    return f'ptw --ext py,sh --runner "python {TESTLOOP_PATH} test" .'


def loop():
    """Run loop command"""
    install_dependencies()

    print(f'testloop: cwd={PROJECT_PATH} ')
    print(f'testloop: loop_command=`{loop_command()}`')

    os.chdir(PROJECT_PATH)
    os.system(loop_command())


def run():
    try:
        mode = sys.argv[1]
    except IndexError:
        print('testloop: default to `looping`')
        mode = 'loop'

    if mode == 'loop':
        loop()
    elif mode == 'test':
        test()
    else:
        raise EnvironmentError(
            f"testloop: usage `{TESTLOOP_PATH} [mode]` "
            f"(invalid mode={mode} specified. must be `loop` or `test`)"
        )

def cli():
    run()

if __name__ == '__main__':
    run()
