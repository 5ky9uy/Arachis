from setuptools import setup, find_packages
import os

setup(
      name="Arachis",
      version="0.40",
      description="Analyzing ReArrangements with Circular Headed Incomplete Sequences",
      author="Jianjun Jin",
      author_email='jinjianjun@mail.kib.ac.cn',
      url="http://github???",
      license="GNU General Public License, version 3",
      packages=["Arachis"],
      scripts=["scripts/run_pypmag.py", "scripts/compare_grimm_files.py"],
      )

os.system('rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info')