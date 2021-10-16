

# Build your own audio processing package using Poetry

Workshop materials for a [PyLadies Hamburg event](https://www.meetup.com/PyLadies-Hamburg/events/278588912/) on October 19, 2021.

The purpose of this workshop is to familiarize people with sound and to build their own audio processing package via Poetry. 

# Getting Started

## Audio *only*:

If you are only interested in the audio portion, all you have to do is **click on the `launch binder` button above.** 

There you can participate in the prepared *programming challenges*. (Answers can be found in the subfolder `reference_notebooks`.)

### Requirements:

Internet and probably just a phone/ tablet/ laptop. Possibly headphones as well, if you don't want to disturb others.

## Package development:

If you want to partake in the audio section from *your local machine* **or** you want to *build your own package*, your machine should have the following installed:

### System Requirements:

- Python 3 
- [Poetry](https://python-poetry.org/docs/) (I use verion 1.1.6 but other versions probably work)

#### Why Poetry?

1) Poetry installs everything in a virtual environment, **not** on your system. This helps avoid messy package conflicts messing up your system.

2) Once you finish your packge, it is easy to share the functionality

3) Poetry figures out the best versions of all the packages to ensure they are compatible. If no compatible versions can be found, Poetry returns a suggestion like this one: 

```
For scipy, a possible solution would be to set the `python` property to ">=3.8,<3.10"
```

# Instructions for using Poetry:

Let's set up our Poetry package and development environment.

## 1. Download code and audio files

Clone/download this repository, which includes the necessary code and 4 example audio files to experiment with.

Then set the resulting folder, `build-acoustics-package-with-poetry`, as your current working directory.

Using [git](https://git-scm.com/) you can do this by typing into your console:

```bash
$ git clone https://gitlab.com/airose/build-acoustics-package-with-poetry.git
$ cd build-acoustics-package-with-poetry
```

## 2. Set up your new pacakge with Poetry

Type into your console:

```bash
$ poetry new pyladies_acoustics
```

If it works, you should get this output:

```
Created package pyladies_acoustics in pyladies_acoustics
```

This will create the following folder architecture:

```
├── pyladies_acoustics                                                  
│   ├── pyproject.toml                                      
│   ├── README.rst                                  
│   │   ├── pyladies_acoustics                                                                     
│   │   │   ├── __init__.py                             
│   │   ├── tests            
│   │   │   │   ├── __init__.py             
│   │   │   │   ├── test_pyladies_acoustics.py                  
```

Great! 

Poetry saves the dependencies we want in `pyproject.toml`. We indicate which dependencies we need for the package via `poetry add` and which dependencies we need for development via `poetry add -d`.

## 3. Add basic dependencies

Set the new package as the current working directory and add some dependencies for handling audio data.

[Scipy](http://scipy.github.io/devdocs/tutorial/index.html) is a wonderful package that is **easy to install across environments**. We can load and save wav files and do some pretty cool stuff with audio. [Matplotlib](https://matplotlib.org/) is a package we can use for visualizing our audio.

Advanced users: try adding [librosa](https://librosa.org/doc/latest/index.html) as well. Note: you might need some additional packages installed on your system, however, which you will have to figure out on your own.


```bash
$ cd pyladies_acoustics
pyladies_acoustics$ poetry add matplotlib
pyladies_acoustics$ poetry add scipy
```

When running this last line, I got the following error:

```
  SolverProblemError

  The current project's Python requirement (>=3.8,<4.0) is not compatible with some of the required packages Python requirement:
    - soundpy requires Python >=3.7,<3.10, so it will not be satisfied for Python >=3.10,<4.0
  
  Because pyladies-acoustics depends on soundpy (0.1.0a4) which requires Python >=3.7,<3.10, version solving failed.

  For scipy, a possible solution would be to set the `python` property to ">=3.8,<3.10"
```

I will open the `pyproject.toml` file and adjust this line:

```
[tool.poetry.dependencies]
python = "^3.8"
```

to this:

```
[tool.poetry.dependencies]
python = ">=3.8,<3.10"
```

When I add `scipy` again, it works. You might get a different conflict depending on which Python version you have installed on your computer.

## 4. Add development dependencies

These are dependencies we use only when building our package. We will build onto our package using [Jupyter Lab](https://jupyterlab.readthedocs.io/en/stable/). Let's install it. 

```bash
pyladies_acoustics$ poetry add -D jupyterlab
```

## 5. Install your new package

In order to import our package into our Jupyter Lab environment, we need to install it into our virtual environment (created by Poetry).

```bash
pyladies_acoustics$ poetry install
```

## 6. Run Jupyter Lab and start messing around!

```bash
pyladies_acoustics$ poetry run jupyter lab
```
## 7. Inside Jupyter Lab:

Import your package and other dependencies in the first cell:

```
import pyladies_acoustics as pa
import scipy
import numpy as np # was installed with scipy
```

Any time you add functionality to your package, restart the kernel and rerun the cells; you will be able to use your updated pacakge!

If you need more packages installed, all you have to do is type the folling in your bash:

```bash
pyladies_acoustics$ poetry add <package>
pyladies_acoustics$ poetry update
```

and restart your Jupyter Lab kernel.

## 8. Ready to share your package?

When you are done with adding functionality and you want to share your package with your team, type into your bash:

```bash
pyladies_acoustics$ poetry build
```

Then you can share the produced file `dist/<pacakge>.tar.gz` and others can install it via `pip install` or of course via `poetry add`. For an example, look in the local folder `soundpy`. I will install that package in the Part1 notebook, available to interact with via the `launch binder` button at the top of this page or to simply look at by navigating [here](https://gitlab.com/airose/build-acoustics-package-with-poetry/-/blob/main/notebooks/part1_audio.ipynb).