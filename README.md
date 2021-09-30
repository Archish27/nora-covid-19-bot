![Nora Bot](./logo-white.png)

# Nora Bot - Covid-19

Corona Virus Self Awareness Bot that addresses typical questions about the COVID-19 virus to help you to know about corona virus. It provides awarness about Covid-19 social distancing, self isolation, quarantine.

## ✨ How to contribute
--------

I am very happy to receive and merge your contributions into this repository!

To contribute via pull request, follow these steps:

1. Create an issue describing the feature you want to work on (or
   have a look at the [issues](https://github.com/browserstack/ws-reconnect-proxy/issues))
2. Write your code
3. Create a pull request describing your changes

Your pull request will be reviewed by me, will get back to you about any necessary changes or questions.

## ⚡️ Development Internals
----------
### 🔨 1. Install the Python development environment on your system 

```shell
python3 --version
pip3 --version
virtualenv --version1
```
> Requires Python 3.6–3.7.7 and pip >= 19.0

If these packages are already installed, skip to the next step.\
Otherwise, install Python, the pip package manager, and Virtualenv:

- **Windows**
  Install the Microsoft Visual C++ Redistributable for Visual Studio 2015, 2017, and 2019. Starting with the TensorFlow 2.1.0 version, the msvcp140_1.dll file is required from this package (which may not be provided from older redistributable packages). The redistributable comes with Visual Studio 2019 but can be installed separately:

1. Go to the [Microsoft Visual C++ downloads](https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads/),
2. Scroll down the page to the Visual Studio 2015, 2017 and 2019 section.
3. Download and install the Microsoft Visual C++ Redistributable for Visual Studio 2015, 2017 and 2019 for your platform.
   Make sure [long paths are enabled](https://superuser.com/questions/1119883/windows-10-enable-ntfs-long-paths-policy-option-missing) on Windows.

Install the 64-bit [Python 3 release for Windows](https://www.python.org/downloads/windows/) (select pip as an optional feature).

- **mac OS**
  - Install using the [Homebrew](https://brew.sh/) package manager:
  ```shell
    $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    $ export PATH="/usr/local/bin:/usr/local/sbin:\$PATH"
    $ brew update
    $ brew install python # Python 3
    $ sudo pip3 install -U virtualenv # system-wide install
  ```

- **Ubuntu**

  ```shell
  $ sudo apt update
  $ sudo apt install python3-dev python3-pip
  $ sudo pip3 install -U virtualenv # system-wide install
  ```

```
pip3 install -U pip virtualenv
```


### 🔧 2. Create a virtual environment (recommended) 

Python virtual environments are used to isolate package installation from the system.

- **Ubuntu / mac OS**

  - Create a new virtual environment by choosing a Python interpreter and making a `./venv` directory to hold it:
    `virtualenv --system-site-packages -p python3 ./venv`

  - Activate virtual environment\
    `source ./venv/bin/activate`

  - When virtualenv is active, your shell prompt is prefixed with (venv).

  - Install packages within a virtual environment without affecting the host system setup. Start by upgrading pip:

    ```shell
    (venv) $ pip install --upgrade pip

    (venv) $ pip list  # show packages installed within the virtual environment
    ```

  - And to exit virtualenv later:
    `(venv) $ deactivate`

* **Windows**

  - Create a new virtual environment by choosing a Python interpreter and making a .\venv directory to hold it:

    `virtualenv --system-site-packages -p python3 ./venv`

  - Activate the virtual environment:

    `.\venv\Scripts\activate`

  - Install packages within a virtual environment without affecting the host system setup. Start by upgrading pip:

    ````shell
    pip install --upgrade pip
    pip list  # show packages installed within the virtual environment```
    ````

  - And to exit virtualenv later:

    ```shell
      deactivate # don't exit until you're done using TensorFlow
    ```

### 🚀 3. Project Setup 

```shell
(venv) $ pip install rasa
```

> Note: Run this in virtual environment. If issues regarding installing raise issues.

## 🧠 How to train bot

`rasa train`

## ✅ How to run Nora bot

### Rasa Server

`rasa run --enable-api --cors '*'`

> [http://localhost:5005/](http://localhost:5005/)

### Rasa Action Server

`rasa run actions`

> [http://localhost:5055/](http://localhost:5055/)

### Run Nora bot ui

`npm run start`

> [http://localhost:3000/](http://localhost:/3000)

#  👩‍💻  !Happy Coding! 🧑‍💻
