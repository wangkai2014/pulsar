import os
from datetime import datetime, date

import setup
from clean import rmfiles

rmfiles()
script = os.path.abspath(setup.__file__)

assert setup.mod.VERSION[3] == 'final'

with open('CHANGELOG.rst', 'r') as f:
    changelog = f.read()

top = changelog.split('\n')[0]
version_date = top.split(' - ')
assert len(version_date) == 2, 'Top of CHANGELOG.rst must be version and date'
version, datestr = version_date
dt = datetime.strptime(datestr, '%Y-%b-%d').date()
assert dt == date.today()

assert version == 'Ver. %s' % setup.mod.__version__


setup.run(argv=[script, 'sdist'])


print('%s %s ready!' % (setup.package_name, setup.mod.__version__))
