# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['safetydance']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'safetydance',
    'version': '0.3.2',
    'description': 'A typesafe system for defining and composing steps.',
    'long_description': '# safetydance\n\n`safetydance` is a Python framework for defining type-safe and flexibly composable\napplication steps with a shared execution context for sharing variables between the\nsteps. The design of safetydance is partially inspired by `<https://cucumber.io>`_.\n\n\n## Description\n\n`safetydance` defines a set of decorators that rewrite functions as steps and scripts.\n\nA step should be a function with a name that reads easily, like a short phrase or\nsentence. Steps may take arguments and they may access variables defined for the\n"context scope". Steps may call other steps, too.\n\nA script is a function composing the execution of a series of steps. A script is a step\nthat defines an execution context. Scripts may also call other scripts. The primary\ndifference between a script and a step is the implicit definition of the execution\ncontext. *TODO* When a script calls another script the current execution context *may*\nbe passed as a kwarg to the nested script; by default all scripts execute in their own\nexecution context; that is, if a step is used by both an originating and a nested script\nthe context variables it accesses are determined by the calling script\'s execution\ncontext.\n\n### Context Scope Variables\n\nA context scope variable is sort of like a global variable. The run of a script defines\na context where `context_data` variables are stored for access by steps.\n\nThink of a conversation between two friends. Much of the conversation will reference\nassumed shared knowledge, or context. For `safetydance`, the context scope provides a\nway for steps to share assumed context to make it possible to provide a more\nconversational style of programming\n\n## Future Work\n\n* Mypy extension to validate scripts. For example, prove that a script shouldn\'t fail\n  due to missing `context_data` for any step in the script.\n* Dry run execution of steps\n* DAG derivation for scripts\n* Parallel evaluation for independent up to a join for DAG legs of a script.\n* Diagram output for script DAGs.\n\n## Setup for Development\n\n```bash\npoetry install\n```\n',
    'author': 'David Charboneau',
    'author_email': 'david@adadabase.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/dcharbon/safetydance',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
