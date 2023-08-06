# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['retimer']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'retimer',
    'version': '0.1.0.1',
    'description': '',
    'long_description': '\nA simple package to make retry loops easier\n\n### Usage:\n\n```python\nfrom retimer import Timer\nimport time\n\ntimer = Timer(10)\nwhile timer.not_expired:\n    # do something for 10 seconds\n    \n    if retry_doing_something:\n                time.sleep(.5) # good if something is a request to a server or cpu intensive\n        continue\n    if something_bad:\n        timer.explode()\n    \n    # all good so we break before timer expires\n    break\n    \nif timer.expired:\n    print("Could not do something after tried for 10 seconds")\nelse:\n    print("Successfully did something after 10 seconds")\n    \n```\n',
    'author': 'henrique lino',
    'author_email': 'henrique.lino97@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
