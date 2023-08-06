# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sweep_design',
 'sweep_design.config',
 'sweep_design.defaults',
 'sweep_design.prepared_sweeps',
 'sweep_design.utility_functions']

package_data = \
{'': ['*']}

install_requires = \
['emd-signal>=1.2.3,<2.0.0', 'packaging>=22,<23']

extras_require = \
{':python_version >= "3.6" and python_version < "3.8"': ['numpy<=1.19',
                                                         'scipy>=1.2,<1.8',
                                                         'typing_extensions>=3.6'],
 ':python_version >= "3.8"': ['numpy>1.19', 'scipy>=1.8']}

setup_kwargs = {
    'name': 'sweep-design',
    'version': '0.2.0',
    'description': 'Project designed to create and analyze sweep signals.',
    'long_description': '# sweep-design\n\nSimple way to create sweep signal.\n\n## The project is intended for designing sweep signals.\n\nThe package is intended to create and develop sweep signals of\nvarying complexity.\n\nThe project can be used both for educational and work purposes.\n\nIt is convenient to use [`Jupyter Lab`](https://jupyter.org/) or\n[`Jupyter Notebook`](https://jupyter.org/) to speed up the development\nof signals, to compare their parameters with other signals,\nand to visualize them.\n\nThe project is designed so that you can easily change the creation of sweep\nsignals. For example, write your own methods describing how the frequency\nand amplitude will change from the time of the sweep signal.\n\nThe project was made to be able to create various sweep signals: implemented\nand not implemented by a vibration source, from simple ones, like a linear\nsweep signal, to complex ones, like a pseudo-random sweep signal.\n\nTools have been written with which unrealizable sweep signals\ncould be made realizable.\n\nIn addition, documentation consist tutorial how to work with library\nand examples of ready-made sweeps. You can write own sweep creation.\n\n# Installation\n\nTo install use:\n\n```bash\n$ pip install sweep-design\n```\n\nor using `poetry`\n\n```bash\n$ poetry add sweep-design\n```\n\nAlso you can clone or load project from [GitHub](https://github.com/Omnivanitate/sweep-design),\nand install requirement packages using the\n\n```bash\n$ pip install -r requirement.txt\n```\n\nor if you want develop, use\n\n```bash\n$ pip install -r requirement-dev.txt\n```\n\nor\n\n```bash\n$ poetry install\n```\n\nor coping pieces of code and create your own.\n\n## Usage\n\nThe project is a library. Working with it is the same as with\nother third-part libraries of the python language.  \nAn example of how to include the library is described\n[here](https://docs.python.org/3/tutorial/modules.html).\n\nThe library consists sub-modules:\n\n- `sweep_design.config` - contains the project configuration `Config` and `SweepConfig`.\n- `sweep_design.defaults` - contains default methods to calculate.\n- `sweep_design.prepared_sweep` - contains sweep signal templates.\n- `sweep_design.utility_functions` - contains function to work with signals.\n- `sweep_design.core` - contains basic classes `MathOperation` and `RelationProtocol`.\n- `sweep_design.exc` - contains exceptions.\n- `sweep_design.axis` - contains class `ArrayAxis`\n- `sweep_design.relation ` - contains class `Relation`\n- `sweep_design.signal ` - contains class `Signal`\n- `sweep_design.spectrum ` - contains class `Spectrum`\n- `sweep_design.sweep` - contains class `Sweep`\n- `sweep_design.uncalculated` - contains classes `UncalculatedSweep` and `ApriorUncalculatedSweep`\n- `sweep_design.spectrogram` - contains classes `Spectrogram`\n\nFor convenient base classes:\n`ArrayAxis`, `Relation`, `Signal`, `Spectrum`, `Sweep`, `UncalculatedSweep`,\n`ApriorUncalculatedSweep`, `Config`, `ConfigSweep` - can be imported from\na `sweep_design` module.\n\nFor example:\n\n```python\nfrom sweep_design import Signal\n```\n\nUtility functions can be imported from `sweep_design.utility_functions`.  \nAnd prepared sweep - from `sweep_design.prepared_sweep`.\n\n### Quick start. Simple work flow.\n\nBelow is a simple example of creating a sweep signal and visualizing it.\nA more extended description of the work of the library in the documentation.\nOther examples are contained in the examples contains in _Tutorial_ and\n_Prepared sweep_ sections.\n\nFor the following code [`Matplotlib`](https://matplotlib.org/) need be used\nto visualize a result of work. But `Matplotlib` can be replaced with another\nlibrary that you use.\n\n```python\nimport matplotlib.pyplot as plt\n\nfrom sweep_design import ArrayAxis, UncalculatedSweep\n\ntime = ArrayAxis(start=0., end=10., sample=0.01)\n\nusw = UncalculatedSweep(time=time)\nsw = usw()\n\nt_sw, a_sw = sw.get_data()\nplt.plot(t_sw, a_sw)\nplt.xlabel(\'Time, s\')\nplt.ylabel(\'Amplitude\')\nplt.title(\'Sweep-signal\')\n```\n\nResult:\n\n![sweep_with_matplotlib](https://user-images.githubusercontent.com/89973180/156033978-ccc8de40-9f6b-4bb1-b59f-7a3ea41d2f64.png "Linear Sweep")\n\n## Credits\n\n`sweep-design` was created with  \n[`numpy`](https://numpy.org/)  \n[`scipy`](https://scipy.org/)  \n[`EMD-signal`](https://pyemd.readthedocs.io/en/latest/)\n',
    'author': 'Vladislav',
    'author_email': 'serebraykov.vs@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
