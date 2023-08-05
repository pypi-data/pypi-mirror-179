# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sims_reia']

package_data = \
{'': ['*']}

install_requires = \
['pillow>=9.3.0,<10.0.0']

setup_kwargs = {
    'name': 'sims-reia',
    'version': '0.1.0',
    'description': '',
    'long_description': '# Sims2 Reia File Library\n\nThis is a parser for Sims 2 `.reia` files in Python.\n\n## Basic Usage\n\nRead a `.reia` file:\n\n```python\nwith open("N001.reia", "rb") as f:\n    reia_file = sims_reia.read_from_file(input)\n    print(f"resolution={reia_file.width}x{reia_file.height}, fps={reia_file.frames_per_second}")\n\n    for i, frame in enuemrate(reia_file.frames):\n        frame.image.save(f"frame{i}.png")\n```\n\n## Testing\n\n`poetry run pytest`\n\n## Formatting\n\n`poetry run black .`\n\n',
    'author': 'Ammar Askar',
    'author_email': 'ammar@ammaraskar.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
