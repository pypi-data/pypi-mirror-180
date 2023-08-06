# Developing MedUX plugins

A MedUX plugin can be developed independently of the main software. You don't need MedUX' git development version for developing plugins, you can develop against the current available PyPi version.

There are some bells and whistles included to make plugin development easier.
MedUX plugins can be developed independently of the main application. Just make sure you use the correct (mostly: current) version of MedUX. In most cases you can use the PyPi package. If you want to use the development version, please have a look how wo install the [Setup Medux for Development][], and continue with the instructions below - just omit the `pip install medux` part.


You should be familiar with creating virtualenvs, and create a virtual python environment for this plugin first.

```bash
mkdir medux-foo-plugin
cd medux-foo-plugin
virtualenv .venv
source .venv/bin/activate
```

Now, within that virualenv, install the necessary packages:

```bash
# just install the MedUX main application from PyPi, and cookiecutter
pip install cookiecutter

# Install the medux main package - omit that if you use the development version
pip install medux

# if you want to automatically find your git username/email...
pip install gitpython
```

MedUX' ``manage.py`` script is placed automatically into the PYTHONPATH, so it's easy to start using its management commands. We've adapted GDAPS' `startplugin` command to create a plugin (this feature uses cookiecutter).

```bash
manage.py startplugin foo
```

Answer the questions (for most of the questions you could just take the default).

Now install your plugin into your virtualenv:

```bash
pip install -e medux-foo
```

so you can instantly start developing it:

```bash
manage.py migrate        #  get the database up and running
manage.py syncplugins    #  sync plugin metadata into the database
manage.py collectstatic  #  collect all staticfiles
manage.py runserver      #  Go!
```

Happy coding!