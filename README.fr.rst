======
dockeb
======

.. image:: https://img.shields.io/pypi/v/dockeb.svg
   :target: https://pypi.org/project/dockeb/
   :alt: PyPI

*Documentation also available in* `English <README.rst>`_

**dockeb**, la version Keb de Docker.

**dockeb** peut être utilisé comme remplacement «tel quel» pour l'outil de
`ligne de commande Docker <https://docs.docker.com/engine/reference/commandline/cli/>`_.

La différence entre docker et **dockeb** est la génération de
noms. Tandis que docker génère un nom de la forme ``adjectif_nom`` pour
les containers, **dockeb** génère plutôt un nom Keb aléatoire.

Si par contre un nom est assigné à un container de manière explicite,
via l'option ``--name``, celui-ci demeurera inchangé.

Pré-requis
----------

Pour utiliser **dockeb**, vous aurez besoin de Python ≥ 3.4, ainsi que
de `Docker <https://docs.docker.com/>`_.

Pour l'installation, nous recommandons l'utilisation du gestionnaire
de paquets ``pip``.

Installation
------------

Pour installer **dockeb** sur l'ensemble du système, exécutez:

.. code-block:: sh

   sudo pip3 install dockeb

Pour installer **dockeb** manuellement à partir du code source, les
étapes sont les suivantes:

.. code-block:: sh

   git clone git@github.com:abusque/dockeb.git
   cd dockeb
   sudo ./setup.py install

Utilisation
-----------

Une fois installé, vous pouvez utiliser **qng** avec la commande
suivante:

.. code-block:: sh

   qng

Pour une commande plus intéressante, essayez:

.. code-block:: sh

   dockeb run hello-world
   dockeb ps -a

Vous constaterez qu'un nom Keb aléatoire a été assignée au container à
sa création.

Pour utiliser **dockeb** automatiquement au lieu de docker, vous
pouvez définir un alias dans la configuration de votre shell:

.. code-block:: sh

   alias docker='dockeb'

Développement
-------------

Pour développer **dockeb** localement, vous pouvez utiliser `pipenv
<https://docs.pipenv.org/>`_. Exécutez ``pipenv install --dev`` pour
générer un environnement virtuel (*virtual environment*) dans lequel
les dépendances seront installées. Vous pouvez ensuite utiliser
``pipenv shell`` pour activer cet environnement.

Pour publier de nouvelles versions sur PyPI, nous recommandons
l'utilisation de `Twine <https://pypi.org/project/twine/>`_.

Voir aussi
----------

* `qng <https://github.com/abusque/qng>`_, le générateur de noms Queb.
