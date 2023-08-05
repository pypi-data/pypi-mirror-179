from setuptools import setup

setup(
    name='evinweather',
    packages=['evinweather'],
    version='1.0.0',
    license='MIT',                      # More here: https://help.github.com/articles/licensing-a-repository
    description='Weather forecast data',
    author='Togay Tunca',
    author_email='ttunca@evin-ai.com',
    url='https://github.com/evinai',
    keywords=['weather', 'forecast', 'openweather'],
    install_requires=[
            'requests',
    ],
    requires_python=">=3.5",
    classifiers=[
            'Development Status :: 3 - Alpha',              # Chose either "3 - Alpha", "4 - Beta" or "5 - Production Stable' as the current state.
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Build Tools',
            'License :: OSI Approved :: MIT License',       # Type a license again,

    ],

)
