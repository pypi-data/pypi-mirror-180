from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read() 

INSTALL_REQUIRES = []

def doSetup(install_requires):
    setup(
        name='pcr_optimizer',
        version='0.13',
        author=' Lily Torp, K. Lionel Tukei ',
        author_email='ltorp3@uw.edu, ltukei@uw.edu',
        url='https://github.com/Ara101/PCR_Optimization_class.git',
        description='A function for PCR protocal optimization',
        long_description=long_description,
        long_description_content_type='text/markdown',
        packages=['pcr_optimizer'],
        package_dir={'pcr_optimizer':
            'pcr_optimizer'},
        install_requires=install_requires,
        include_package_data=True,
        classifiers=[
            'Development Status :: 3 - Alpha',  
            'Intended Audience :: Science/Research',
            'Topic :: Scientific/Engineering',
            'License :: OSI Approved :: MIT License', 
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
        ],
    )

if __name__ == '__main__':
  doSetup(INSTALL_REQUIRES)
