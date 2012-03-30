from setuptools import setup, find_packages


version = '0.7'

install_requires = [
    'setuptools',
    'zc.buildout',
    ]


setup(name='zojax.mr.gae',
    version=version,
    description="A zc.buildout extension to ease the development of large projects with lots of packages.",
    long_description='Extention download google_appengine end cteate symlincks to lib in src folder',
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Buildout",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    keywords='gae zojax',
    author='Zojax',
    author_email='',
    url='https://github.com/Zojax/zojax.mr.gae',
    license='GPL',
    packages=find_packages('src'),
    package_dir = {'':'src'},
    namespace_packages=['zojax', 'zojax.mr'],
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points="""
      [zc.buildout.extension]
      default = zojax.mr.gae.extension:extension
      """,

)
