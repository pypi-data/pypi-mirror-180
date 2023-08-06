# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fireproxng', 'fireproxng.lib', 'fireproxng.utils']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.24.41,<2.0.0',
 'bs4>=0.0.1,<0.0.2',
 'click',
 'click-extra>=3.0.1,<4.0.0',
 'lxml>=4.9.1,<5.0.0',
 'rich',
 'tldextract>=3.3.1,<4.0.0',
 'tzlocal>=4.2,<5.0',
 'validators>=0.20.0,<0.21.0']

entry_points = \
{'console_scripts': ['fireproxng = fireproxng.__main__:main',
                     'fpng = fireproxng.__main__:main']}

setup_kwargs = {
    'name': 'fireproxng',
    'version': '0.0.1',
    'description': 'Next generation fireprox AWS API endpoint creation utility.',
    'long_description': '<div align="center">\n\n# fireproxng\n\nfireproxng is a refresh of the widely loved fireprox.\n\n<br>\n\n[Why](#why) •\n[Installation](#installation) •\n[Getting started](#getting-started) •\n[Usage](#usage) •\n[Example Usage](#example-usage) •\n[Coming Soon](#coming-soon) •\n[Thanks](#thanks)\n\n#### Check out the [Sprocket Security Blog]([https://sprocketsecurity.com/resources/](https://www.sprocketsecurity.com/resources/evading-external-network-security-controls)) for more details!\n\n</div><br>\n\n</div>\n\n# Why\n\nThe original fireprox project appears to be mostly unchanged and I assume most organizations have transitioned to maintaining an internal version of the tool. We need fireprox to enable continuous penetration testing and would like to open up the updated version of the tool to the public.\n\nfireproxng also includes some evasion features that are not present in the original fireprox. Please see the [Thanks](#thanks) section for more information.\n\n<br>\n\n## Installation\n\nfireproxng be installed from the PyPi using the following command:\n\n```\npipx install fireproxng\n```\n\nIf this tool is not yet availible via PyPi, you can install it directly from the repository using:\n\n```\npipx install git+https://github.com/puzzlepeaches/fireproxng.git\n```\n\nFor development, clone the repository and install it locally using Poetry.\n\n```\ngit clone https://github.com/puzzlepeaches/fireproxng.git\ncd fireproxng\npoetry shell && poetry install\n```\n\n<br>\n\n## Getting started\n\nfireproxng holds the same functionality as its predecessor, fireprox. The utility now however has been moderized to be more user friendly with argument driven operations along with a more intuitive interface.\n\nfireproxng has four subcommands:\n\n- create\n- delete\n- list\n- update\n\nAll functionality is shared with the original tool. fireproxng can be called using `fireproxng` or `fpng`.\n\n<br>\n\n## Usage\n\nThe help menu for the base utility is shown below:\n\n```\nUsage: fireproxng [OPTIONS] COMMAND [ARGS]...\n\n  fireproxng is a tool for deploying AWS API Gateway proxies.\n\nOptions:\n  -ak, --access_key TEXT          AWS Access Key ID\n  -sk, --secret_access_key TEXT   AWS Secret Access Key\n  -r, --region [us-east-1|us-east-2|us-west-1|us-west-2|ca-central-1|eu-west-1|eu-west-2|eu-central-1|ap-southeast-1|ap-southeast-2|ap-south-1|ap-northeast-1|ap-northeast-2|sa-east-1|cn-north-1]\n                                  AWS Region\n  -st, --session_token TEXT       AWS Session Token\n  -p, --profile TEXT              AWS Profile\n  -h, --help                      Show this message and exit.\n\nCommands:\n  create  Create a new fireproxng proxy.\n  delete  Delete a fireproxng proxy.\n  list    List all fireproxng proxies.\n  update  Update a fireproxyng proxy.\n```\n\nAll subcommands expect AWS credentials sourced from command line parameters, environment variables, or the aws credentials file (perfered). Major regions are supported.\n\nThe environment variables fireproxng can read from are as follows:\n\n- access_key - AWS_ACCESS_KEY_ID\n- secret_access_key - AWS_SECRET_ACCESS_KEY\n- region - AWS_REGION\n\nTo specify a profile in your existing AWS credentials file, use the `-p` or `--profile` flag.\n\n<br>\n\n### Create\n\nAn example help menu for the create subcommand is shown below:\n\n```\nUsage: fireproxng create [OPTIONS] TARGET...\n```\n\nWhen creating a new proxy endpoint, you can specify an arbitrary number of URLs to stage the API gateway. The tool will automatically generate a unique name for the proxy endpoint. For example you can do the following:\n\n```\nfpng create https://example.com https://example.com/api/v1 https://example.com/api/v2\n```\n\nThis will stage multiple endpoints with the same name and different api-id values. You can additionally specify a list of URLs from a file:\n\n```\nfpng create /tmp/urls.txt\n```\n\nThe file should contain one URL per line.\n\nOutput files in JSON format are also supported for tracking created existing endpoints and integrating with existing tools:\n\n```\nfpng create -o /tmp/proxies.json /tmp/urls.txt\n```\n\n<br>\n\n### Delete\n\nThe same goes as above for the delete subcommand with the fireproxng enhanced capability to delete multiple endpoints at once. The help menu for the delete subcommand is shown below:\n\n```\n Usage: fpng delete [OPTIONS] [PROFILE_NAME] [API_ID]...\n```\n\nAn example of the delete command in action is shown below:\n\n```\nfpng delete lvofzv6sc2 n7sark2eei\n```\n\nYou can alternatively specify "all" as the API ID to delete all endpoints.\n\n```\nfpng delete all\n```\n\nSimilarly to the create subcommand, you can specify a list of API IDs from a file:\n\n```\nfpng delete /tmp/api_ids.txt\n```\n\n<br>\n\n### List\n\nfireproxng can also list existing API endpoints not in a deleted state. The help menu for the list subcommand is shown below:\n\n```\n Usage: fpng list [OPTIONS] [PROFILE_NAME]\n```\n\nAn example command to list all endpoints is shown below:\n\n```\nfpng list\n```\n\n<br>\n\n### Update\n\nThe update subcommand includes the ability to update the target of an existing endpoint using an API ID. The help menu for the update subcommand is shown below:\n\n```\n Usage: fpng update [OPTIONS] [PROFILE_NAME] API_ID TARGET\n```\n\n<br>\n\n## Example Usage\n\nCreate multiple API endpoints from the command line using the create subcommand while sourcing from environment variables:\n\n```\nexport AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE\nexport AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY\nfpng create https://example.com https://example.com/api/v1 https://example.com/api/v2\n```\n\nDelete all API endpoints using the delete subcommand while sourcing credentials from a profile:\n\n```\nfpng delete -p default all\n```\n\nList all API endpoints using the list subcommand while sourcing credentials from the command line:\n\n```\nfpng -ak AKIAIOSFODNN7EXAMPLE -sk wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY list\n```\n\n## Coming Soon\n\nSome planned features coming in the next release:\n\n- Create proxy endpoints across multiple regions\n- Update fireproxng endpoint name when updating target\n- Alternate service usage for proxying traffic\n- Session token handling (This is borken currently and I don\'t know anyone who uses it)\n- YAML config file support\n\n<br>\n\n## Thanks\n\n- The original [fireprox](https://github.com/ustayready/fireprox) of course from ustayready.\n- Evasion features added by the authors of [CredMaster](https://github.com/knavesec/CredMaster/blob/master/fire.py).\n',
    'author': 'Nicholas Anastasi',
    'author_email': 'nanastasi@sprocketsecurity.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/puzzlepeaches/fireproxng',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
