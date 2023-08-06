# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['textual_forms']

package_data = \
{'': ['*']}

install_requires = \
['textual[dev]>=0.4.0,<0.5.0']

setup_kwargs = {
    'name': 'textual-forms',
    'version': '0.1.5',
    'description': 'Dynamic forms for Textual TUI Framework',
    'long_description': '# Textual Forms\n\n[![Python Versions](https://shields.io/pypi/pyversions/textual-inputs)](https://www.python.org/downloads/)\n[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)\n\nDynamic forms for [Textual](https://github.com/willmcgugan/textual) TUI framework.\n\n> #### Note: This library is still very much WIP 🧪\n\n## About\n\nTextual Forms aims to make it easy to add forms to your Textual-powered applications.\n\n### Requirements\n\n* python >=3.7,<4\n* poetry\n\n## Install\n\n```bash\npip install textual-forms\n```\n\n### Form Field Schema\n\n| Key         | Type        | Required | Options                 |\n|-------------|-------------|----------|-------------------------|\n| id          | str         | X        |                         |\n| type        | str         |          | string, number, integer |\n| value       | str, number |          |                         |\n| required    | bool        |          |                         |\n| placeholder | str         |          |                         |\n| rules       | dict        |          |                         |\n\n#### Type Rules\n\n**string**\n\n* min_length\n* max_length\n\n**integer**\n\n* min\n* max\n\n**number**\n\n* N/A\n\n### Button Schema\n\n| Key              | Type | Required | Options                          |\n|------------------|------|----------|----------------------------------|\n| id               | str  | x        |                                  |\n| label            | str  | x        |                                  |\n| variant          | str  |          | primary, error, success, warning |\n| watch_form_valid | bool |          |                                  |\n\nNote: If you set the `watch_form_valid` property, the button will only be enabled when the form is valid.\n\n## Overriding Form Widgets\n\nDocumentation TBD\n\n---\n\n## Example\n\n```python\nfrom rich.table import Table\nfrom textual.app import App, ComposeResult\nfrom textual.widgets import Static\n\nfrom textual_forms.forms import Form\n\nFIELDS = [\n    {\n        \'id\': \'name\',\n        \'required\': True,\n        \'placeholder\': \'name...\',\n        \'rules\': {\n            \'min_length\': 3,\n        }\n    },\n    {\n        \'id\': \'age\',\n        \'type\': \'integer\',\n        \'required\': True,\n        \'placeholder\': \'age...\',\n        \'rules\': {\n            \'min\': 18,\n            \'max\': 65\n        }\n    },\n    {\n        \'id\': \'email\',\n        \'required\': False,\n        \'placeholder\': \'hi@example.com\',\n    },\n]\n\nBUTTONS = [\n    {\n        \'id\': \'submit\',\n        \'label\': \'Submit\',\n        \'variant\': \'success\',\n        \'watch_form_valid\': True\n    },\n]\n\n\nclass BasicTextualForm(App):\n    def compose(self) -> ComposeResult:\n        yield Static(id=\'submitted-data\')\n        yield Form(\n            fields=FIELDS,\n            buttons=BUTTONS,\n        )\n\n    def on_form_event(self, message: Form.Event) -> None:\n        if message.event == \'submit\':\n            table = Table(*message.data.keys())\n            table.add_row(*message.data.values())\n            self.query_one(\'#submitted-data\').update(table)\n\n\nif __name__ == \'__main__\':\n\n    BasicTextualForm().run()\n\n```\n\n**Initial render**\n<img width="1004" alt="Screenshot 2022-11-15 at 3 49 46 PM" src="https://user-images.githubusercontent.com/7029352/202023490-e6494105-a102-4d9d-9072-90872ecad41a.png">\n\n**Valid form** \n<img width="1006" alt="Screenshot 2022-11-15 at 3 51 15 PM" src="https://user-images.githubusercontent.com/7029352/202023592-1a16f742-6af2-4e88-a9d3-7b84339fd231.png">\n\n**Invalid form**\n<img width="1006" alt="Screenshot 2022-11-15 at 3 51 39 PM" src="https://user-images.githubusercontent.com/7029352/202023734-76ae0b55-01b4-48a4-8a34-7c972d7a7df9.png">\n\n\n\n## Contributing\n\nTBD\n',
    'author': 'Lemuel Boyce',
    'author_email': 'lemuelboyce@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/rhymiz/textual-forms',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
