import os
import subprocess
from setuptools import setup, find_packages
from setuptools.command.build_ext import build_ext
from setuptools.command.install import install

TORCH_VERSION = '1.11.0'
CONDA_PREFIX = os.environ.get("CONDA_PREFIX", None)
WORKING_DIR = os.getcwd()


class Build(build_ext):
    """Customized setuptools build command - builds protos on build."""

    def run(self):
        run_makefile()
        os.chdir(WORKING_DIR)
        self.inplace = 1
        build_ext.run(self)


def makefile_command(gpu: bool):
    if not gpu:
        return ["conda run -n boost make -f Makefile-conda"]
    return ["conda run -n boost make -f Makefile-conda", "conda run -n boost make -f Makefile-gpu"]


def run_makefile():
    # if user use conda run makefile
    if CONDA_PREFIX is not None:
        print("Download version with accelerated calculation.")

        # check if gpu exists
        import torch
        if not torch.cuda.is_available():
            print("Does not support GPU.\nBuild accelerated features.")
            gpu_available = False
        else:
            print("Support GPU.\nBuild accelerated features for GPU.")
            gpu_available = True

        # build Makefile
        os.chdir("graphMeasures/features_algorithms/accelerated_graph_features/src")
        print("cd ed")
        os.system("conda env create -f env.yml --force")
        print("created conda env")

        def conda_base():
            split_path = list(os.path.split(CONDA_PREFIX))
            while "conda" not in split_path[-1]:
                split_path = list(os.path.split(split_path[0]))
            return "/".join(split_path)

        cmd = '. ' + conda_base() + '/etc/profile.d/conda.sh && conda activate boost'
        print(cmd)
        subprocess.call(cmd, shell=True, executable='/bin/bash')
        print("did subprocess thingy")
        for command in makefile_command(gpu_available):
            process = subprocess.Popen(
                command.split(), stdout=subprocess.PIPE)
            print("another subprocessing")
            output = process.stdout.read()
            print(output)
            output, error = process.communicate()
            print(output)
            print(error)

    else:
        print("Does not use Conda environment or Linux.\nDownload version without accelerated calculation.")


if __name__ == '__main__':
    # get text for setup
    with open("requirements.txt") as f:
        requirements = [l.strip() for l in f.readlines()]

    with open("README.md") as r:
        readme = r.read()

    setup(
        name="graph-measures",
        version="0.1.55",
        license="GPL",
        maintainer="Ziv Naim",
        author="Itay Levinas",
        maintainer_email="zivnaim3@gmail.com",
        url="https://github.com/louzounlab/graph-measures",
        description="A python package for calculating "
                    "topological graph features on cpu/gpu",
        long_description=readme,
        long_description_content_type="text/markdown",
        keywords=["gpu", "graph", "topological-features-calculator"],
        description_file="README.md",
        license_files="LICENSE.rst",
        install_requires=requirements,
        packages=find_packages('.'),
        python_requires=">=3.6.8",
        package_data={'': ['*.pkl']},
        include_package_data=True,
        has_ext_modules=lambda: True,
        package_dir={"": "."},
        # cmdclass={
        #     'build_ext': Build
        #     # 'install': Install,
        # },
        classifiers=[
            'Programming Language :: Python',
            'Programming Language :: C++',
            'Operating System :: Unix',
            'Operating System :: POSIX :: Linux',
        ],
        easy_install="ok_zip"
    )
