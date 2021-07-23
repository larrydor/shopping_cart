# Shopping Cart Project

A Python business application that automates the checkout process for a local grocery store.

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation

Fork this [remote repository](https://github.com/larrydor/shopping_cart) under your own control, then "clone" or download your remote copy onto your local computer.

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

```sh
cd ~/Desktop/shopping_cart
```
Use Anaconda to create and activate a new virtual environment, perhaps called "shopping-env":

```sh
conda create -n shopping-env python=3.8
conda activate shopping-env
```

After activating the virtual environment, install package dependencies (see the ["requirements.txt"](/requirements.txt) file):

```sh
pip install -r requirements.txt
```

> NOTE: if this command throws an error like "Could not open requirements file: [Errno 2] No such file or directory", make sure you are running it from the repository's root directory, where the requirements.txt file exists (see the initial `cd` step above).

## Configuration

Follow these [SendGrid setup instructions](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/sendgrid.md#setup) to sign up for a SendGrid account, configure your account's email address (i.e. `SENDER_EMAIL_ADDRESS`), and obtain an API key (i.e. `SENDGRID_API_KEY`). Also you will need to create a SendGrid Dynamic Email Template to programmatically display order contents. 

## Setup

Create a new file called ".env" in the root directory of this repo, and paste the following contents inside, using your own values as appropriate:

```sh
# required contents for ".env" file:
SENDGRID_API_KEY="_______________"
SENDGRID_TEMPLATE_ID="_____________"
SENDER_EMAIL_ADDRESS="_______________"
TAX_RATE="______"
```

> NOTE: Please, create a TAX_RATE variable within the .env file to specific your location's specific tax rate.

> NOTE: the ".env" file is usually the place for passing configuration options and secret credentials, so as a best practice we don't upload this file to version control (which is accomplished via a corresponding entry in the [".gitignore"](/.gitignore) file). This means we need to instruct each person who uses our code needs to create their own local ".env" file.

## Usage

Run the Python script:

```py
python shopping_cart.py
```

> NOTE: if you see an error like "ModuleNotFoundError: No module named '...'", it's because the given package isn't installed, so run the `pip` command above to ensure that package has been installed into the virtual environment.

## Reference
Thank you to Professor Rossetti for providing a reference README file and SendGrid configuration instructions.
Source: https://raw.githubusercontent.com/prof-rossetti/my-first-python-app/main/README.md
Source: https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/sendgrid.md#setup