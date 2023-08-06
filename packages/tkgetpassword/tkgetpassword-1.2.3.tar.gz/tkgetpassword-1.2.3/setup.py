from distutils.core import setup


setup( name = 'tkgetpassword',
       packages = ['tkgetpassword'], # this must be the same as the name above version = '0.1',
    description = 'Logins to enter password, create password, change password and login, simple way to enter password in tkinter, Tkinter.',
       author = 'Leonardo A. Reichert',
       author_email = 'leoreichert5000@gmail.com',
       url = 'https://github.com/LeonardoReichert/tkgetpassword/', # use the URL to the github repo download_url = 'https://github.com/{user_name}/{repo}/tarball/0.1',
       keywords = ["tkinter", "password", "login", "authentication",
                   "password", "tk", "sha256", "hash", "gui"],

       license='MIT',

       version='1.2.3',

    project_urls={
    'Source': 'https://github.com/LeonardoReichert/tkgetpassword/'},
       
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        #'Topic :: Software Development :: Form Tools',
        #'Topic :: Software Development :: Password Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        #'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        ],
       )

