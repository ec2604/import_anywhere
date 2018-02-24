from distutils.core import setup
setup(name='import_anywhere',
      version='1.3',
      description='Python Package allowing relative imports, no dependence on where python is run from',
      long_description= "Python Package allowing relative imports, no dependence on where python is run from."
                        "This allows python"
                       " to run python files with relative imports, without running from the source folder."
                       " All parent directories must be specified in environment variable IMPORT_ANYWHERE_DIRS",
      author='Era Choshen',
      author_email='erachoshen@gmail.com',
      license='MIT',
      packages=['import_anywhere'],
      url= 'https://github.com/ec2604/import_anywhere',
      download_url='https://github.com/ec2604/import_anywhere/archive/1.3.tar.gz',
      keywords=['relative_import'],
      python_requires = '>=3',
     )