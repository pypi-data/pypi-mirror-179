# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pypath',
 'pypath.biocypher',
 'pypath.core',
 'pypath.data',
 'pypath.formats',
 'pypath.inputs',
 'pypath.internals',
 'pypath.legacy',
 'pypath.obsolete',
 'pypath.obsolete.old_manuscript',
 'pypath.omnipath',
 'pypath.omnipath.databases',
 'pypath.omnipath.server',
 'pypath.reader',
 'pypath.resources',
 'pypath.resources.data',
 'pypath.share',
 'pypath.share.lookup',
 'pypath.utils',
 'pypath.visual',
 'pypath.visual.igraph_drawing']

package_data = \
{'': ['*'], 'pypath.data': ['licenses/*', 'www/*']}

install_requires = \
['PyYAML',
 'beautifulsoup4',
 'dill',
 'future',
 'glom',
 'lxml',
 'matplotlib',
 'numpy',
 'openpyxl',
 'pandas',
 'pycurl',
 'pyreadr',
 'rdata',
 'requests',
 'scipy',
 'tabulate',
 'timeloop',
 'toml',
 'tqdm',
 'xlrd']

extras_require = \
{'bel': ['pybel', 'bio2bel', 'click'], 'graph': ['python-igraph']}

entry_points = \
{'bio2bel': ['omnipath = pypath.omnipath.bel'],
 'console_scripts': ['bio2bel_omnipath = pypath.omnipath.bel:main']}

