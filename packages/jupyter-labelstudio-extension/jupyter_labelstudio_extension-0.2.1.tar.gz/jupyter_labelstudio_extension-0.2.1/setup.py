from setuptools import setup, find_packages

__import__('setuptools').setup()



setup(
  name="jupyter_labelstudio_extension",
  version="0.0.1",
  packages=find_packages(),
  py_modules=['jupyter_labelstudio_extension'],
#   entry_points={
#       'jupyter_serverproxy_servers': [
#           # name = packagename:function_name
#           'labelstudio = jupyter_labelstudio_extension:launch_server',
#       ]
#   },
  install_requires=['label_studio_sdk'],
)
