# Testloop

A nimble testing tool

## Usage


```shell
$ python testloop.py
[Wed Nov 30 20:34:50 2022] Running: python /home/jskulski/Code/jskulski/testloop/testloop.py test .

testloop: cwd=/home/jskulski/Code/jskulski/testloop
testloop: running test_command=`pytest -v --pdb --pdbcls=IPython.terminal.debugger:TerminalPdb -s tests/`


======================================= test session starts =======================================
platform linux -- Python 3.11.0, pytest-7.2.0, pluggy-1.0.0
rootdir: /home/jskulski/Code/jskulski/ballooning
plugins: cov-2.12.1, asyncio-0.20.2, syrupy-3.0.5, time-machine-2.8.2, anyio-3.6.2, aiohttp-1.0.4
asyncio: mode=Mode.STRICT
collected 9 items / 2 deselected / 7 selected

tests/test_initial_design_sprint.py s......                                                 [100%]

------------------------------------- snapshot report summary -------------------------------------

=========================== 6 passed, 1 skipped, 2 deselected in 0.04s ============================

```

testloop.py: reads itself for configuration, builds a pytest command
  and runs it when files change

Running `python testloop.py` starts a filewatcher that runs pytest

When a file changes:
1. `testloop` reads itself for pytest options
1. builds a pytest command from those options
1. runs that pytest command and reports results

`testloop.py` contains option dictionaries:

You can comment/uncomment/modify these options to trigger a new test run. Changing your source code will also trigger a new run.

```python
pytest_opts = dict(
    # match='-k test_logs_when_both_repo_and_failsafe_fail_to_persist',
    # last_failed="--lf",
    dbg="--pdb --pdbcls=IPython.terminal.debugger:TerminalPdb",
    use_settrace="-s",
    # coverage="--cov=lib/history --cov-report term",
)
```

Note, the initial run of testloop will install dependencies at runtime.


## Design

Testloop is a nimble developement testing tool.

Nimble development tools are designed to be:


- "Good enough" development tools available across the containerized divide.
- at-hand, easy to install, even on the most alpine of docker containers
- simple in function
- complex in features
- self contained configuration, effectively stateless
- self-installing dependencies allow for an unfolding feature set


## Changelog

v 0.1.0

- create readme, package and publish
- testloop in a working state (read self for config, watches files, runs pytest)
- add a test for testloop

v 0.1.1

- adding CLI script, pre-commits
- updating pypi page

### Current


v 0.1.5
- [x] testloop executable script
- [ ] how do we handle configuration if we install via pip?
- [ ] fix PATHING

### Future

v 0.2.0

- [ ] handle project environments venv activation (setup step?)
- [ ] direct skul.ski to a hosting service, update install doc
- [ ] system binary `testloop` if installed via pip
- [ ] cli options to turn on/off dependencies
- [ ] add pudb option, build configurations as object


- [ ] tui / gui / editor integrations
- [ ] create system-wide venv for dependencies OR consider rewriting as an executable + config
