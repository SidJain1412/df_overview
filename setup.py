from setuptools import setup

setup(name='df_overview',
      version='0.3',
      description='Quick overview of a dataframe, for data analysis.',
      url='http://github.com/SidJain1412/df_overview',
      author='Siddharth Jain',
      author_email='sidjain1412@gmail.com',
      license='MIT',
      packages=['df_overview'],
      zip_safe=False,
      install_requires=[
          'pandas>=0.23.4',
          'numpy>=1.14.2',
          'seaborn>=0.8.1',
          'scipy>=1.0.0',
          'matplotlib>=2.1.2',
      ],
      long_description='A python package to do basic data analysis of your dataframe with just one line of code',
      )
