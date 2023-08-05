# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['logging_journald']
setup_kwargs = {
    'name': 'logging-journald',
    'version': '0.6.3',
    'description': 'Pure python logging handler for writing logs to the journald using native protocol',
    'long_description': 'logging-journald\n================\n\nPure python logging handler for writing logs to the journald using\nnative protocol.\n\n```python\nimport logging\nfrom logging_journald import JournaldLogHandler, check_journal_stream\n\n# Use python default handler\nLOG_HANDLERS = None\n\n\nif (\n    # Check if program running as systemd service\n    check_journal_stream() or\n    # Check if journald socket is available\n    JournaldLogHandler.SOCKET_PATH.exists()\n):\n    LOG_HANDLERS = [JournaldLogHandler()]\n\nlogging.basicConfig(level=logging.INFO, handlers=LOG_HANDLERS)\nlogging.info("Hello logging world.")\n```\n',
    'author': 'Dmitry Orlov',
    'author_email': 'me@mosquito.su',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/mosquito/logging-journald',
    'py_modules': modules,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
