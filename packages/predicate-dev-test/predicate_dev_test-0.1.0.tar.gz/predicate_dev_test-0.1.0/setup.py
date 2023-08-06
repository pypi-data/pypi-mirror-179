# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cli', 'solver', 'solver.test']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'black>=22.8.0,<23.0.0',
 'click>=8.1.3,<9.0.0',
 'flake8>=5.0.4,<6.0.0',
 'isort>=5.10.1,<6.0.0',
 'lint-python>=2.0.0,<3.0.0',
 'mypy>=0.982,<0.983',
 'pytest>=7.1.3,<8.0.0',
 'setuptools>=65.3.0,<66.0.0',
 'z3-solver>=4.11.2.0,<5.0.0.0']

entry_points = \
{'console_scripts': ['predicate = cli:main']}

setup_kwargs = {
    'name': 'predicate-dev-test',
    'version': '0.1.0',
    'description': '',
    'long_description': '# predicate\n\n## Installing predicate\n\n```bash\npoetry install\n```\n\nAlternately, `poetry shell` can also be used to run `predicate`.\n\n## Working with policies\n\n### Example policy\n\n```py\n# access.py\n\nfrom solver.ast import Duration\nfrom solver.teleport import AccessNode, Node, Options, OptionsSet, Policy, Rules, User\n\n\nclass Teleport:\n    p = Policy(\n        name="access",\n        loud=False,\n        allow=Rules(\n            AccessNode(\n                ((AccessNode.login == User.name) & (User.name != "root"))\n                | (User.traits["team"] == ("admins",))\n            ),\n        ),\n        options=OptionsSet(Options((Options.max_session_ttl < Duration.new(hours=10)))),\n        deny=Rules(\n            AccessNode(\n                (AccessNode.login == "mike")\n                | (AccessNode.login == "jester")\n                | (Node.labels["env"] == "prod")\n            ),\n        ),\n    )\n\n    def test_access(self):\n        # Alice will be able to login to any machine as herself\n        ret, _ = self.p.check(\n            AccessNode(\n                (AccessNode.login == "alice")\n                & (User.name == "alice")\n                & (Node.labels["env"] == "dev")\n            )\n        )\n        assert ret is True, "Alice can login with her user to any node"\n\n        # No one is permitted to login as mike\n        ret, _ = self.p.query(AccessNode((AccessNode.login == "mike")))\n        assert ret is False, "This role does not allow access as mike"\n\n        # No one is permitted to login as jester\n        ret, _ = self.p.query(AccessNode((AccessNode.login == "jester")))\n        assert ret is False, "This role does not allow access as jester"\n```\n\n### Testing a policy\n\n```bash\npredicate test access.py\n```\n\n```bash\nRunning 1 tests:\n  - test_access: ok\n```\n\n### Exporting a policy\n\n```bash\npredicate export access.py\n```\n\n```yaml\nkind: policy\nmetadata:\n  name: access\nspec:\n  allow:\n    access_node: (((access_node.login == user.name) && (!(user.name == "root"))) ||\n      equals(user.traits["team"], ["admins"]))\n  deny:\n    access_node: (((access_node.login == "mike") || (access_node.login == "jester"))\n      || (node.labels["env"] == "prod"))\n  options: (options.max_session_ttl < 36000000000000)\nversion: v1\n```',
    'author': 'Sakshyam Shah',
    'author_email': 'sshah@goteleport.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
