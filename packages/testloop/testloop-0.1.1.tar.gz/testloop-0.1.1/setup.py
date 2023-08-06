# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['testloop']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['testloop = testloop.testloop:cli']}

setup_kwargs = {
    'name': 'testloop',
    'version': '0.1.1',
    'description': 'A nimble testing tool',
    'long_description': '# Testloop\n\nA nimble testing tool\n\n## Usage\n\n\n```shell\n$ python testloop.py\n[Wed Nov 30 20:34:50 2022] Running: python /home/jskulski/Code/jskulski/testloop/testloop.py test .\n\ntestloop: cwd=/home/jskulski/Code/jskulski/testloop\ntestloop: running test_command=`pytest -v --pdb --pdbcls=IPython.terminal.debugger:TerminalPdb -s tests/`\n\n\n======================================= test session starts =======================================\nplatform linux -- Python 3.11.0, pytest-7.2.0, pluggy-1.0.0\nrootdir: /home/jskulski/Code/jskulski/ballooning\nplugins: cov-2.12.1, asyncio-0.20.2, syrupy-3.0.5, time-machine-2.8.2, anyio-3.6.2, aiohttp-1.0.4\nasyncio: mode=Mode.STRICT\ncollected 9 items / 2 deselected / 7 selected\n\ntests/test_initial_design_sprint.py s......                                                 [100%]\n\n------------------------------------- snapshot report summary -------------------------------------\n\n=========================== 6 passed, 1 skipped, 2 deselected in 0.04s ============================\n\n```\n\ntestloop.py: reads itself for configuration, builds a pytest command\n  and runs it when files change\n\nRunning `python testloop.py` starts a filewatcher that runs pytest\n\nWhen a file changes:\n1. `testloop` reads itself for pytest options\n1. builds a pytest command from those options\n1. runs that pytest command and reports results\n\n`testloop.py` contains option dictionaries:\n\nYou can comment/uncomment/modify these options to trigger a new test run. Changing your source code will also trigger a new run.\n\n```python\npytest_opts = dict(\n    # match=\'-k test_logs_when_both_repo_and_failsafe_fail_to_persist\',\n    # last_failed="--lf",\n    dbg="--pdb --pdbcls=IPython.terminal.debugger:TerminalPdb",\n    use_settrace="-s",\n    # coverage="--cov=lib/history --cov-report term",\n)\n```\n\nNote, the initial run of testloop will install dependencies at runtime.\n\n\n## Design\n\nTestloop is a nimble developement testing tool.\n\nNimble development tools are designed to be:\n\n\n- "Good enough" development tools available across the containerized divide.\n- at-hand, easy to install, even on the most alpine of docker containers\n- simple in function\n- complex in features\n- self contained configuration, effectively stateless\n- self-installing dependencies allow for an unfolding feature set\n\n\n## Changelog\n\nv 0.1.0\n\n- create readme, package and publish\n- testloop in a working state (read self for config, watches files, runs pytest)\n- add a test for testloop\n\nv 0.1.1\n\n- adding CLI script, pre-commits\n- updating pypi page\n\n### Current\n\n\nv 0.1.5\n- [x] testloop executable script\n- [ ] how do we handle configuration if we install via pip?\n- [ ] fix PATHING\n\n### Future\n\nv 0.2.0\n\n- [ ] handle project environments venv activation (setup step?)\n- [ ] direct skul.ski to a hosting service, update install doc\n- [ ] system binary `testloop` if installed via pip\n- [ ] cli options to turn on/off dependencies\n- [ ] add pudb option, build configurations as object\n\n\n- [ ] tui / gui / editor integrations\n- [ ] create system-wide venv for dependencies OR consider rewriting as an executable + config\n',
    'author': 'Jon Skulski',
    'author_email': 'jskulski@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/jskulski/testloop',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
