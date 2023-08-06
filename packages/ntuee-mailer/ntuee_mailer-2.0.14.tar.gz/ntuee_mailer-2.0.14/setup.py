# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ntuee_mailer']

package_data = \
{'': ['*'],
 'ntuee_mailer': ['template_letter/*', 'template_letter/attachments/*']}

install_requires = \
['Cerberus==1.3.4',
 'PyYAML==6.0',
 'click==8.0.4',
 'email-validator==1.2.1',
 'rich==12.5.1',
 'typer[all]>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['ntuee-mailer = ntuee_mailer.main:app']}

setup_kwargs = {
    'name': 'ntuee-mailer',
    'version': '2.0.14',
    'description': 'an auto mailer to send emails in batch for you',
    'long_description': '# `ntuee-mailer`\n\nThis is a simple mailer for NTU students to send letters in batches.\n\n**Installation**\n\n```bash\n$ pip install ntuee-mailer\n```\n\n**Usage**:\n\n```bash\n$ ntuee-mailer [OPTIONS] COMMAND [ARGS]...\n```\n\n**Options**:\n\n- `--install-completion`: Install completion for the current shell.\n- `--show-completion`: Show completion for the current shell, to copy it or customize the installation.\n- `--help`: Show this message and exit.\n\n**Commands**:\n\n- `check`: check wether a directory is a valid letter a...\n- `config`: configure the auto mailer a valid config file...\n- `new`: create a new letter from template\n- `send`: send emails to a list of recipients as...\n\n## `ntuee-mailer check`\n\ncheck wether a directory is a valid letter\n\na letter folder should be structured as follows:\n\n```\nletter_name\n├── attachments\n│ ├── ...\n│ └── ...\n├── config.yml\n├── content.html\n└── recipients.csv\n```\n\n**Usage**:\n\n```console\n$ ntuee-mailer check [OPTIONS] LETTER_PATH\n```\n\n**Arguments**:\n\n- `LETTER_PATH`: Path to letter directory [required]\n\n**Options**:\n\n- `--help`: Show this message and exit.\n\n## `ntuee-mailer config`\n\nconfigure the auto mailer\n\na valid config file should have the following structure:\n\n```\n[smtp]\nhost=smtps.ntu.edu.tw\nport=465\ntimeout=5\n[pop3]\nhost=msa.ntu.edu.tw\nport=995\ntimeout=5\n[account]\nname=John Doe\n```\n\n**Usage**:\n\n```console\n$ ntuee-mailer config [OPTIONS]\n```\n\n**Options**:\n\n- `-f, --file TEXT`: Path to new config file whose content will be copied to config.ini\n- `-r, --reset`: Reset config.ini to default [default: False]\n- `-l, --list`: list current config [default: False]\n- `--help`: Show this message and exit.\n\n## `ntuee-mailer new`\n\ncreate a new letter from template\n\n**Usage**:\n\n```console\n$ ntuee-mailer new [OPTIONS] LETTER_NAME\n```\n\n**Arguments**:\n\n- `LETTER_NAME`: Name of letter [required]\n\n**Options**:\n\n- `--help`: Show this message and exit.\n\n## `ntuee-mailer send`\n\nsend emails to a list of recipients as configured in your letter\n\n**Usage**:\n\n```console\n$ ntuee-mailer send [OPTIONS] [LETTER_PATH]\n```\n\n**Arguments**:\n\n- `[LETTER_PATH]`: Path to letter\n\n**Options**:\n\n- `-t, --test`: Test mode: send mail to yourself [default: False]\n- `-c, --config FILE`: Path to config.ini [default: /home/madmax/.config/ntuee-mailer/config.ini]\n- `-q, --quiet`: Quiet mode: less output [default: False]\n- `-d, --debug INTEGER RANGE`: Debug level [default: 0]\n- `--help`: Show this message and exit.\n\n## `ntuee-mailer test`\n\n**Usage**:\n\n```console\n$ ntuee-mailer test [OPTIONS]\n```\n\n**Options**:\n\n- `--help`: Show this message and exit.\n\n## mail format\n\na letter folder should be structured as follows:\n```\nletter_name\n├── attachments\n│ ├── ...\n│ └── ...\n├── config.yml\n├── content.html\n└── recipients.csv\n```\n\n### content.html\nThe content of the email. `$<pattern>` would be replaced by the corresponding field defined in `recipients.csv`\n\n### recipients.csv\nStores the data related to recipients. The value of "name" field is will be used to replace `$name` in `content.html`, whose behavior can be modified in `config.yml`. The "email" field stores the recipients email. The emails will be CCed and BCCed to the emails in "cc" and "bcc" field. One recipients may have several CC and BCCs, emails should be separated with spaces. "email", "cc" and "bcc" are reserved fields, they cannot be used in html pattern, any additional field will be replaced in the html. "name" and "email" fields are required\n\n### config.yml\nConfiguration of each email. "subjects" defines subject, "from" defines the name recipients see in their email client. "recipientTitle" and "lastNameOnly" modifies the behavior of `$name` in `content.html`.\n\n### attachments\nThe attachment directory. Any file placed in this folder will be attached to the email. Any file with name started with \'.\' will be ignored, i.e. .git, .DS_STORE.\n',
    'author': 'madmaxieee',
    'author_email': '76544194+madmaxieee@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/madmaxieee/ntuee-mailer',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.3,<4.0.0',
}


setup(**setup_kwargs)