setup_kwargs = {
    'name': 'pypath-omnipath',
    'version': '0.14.30',
    'description': 'Molecular signaling prior knowledge processing',
    'long_description': "============================================================================\n*pypath:* A Python module for molecular signaling prior knowledge processing\n============================================================================\n\n|Demo|\n\nOmniPath\n========\n\nAre you interested in OmniPath data? Check out our R package OmnipathR_,\nthe most popular and most versatile access point to OmniPath, a database\nbuilt from more than 150 original resources. If you use Python and don't\nneed to build the database yourself, try our `Python client`_. Read more\nabout the `web service here`_.\n\n.. _OmnipathR: https://saezlab.github.io/OmnipathR\n.. _`Python client`: https://github.com/saezlab/omnipath\n.. _`web service here`: https://pypath.omnipathdb.org/webservice.html\n\nDo you need pypath?\n===================\n\nPypath is the database builder of OmniPath. For most people the data\ndistributed in OmniPath is satisfying (see above), they don't really need\npypath. Typically you need pypath to:\n\n* Build a custom or very fresh version of the OmniPath database(s)\n* Use one of the utilities such as ID translation, homology translation, etc.\n  (see the `utils module`_)\n* Access the raw or preprocessed data directly from the original resources\n  (see the `inputs module`_)\n\n.. _`utils module`: https://github.com/saezlab/pypath/tree/master/pypath/utils\n.. _`inputs module`: https://github.com/saezlab/pypath/tree/master/pypath/inputs\n\nInstallation\n============\n\n**From PyPI:**\n\n.. code:: bash\n\n    pip install pypath-omnipath\n\n**From Git:**\n\n.. code:: bash\n\n    pip install git+https://github.com/saezlab/pypath.git\n\nDocs\n====\n\nRead the `reference documentation`_ or check out the tutorials_.\n\n.. _`reference documentation`: https://pypath.omnipathdb.org/\n.. _tutorials: https://workflows.omnipathdb.org/\n\nThe *Pypath guide*, the comprehensive tutorial for pypath is currently out\nof date, we are very sorry about that!\n\nGet help\n========\n\nShould you have a question or experiencing an issue, please write us by\nthe `Github issues`_ page.\n\nFeatures\n========\n\n**pypath** is a Python module for processing molecular biology data resources,\ncombining them into databases and providing a versatile interface in Python\nas well as exporting the data for access through other platforms such as\nR_, `web service`_, Cytoscape_ and BEL (Biological Expression Language).\n\n.. _R: https://github.com/saezlab/OmnipathR\n.. _`web service`: https://omnipathdb.org/\n.. _Cytoscape: https://apps.cytoscape.org/apps/omnipath\n\n**pypath** provides access to more than 100 resources! It builds 5 major\ncombined databases and within these we can distinguish different datasets.\nThe 5 major databases are interactions (molecular interaction network or\npathways), enzyme-substrate relationships, protein complexes, molecular\nannotations (functional roles, localizations, and more) and inter-cellular\ncommunication roles.\n\n**pypath** consists of a number of submodules and each of them again contains\na number of submodules. Overall **pypath** consists of around 100 modules.\nThe most important higher level submodules:\n\n* *pypath.core:* contains the database classes e.g. network, complex,\n  annotations, etc\n* *pypath.inputs:* contains the resource specific methods which directly\n  downlad and preprocess data from the original sources\n* *pypath.omnipath:* higher level applications, e.g. a database manager, a\n  web server\n* *pypath.utils:* stand alone useful utilities, e.g. identifier translator,\n  Gene Ontology processor, BioPax processor, etc\n\nIntegrated databases\n--------------------\n\nIn the beginning the primary aim of ``pypath`` was to build networks from\nmultiple sources using an igraph object as the fundament of the integrated\ndata structure. From version 0.7 and 0.8 this design principle started to\nchange. Today ``pypath`` builds a number of different databases, exposes them\nby a rich API and each of them can be converted to ``pandas.DataFrame``.\nThe modules and classes responsible for the integrated databases are located\nin ``pypath.core``. The five main databases are the followings:\n\n* *network* - ``core.network``\n* *enzyme-substrate* - ``core.enz_sub``\n* *complexes* - ``core.complex``\n* *annotations* - ``core.annot``\n* *intercell* - ``core.intercell``\n\nSome of the databases have different variants (e.g. PPI and transcriptional\nnetwork) and all can be customized by many parameters.\n\nDatabase management\n-------------------\n\nThe databases above can be loaded by calling the appropriate classes.\nHowever building the databases require time and memory so we want to avoid\nbuilding them more often than necessary or keeping more than one copies\nin the memory. Some of the modules listed above have a method ``get_db``\nwhich ensures only one instance of the database is loaded. But there is a\nmore full featured database management system available in **pypath**,\nthis is the **pypath.omnipath** module. This module is able to build the\ndatabases, automatically saves them to ``pickle`` files and loads them from\nthere in subsequent sessions. **pypath** comes with a number of database\ndefinitions and users can add more. The ``pickle`` files are located by\ndefault in the ``~/.pypath/pickles/`` directory. With the ``omnipath``\nmodule it's easy to get an instance of a database. For example to get the\n`omnipath` PPI network dataset:\n\n.. code:: python\n\n    from pypath import omnipath\n    op = omnipath.db.get_db('omnipath')\n\n**Important:** Building the databases for the first time requires the\ndownload of several MB or GB of data from the original resources. This\nnormally takes long time and is prone of errors (e.g. truncated or empty\ndownloads due to interrupted HTTP connection). In this case you should check\nthe log to find the path of the problematic cache file, check the contents\nof this file to find out the reason and possibly delete the file to ensure\nanother download attempt when you call the database build again. Sometimes\nthe original resources change their content or go offline. If you encounter\nsuch case please open an issue at https://github.com/saezlab/pypath/issues\nso we can fix it in ``pypath``. Once all the necessary contents are\ndownloaded and stored in the cache, the database builds are much faster,\nbut still can take minutes.\n\nFurther modules in pypath\n-------------------------\n\nApart from the databases, **pypath** has many submodules with standalone\nfunctionality which can be used in other modules and scripts. Below we\npresent a few of these.\n\nID conversion\n-------------\n\nThe ID conversion module ``utils.mapping`` translates between a large variety\nof gene, protein, miRNA and small molecule ID types. It has the feature to\ntranslate secondary UniProt ACs to primaries, and Trembl ACs to SwissProt,\nusing primary Gene Symbols to find the connections. This module automatically\nloads and stores the necessary conversion tables. Many tables\nare predefined, such as all the IDs in **UniProt mapping service,** while\nusers are able to load any table from **file** using the classes provided\nin the module ``input_formats``. An example how to translate identifiers:\n\n.. code:: python\n\n    from pypath.utils import mapping\n    mapping.map_name('P00533', 'uniprot', 'genesymbol')\n    # {'EGFR'}\n\n\nHomology translation\n--------------------\n\nThe ``pypath.utils.homology`` module is able to find the orthologs of genes\nbetween two organisms. It uses data both from NCBI HomoloGene, Ensembl and\nUniProt. This module is really simple to use:\n\n.. code:: python\n\n    from pypath.utils import homology\n    homology.translate('P00533', 10090) # translating the human EGFR to mouse\n    # ['Q01279'] # it returns the mouse Egfr UniProt AC\n\nIt is able to handle any ID type supported by ``pypath.utils.mapping``.\nAlternatively, you can access a complete dictionary of orthologous genes,\nor translate columns in a pandas data frame.\n\nFAQ\n===\n\n**Does it run on my old Python?**\n\nMost likely it doesn't. The oldest supported version, currently 3.9, is\ndefined in our `pyproject.toml`_.\n\n.. _`pyproject.toml`: https://github.com/saezlab/pypath/blob/master/pyproject.toml\n\n**Is there something similar in R?**\n\n`OmniPath's R client`_, besides accessing data from OmniPath, provides many\nsimilar services as pypath: `ID translation`_, `homology translation`_,\n`taxonomy support`_, `GO support`_, and many more.\n\n.. _`OmniPath's R client`: https://saezlab.github.io/OmnipathR\n.. _`ID translation`: https://saezlab.github.io/OmnipathR/reference/translate_ids.html\n.. _`homology translation`: https://saezlab.github.io/OmnipathR/reference/homologene_uniprot_orthology.html\n.. _`taxonomy support`: https://saezlab.github.io/OmnipathR/reference/ncbi_taxid.html\n.. _`GO support`: https://saezlab.github.io/OmnipathR/reference/go_annot_download.html\n\n`Questions about OmniPath`_\n\n.. _`Questions about OmniPath`: https://omnipathdb.org/#faq\n\nContact\n=======\n\nWe prefer to keep all communication within the `Github issues`_. About private\nor sensitive matters feel free to contact us by omnipathdb@gmail.com.\n\n.. _`Github issues`: https://github.com/saezlab/pypath/issues\n\nImpressum\n=========\n\n``pypath`` is developed in the `Saez Lab`_ by `Dénes Türei`_, Sebastian\nLobentanzer and Ahmet Rifaioglu, and Erva Ulusoy and Tennur Kılıç in\n`Volkan Atalay's group`_. Olga Ivanova and Nicolàs Palacio also\ncontributed in the past. The `R package`_ and the `Cytoscape app`_ are\ndeveloped and maintained by Francesco Ceccarelli, Attila Gábor, Alberto\nValdeolivas, Dénes Türei and Nicolàs Palacio. The `Python client`_ for the\nOmniPath web service has been developed and is maintained by Michael Klein\nin the group of `Fabian Theis`_.\n\n.. _`Saez Lab`: https://saezlab.org/\n.. _`Volkan Atalay's group`: https://blog.metu.edu.tr/vatalay/\n.. _`Dénes Türei`: https://denes.omnipathdb.org/\n.. _`R package`: https://saezlab.github.io/OmnipathR\n.. _`Cytoscape app`: https://apps.cytoscape.org/apps/omnipath\n.. _`Fabian Theis`: https://www.helmholtz-munich.de/en/icb/research-groups/theis-lab\n\nHistory and releases\n====================\n\nSee here_ a bird eye view of pypath's development history. For more details\nabout recent developments see the `Github releases`_.\n\n.. _here: https://pypath.omnipathdb.org/releasehistory.html\n.. _`Github releases`: https://github.com/saezlab/pypath/releases\n\n.. |Demo| image:: https://raw.githubusercontent.com/saezlab/pypath/master/docs/source/_static/img/pypath-demo.webp\n",
    'author': 'Denes Turei',
    'author_email': 'turei.denes@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://omnipathdb.org/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
