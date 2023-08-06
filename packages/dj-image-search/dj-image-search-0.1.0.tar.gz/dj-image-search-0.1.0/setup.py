from setuptools import setup, find_packages

setup(
        name="dj-image-search",
        version="0.1.0",
        packages=find_packages(),
        include_package_data=True,
        install_requires=[
            'click',
            'keyboard',
            'climage',
            'urllib3',
            'google-search-results',
            ],
        entry_points={
            'console_scripts': [
                'djsearch = dj_search.djsearch:image',

                ],
            },

        )
