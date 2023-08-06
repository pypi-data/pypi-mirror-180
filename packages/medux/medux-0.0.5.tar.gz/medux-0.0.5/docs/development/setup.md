# Setup MedUX for Development

For MedUX development, you have to first setup the correct environment. As MedUX stands upon GDAPS' shoulders, and plugins can be distributed via PyPi and developed separately, there are a few caveats. This setup helps you through this process.

Make sure you have `Python 3.6+`, `pip` and `virtualenv` installed.

Clone the MedUX repository:

```bash
git clone git@gitlab.com:nerdocs/medux/medux.git
cd medux
```

Create a virtualenv for Python:

```bash
virtualenv .venv
. ./venv/bin/activate
```

Install all the required dependencies now:

```bash
pip install --upgrade pip
pip install requirements/dev.txt
# python manage.py makemigrations  # see note below
python manage.py migrate
python manage.py syncplugins
```

!!! note

    It might be necessary to do a `makemigrations` before `migrate`: as long as MedUX is <v1.0.0 and the API is not stable, we won't include all Django migrations, because models are still changing a lot. *Never ever* use this software in any production environment, before v1.0.0 is released. Did I say **NEVER**? Right. It'll eat your pets, beware.

The script creates an `admin` user per default, password `admin`.

Now create an `.env` file in the `medux/medux` directory. You can use the `.env.example` file there as a template, and set the variables according to your needs.

```bash
python manage.py runserver
```

Happy coding...

If you want to create a plugin, have a look at the [Developing MedUX plugins][] section