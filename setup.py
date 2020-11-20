from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

setup(
    name='slayerCuda',
    ext_modules=[
        CUDAExtension(
            name='slayerCuda',
            sources=[
                'src/cuda/slayerKernels.cu'
            ],
            depends=[
                'src/cuda/spikeKernels.h',
                'src/cuda/convKernels.h',
                'src/cuda/shiftKernels.h'
            ],
            extra_compile_args={
                'cxx': ['-g'],
                'nvcc': ['-arch=sm_60', '-O2', '-use_fast_math']
            }
        )
    ],
    cmdclass={'build_ext': BuildExtension},
    install_requires=[
        'matplotlib>=2.2.3',
        'numpy>=1.18.5',
        'pickleshare>=0.7.5',
        'PyYAML>=5.3.1',
        'torchvision>=0.6.1',
        ],
)

setup(
    name='slayerLoihiCuda',
    ext_modules=[
        CUDAExtension(
            name='slayerLoihiCuda',
            sources=[
                'src/cuda/slayerLoihiKernels.cu'
            ],
            depends=[
                'src/cuda/spikeLoihiKernels.h'
            ],
            extra_compile_args={
                'cxx': ['-g'],
                'nvcc': ['-arch=sm_60', '-O2', '-use_fast_math']
            }
        )
    ],
    cmdclass={'build_ext': BuildExtension},
    install_requires=[
        'matplotlib>=2.2.3',
        'numpy>=1.18.5',
        'pickleshare>=0.7.5',
        'PyYAML>=5.3.1',
        'torchvision>=0.6.1',
        ],
)

setup(
    name='slayerSNN',
    packages = ['slayerSNN'],
    package_dir = {'slayerSNN': 'src'},
    install_requires = [
        'matplotlib>=2.2.3',
        'numpy>=1.18.5', 
        'pickleshare>=0.7.5',
        'PyYAML>=5.3.1',
        'torchvision>=0.6.1',
        ],
)
