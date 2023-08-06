import setuptools


def long_description():
    with open('README.md', 'r') as file:
        return file.read()


setuptools.setup(
    name='git-lfs-http-mirror',
    version='0.0.1',
    author='Department for International Trade',
    author_email='sre@digital.trade.gov.uk',
    description='Simple Python server to serve a read only HTTP mirror of git repositories that use Large File Storage (LFS)',
    long_description=long_description(),
    long_description_content_type='text/markdown',
    url='https://github.com/uktrade/git-lfs-http-mirror',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Version Control :: Git',
    ],
    python_requires='>=3.7.4',
    install_requires=[
        'flask>=2.2.2',
        'httpx>=0.23.1',
        'waitress>=2.1.2',
    ],
    py_modules=[
        'git_lfs_http_mirror',
    ],
)
