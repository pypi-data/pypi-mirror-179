# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dlkinematics',
 'dlkinematics.urdf_parser',
 'dlkinematics.urdf_parser.xml_reflection']

package_data = \
{'': ['*']}

install_requires = \
['lxml>=4.9.1,<5.0.0',
 'numpy>=1.23.5,<2.0.0',
 'pyaml>=21.10.1,<22.0.0',
 'pyyaml>=6.0,<7.0',
 'tensorflow-graphics>=2021.12.3,<2022.0.0',
 'tensorflow>=2.2.0,<3.0.0',
 'transformations>=2022.9.26,<2023.0.0']

setup_kwargs = {
    'name': 'dlkinematics',
    'version': '0.1.0rc4',
    'description': 'Differentiable Forward Kinematics for TensorFlow and Keras based on URDF files',
    'long_description': '[![dlkinematics](https://github.com/lumoe/dlkinematics/actions/workflows/main.yml/badge.svg)](https://github.com/lumoe/dlkinematics/actions/workflows/main.yml)\n\n# Deep Learning Kinematics\n\n### Differentiable Forwad Kinematics for TensorFlow and Keras\n\nSupported Joint Types:\n\n- [x] Fixed\n- [x] Revolute\n- [x] Continious\n- [x] Prismatic\n- [x] Floating (not coverd by unit tests)\n- [x] Planar (not coverd by unit tests)\n\n## Installation\n\n### Install from PyPi\n\n`$ pip install dlkinematics`\n\n### Install from source\n\n`$ pip install -e git+https://github.com/lumoe/dlkinematics.git@main#egg=DLKinematics`\n\n## Usage:\n\n```python\nimport tensorflow as tf\nfrom dlkinematics.urdf import chain_from_urdf_file\nfrom dlkinematics.dlkinematics import DLKinematics\n\n# Load URDF\nchain = chain_from_urdf_file(\'data/human.urdf\')\n\n# Create DLKinematics\ndlkinematics = DLKinematics(\n   chain,\n   base_link="human_base",\n   end_link="human_spine_2",\n   batch_size=2)\n\n# Joint configuartion\nthetas = tf.Variable([1., 2., 3., 4.], dtype=tf.float32)\n\n# Forward pass\nwith tf.GradientTape() as tape:\n    result = dlkinematics.forward(thetas)\n\nprint(result)\nprint(tape.gradient(result, thetas))\n\n```\n\n## As Keras Layer\n\n```python\nfrom dlkinematics.training_utils import ForwardKinematics\nfrom tensorflow import keras\nimport tensorflow as tf\n\nmodel = keras.Sequential()\n\nFK_layer = ForwardKinematics(\n   urdf_file = \'path/to/urdf\',\n   base_link = \'link0\',\n   end_link = \'linkN\',\n   batch_size = 2)\n\nmodel.add(FK_layer)\n# Output shape of FK_layer is (batch_size, 4, 4)\n```\n\n## Run tests\n\nThe tests use ROS packages to validate the result of the dlkinematics module.\n\n1. Build the docker image for tests:  \n   `$ docker build -t dlkinematics_tests .`\n\n1. Start the container in the root folder of the project:  \n   `$ docker run -it -v $PWD:/work dlkinematics_tests python3 -m pytest`\n\n1. Execute all tests:  \n   `$ docker run -it -v $PWD:/work dlkinematics_tests python3 -m pytest`  \n   Execute only a single testfile:  \n   `$ docker run -it -v $PWD:/work dlkinematics_tests python3 -m pytest tests/test_prismatic.py`\n',
    'author': 'Lukas Mölschl',
    'author_email': 'lukas+pypi@moelschl.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/lumoe/dlkinematics',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
