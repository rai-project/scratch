===================
carml_python_client
===================


.. image:: https://img.shields.io/pypi/v/carml_python_client.svg
        :target: https://pypi.python.org/pypi/carml_python_client

.. image:: https://img.shields.io/travis/abduld/carml_python_client.svg
        :target: https://travis-ci.org/abduld/carml_python_client

.. image:: https://readthedocs.org/projects/carml-python-client/badge/?version=latest
        :target: https://carml-python-client.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/abduld/carml_python_client/shield.svg
     :target: https://pyup.io/repos/github/abduld/carml_python_client/
     :alt: Updates


Python Boilerplate contains all the boilerplate you need to create a Python package.


* Free software: MIT license
* Documentation: https://carml-python-client.readthedocs.io.



Usage
-----

Go to the `carml_python_client` directory

~~~
cd carml_python_client
~~~

Then use the command line tool to perform the inference. For example

~~~
python cli.py --carml_url impact2.csl.illinois.edu:9099 --urls example.txt
~~~

You will have to make sure that carml is running on the specified url and port.

Modify the `example.txt` file and place your URLs there.

The command line has options that allows you to pick the framework and model to use

~~~
$ python cli.py --help
Usage: cli.py [OPTIONS]

  Console script for carml_python_client.

Options:
  --carml_url TEXT          The URL to the CarML website.
  --urls FILENAME           The file containing all the urls to perform
                            inference on.
  --framework_name TEXT     The framework to use for inference.
  --framework_version TEXT  The framework version to use for inference.
  --model_name TEXT         The model to use for inference.
  --model_version TEXT      The model version to use for inference.
  --help                    Show this message and exit.
~~~

Features
--------

* TODO

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

