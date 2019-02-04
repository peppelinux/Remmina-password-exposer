from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='remmina-password-exposer',
      version='0.3',
      description="Print remmina password in clear",
      long_description=readme(),
      classifiers=['Development Status :: 5 - Production/Stable',
                  'License :: OSI Approved :: BSD License',
                  'Programming Language :: Python :: 2',
                  'Programming Language :: Python :: 3'],
      url='https://github.com/peppelinux/Remmina-password-exposer',
      author='Giuseppe De Marco',
      author_email='giuseppe.demarco@unical.it',
      license='BSD',
      scripts=['remmina_password_exposer/remmina_password_exposer.py'],
      packages=['remmina_password_exposer'],
      install_requires=[
                      'pycrypto'
                  ],
     )
