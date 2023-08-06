from setuptools import setup

setup(name='1Q847',
      version='1.1.8',
      description='模拟操作',
      url='https://github.com/qxt514657/',
      author='1Q847',
      author_email='976671673@qq.com',
      license='MIT',
      packages=['Dll'],  # 包名
      package_data={'Dll': ['dm.dll', 'DmReg.dll']},
      install_requires=[
          'pywin32', 'comtypes'
      ],
      python_requires='>=3.7',
      )
