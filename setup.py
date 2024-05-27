from setuptools import setup, find_packages

setup(
    name='academia_tts',
    version='0.1a',
    packages=find_packages(),
    install_requires=[
        'torch',
        'python-pptx',
        'whisperspeech',
        'pydub',
    ],
    entry_points={
        'console_scripts': [
            'tts_output_wav=academia_tts.scripts.tts_output_wav:main',
            'tts_pptx=academia_tts.scripts.tts_pptx:main',
        ],
    },
    author='l1997i',
    author_email='i@l1997i.com',
    description='A package to convert PPTX slide notes to audio and embed them into the slides',
    long_description='A package to convert PPTX slide notes to audio and embed them into the slides',
    url='https://github.com/l1997i/academia_tts',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)