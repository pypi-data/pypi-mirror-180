# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cli',
 'cli.commands',
 'cli.commons',
 'cli.utils',
 'cli.utils.minio_ops',
 'cli.utils.oss_ops',
 'cli.utils.views',
 'cli.utils.views.cifar-10',
 'cli.utils.views.cifar-10-auto',
 'cli.utils.views.coco-demo',
 'cli.utils.views.coco-demo.src',
 'cli.utils.views.coco-demo.src.constants',
 'cli.utils.views.coco-demo.src.utils',
 'dsdlsdk',
 'dsdlsdk.exception']

package_data = \
{'': ['*'], 'cli': ['resources/*'], 'dsdlsdk': ['common/*']}

install_requires = \
['Pillow>=9.1.0,<10.0.0',
 'boto3>=1.26.14,<2.0.0',
 'click>=8.1.3,<9.0.0',
 'duckdb>=0.6.0,<0.7.0',
 'jinja2>=3.0.0,<4.0.0',
 'jsonmodels>=2.6.0,<3.0.0',
 'loguru>=0.6.0,<0.7.0',
 'networkx>=2.8.4,<3.0.0',
 'opencv-python>=4.6.0.66,<5.0.0.0',
 'oss2>=2.15.0,<3.0.0',
 'pandas>=1.5.1,<2.0.0',
 'prettytable>=3.3.0,<4.0.0',
 'psutil>=5.9.4,<6.0.0',
 'pyarrow>=10.0.0,<11.0.0',
 'pyyaml>=6.0,<7.0',
 'rich>=12.6.0,<13.0.0',
 'setuptools-scm>=7.0.5,<8.0.0',
 'smart-open[all]>=6.2.0,<7.0.0',
 'stqdm>=0.0.4,<0.0.5',
 'streamlit>=1.15.1,<2.0.0',
 'tabulate>=0.9.0,<0.10.0',
 'termgraph>=0.5.3,<0.6.0',
 'toml>=0.10.2,<0.11.0',
 'tqdm>=4.64.1,<5.0.0']

entry_points = \
{'console_scripts': ['dsdl = dsdl.cli:cli', 'odl-cli = cli.cli:main']}

