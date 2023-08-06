import setuptools

setuptools.setup(
  name='nonebot_plugin_xiuxian',  # How you named your package folder (MyLib)
  packages=['nonebot_plugin_xiuxian',
            "nonebot_plugin_xiuxian/xiuxian_bank",
            "nonebot_plugin_xiuxian/xiuxian_boss",
            "nonebot_plugin_xiuxian/xiuxian_work",
            "nonebot_plugin_xiuxian/xiuxian_sect",
            "nonebot_plugin_xiuxian/xiuxian_info",
            "nonebot_plugin_xiuxian/xiuxian_buff",
            "nonebot_plugin_xiuxian/xiuxian_back",
            "nonebot_plugin_xiuxian/xiuxian_mixelixir",
            "nonebot_plugin_xiuxian/xiuxian_rift"],  # Chose the same as "name"
  include_package_data=True,
  version='0.4.32',  # Start with a small number and increase it with every change you make
  license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description='xiuxian模拟器',  # Give a short description about your library
  author='PinkCat',  # Type in your name
  author_email='578043031@qq.com',  # Type in your E-Mail
  url='https://github.com/s52047qwas/nonebot_plugin_xiuxian',
  # Provide either the link to your github or to your website
  # packages=setuptools.find_packages(),
  keywords=['plugin', 'nonebot2', 'xiuxian'],  # Keywords that define your package best
  install_requires=[
    'nonebot2',
    'nonebot-adapter-onebot'
  ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',  # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  # Again, pick a license
    'Programming Language :: Python :: 3.9',
  ],
)
