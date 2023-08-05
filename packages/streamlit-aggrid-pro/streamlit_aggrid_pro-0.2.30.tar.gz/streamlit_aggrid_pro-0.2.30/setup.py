# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['st_aggrid_pro']

package_data = \
{'': ['*'],
 'st_aggrid_pro': ['frontend/*',
                   'frontend/build/*',
                   'frontend/build/static/css/*',
                   'frontend/build/static/js/*',
                   'frontend/build/static/media/*',
                   'frontend/public/*']}

install_requires = \
['pandas>=1.2',
 'python-decouple>=3.6,<4.0',
 'python-dotenv>=0.19.1,<0.20.0',
 'simplejson>=3.0',
 'streamlit>=0.87.0']

setup_kwargs = {
    'name': 'streamlit-aggrid-pro',
    'version': '0.2.30',
    'description': 'Streamlit component implementation of ag-grid-pro',
    'long_description': "# streamlit-aggrid-pro\n\n<br>\n\n# Install\n```\npip install streamlit-aggrid-pro\n\n```\n\n# Quick Use\nCreate an example.py file\n```python\nfrom st_aggrid_pro import AgGridPro\nimport pandas as pd\n\ndf = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')\nAgGridPro(df)\n```\nRun :\n```shell\nstreamlit run example.py\n```\n",
    'author': 'Pablo Fonseca',
    'author_email': 'yangxiaochuang2@163.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/llllyang123/streamlit-aggrid-pro',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<4.0',
}


setup(**setup_kwargs)
