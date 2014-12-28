from setuptools import setup, find_packages

setup(name='tlm',
      version='0.0.1',
      description='matrix library of thin layer method',
      author='Tetsuo Koyama',
      author_email='tkoyama010@gmail.com',
      url='https://tkoyama010@bitbucket.org/tkoyama010/tlm.git',
      packages=find_packages(),
      entry_points="""
      [console_scripts]
      greet = tlm.tlm:main
      """,)
