from setuptools import setup, find_packages
setup(
    name = "script-provisioner",
    version = "0.1.0",
    packages = find_packages(),
    namespace_packages = ( 'aminatorplugins', ),

    data_files = [
        ('/etc/aminator/plugins', ['default_conf/aminatorplugins.cloud.euca.yml']),
    ],

    entry_points = {
       'aminator.plugins.cloud': [
           'euca = aminatorplugins.cloud.euca:EucaCloudPlugin',
       ],
    },

    # metadata for upload to PyPI
    author = "Vic Iglesias",
    author_email='viglesiasce@gmail.com',
    url='https://github.com/aminator-plugins/eucalyptus',
    description = "Eucalyptus Cloud Plugin for Netflix's Aminator",
    long_description=open('README.rst').read(),
    license=open("LICENSE.txt").read(),
    keywords = "aminator plugin eucalyptus",
    classifiers=(
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Topic :: System :: Installation/Setup',
        'Topic :: Utilities',
    )

)