setup_kwargs = {
    'name': 'odl-cli',
    'version': '0.1.1.post130',
    'description': 'made for opendatalab dsdl-sdk dev-cli branch(ignore other branches).',
    'long_description': '<div align="center">\n  <img src="resources/opendatalab.svg" width="600"/>\n  <div>&nbsp;</div>\n  <div align="center">\n    <b><font size="5">OpenDataLab website</font></b>\n    <sup>\n      <a href="https://opendatalab.com/">\n        <i><font size="4">HOT</font></i>\n      </a>\n    </sup>\n    &nbsp;&nbsp;&nbsp;&nbsp;\n  </div>\n  <div>&nbsp;</div>\n</div>\n\nEnglish | [简体中文](README_zh-CN.md)\n\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dsdl) ](https://pypi.org/project/dsdl/)[![PyPI](https://img.shields.io/pypi/v/dsdl)](https://pypi.org/project/dsdl) [![docs](https://img.shields.io/badge/docs-latest-blue)](https://opendatalab.github.io/dsdl-docs/)[![dev workflow](https://github.com/opendatalab/dsdl-sdk/actions/workflows/dev.yml/badge.svg?branch=dev)](https://github.com/opendatalab/dsdl-sdk/actions/workflows/dev.yml)[![stage & preview workflow](https://github.com/opendatalab/dsdl-sdk/actions/workflows/preview.yml/badge.svg?branch=dev)](https://github.com/opendatalab/dsdl-sdk/actions/workflows/preview.yml)\n\n[📘Documentation](https://opendatalab.github.io/dsdl-docs/) |\n\n## Introduction\n\n**Data** is the cornerstone of artificial intelligence. The efficiency of data acquisition, exchange, and application directly impacts the advances in technologies and applications. Over the long history of AI, a vast quantity of data sets have been developed and distributed. However, these datasets are defined in very different forms, which incurs significant overhead when it comes to exchange, integration, and utilization -- it is often the case that one needs to develop a new customized tool or script in order to incorporate a new dataset into a workflow.\n\nTo overcome such difficulties, we develop **Data Set Description Language (DSDL)**.\n\n### Major features\n\nThe design of **DSDL** is driven by three goals, namely *generic*, *portable*, *extensible*. We refer to these three goals together as **GPE**.\n\n* **Generic**\n\n  This language aims to provide a unified representation standard for data in multiple fields of artificial intelligence, rather than being designed for a single field or task. It should be able to express data sets with different modalities and structures in a consistent format.\n\n* **Portable**\n\n  Write once, distribute everywhere. Dataset descriptions can be widely distributed and exchanged, and used in different environments without modification of the source files. The achievement of this goal is crucial for creating an open and thriving ecosystem. To this end, we need to carefully examine the details of the design, and remove unnecessary dependencies on specific assumptions about the underlying facilities or organizations.\n\n* **Extensible**\n\n  One should be able to extend the boundary of expression without modifying the core standard. For a programming language such as C++ or Python, its application boundaries can be significantly extended by libraries or packages, while the core language remains stable over a long period. Such libraries and packages form a rich ecosystem, making the language stay alive for a very long time.\n\n## Installation\n\n**Case a** install it with pip\n\n```bash\npip install dsdl\n```\n\n**Case b** install it from source\n\n```shell\ngit clone https://github.com/opendatalab/dsdl.git\ncd dsdl\npython setup.py install\n```\n\n## Get Started\n\n#### Use dsdl parser to deserialize the Yaml file to Python code\n```bash\ndsdl parse --yaml demo/coco_demo.yaml\n```\n\n#### Modify the configuration & set the directory of media in dataset\n\nCreate a configuration file `config.py` with the following contents（for now dsdl only reading from aliyun oss or local is supported）：\n\n```python\nlocal = dict(\n    type="LocalFileReader",\n    working_dir="local path of your media",\n)\n\nali_oss = dict(\n    type="AliOSSFileReader",\n    access_key_secret="your secret key of aliyun oss",\n    endpoint="your endpoint of aliyun oss",\n    access_key_id="your access key of aliyun oss",\n    bucket_name="your bucket name of aliyun oss",\n    working_dir="the relative path of your media dir in the bucket")\n```\n\n In `config.py`, the configuration of how to read the media in a dataset is defined. One should specify the arguments depending on from where to read the media：  \n\n1. read from local： `working_dir` field in `local` should be specified (the directory of local media)    \n2. read from aliyun oss： all the field in `ali_oss `should be specified (including `access_key_secret`, `endpoint`, `access_key_id`, `bucket_name`, `working_dir`)  \n\n#### Visualize samples\n\n   ```bash\n   dsdl view -y <yaml-name>.yaml -c <config.py> -l ali-oss -n 10 -r -v -f Label BBox Attributes\n   ```\n\nThe description of each argument is shown below:  \n\n| simplified  argument | argument      | description                                                  |\n| -------------------- | ------------- | :----------------------------------------------------------- |\n| -y                   | `--yaml`      | The path of dsdl yaml file.                                  |\n| -c                   | `--config`    | The path of  location configuration file.                    |\n| -l                   | `--location`  | `local` or `ali-oss`，which means read media from local or aliyun oss. |\n| -n                   | `--num`       | The number of samples to be visualized.                      |\n| -r                   | `--random`    | Whether to load the samples in a random order.               |\n| -v                   | `--visualize` | Whether to visualize the samples or just print the information in console. |\n| -f                   | `--field`     | The field type to visualize, e.g. `-f BBox`means show the bounding box in samples, `-f Attributes`means show the attributes of a sample in the console . One can specify multiple field types simultaneously, such as `-f Label BBox  Attributes`. |\n| -t                   | `--task`      | The task you are working on, for example, `-t detection` is equivalent to `-f Label BBox Polygon Attributes`. |\n\n## Citation\n\nIf you find this project useful in your research, please consider cite:\n\n```bibtex\n@misc{dsdl2022,\n    title={{DSDL}: Data Set Description Language},\n    author={DSDL Contributors},\n    howpublished = {\\url{https://github.com/opendatalab/dsdl}},\n    year={2022}\n}\n```\n\n## License\n\n`DSDL` is released under the [Apache 2.0 license](LICENSE).\n\n## Acknowledgement\n\n* Field & Model Design inspired by [Django ORM](https://www.djangoproject.com/) and [jsonmodels](https://github.com/jazzband/jsonmodels)\n',
    'author': 'odl-cli',
    'author_email': 'odl-cli@pjlab.org.cn',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/opendatalab/dsdl-sdk/tree/dev-cli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8, !=2.7.*, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*, !=3.6.*, !=3.7.*',
}


setup(**setup_kwargs)
