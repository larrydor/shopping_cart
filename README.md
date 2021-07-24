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

## Setup

### Email Template Setup

Follow [this guide](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/sendgrid.md) to:
  1) Sign up for a SendGrid account, and complete the "Single Sender Verification" using an email address of choice (i.e. the `SENDER_EMAIL_ADDRESS`).
  2) Obtain a SendGrid API Key (i.e. the `SENDGRID_API_KEY`).
  3) Create your own [SendGrid Dynamic Email Template](https://sendgrid.com/dynamic_templates) and locate the template's unique identifier (i.e. the `SENDGRID_TEMPLATE_ID`).
  4) Configure the email template with this [example HTML code](https://github.com/larrydor/shopping_cart/blob/main/email_template.html).

### Credentials Setup

Create a new file called ".env" in the root directory of this repo, then copy the contents below into it, adapting the values to match the `EMAIL_ADDRESS` , `SENDGRID_API_KEY`, and `SENDGRID_TEMPLATE_ID`, obtained in the setup step above. Additionally, create a `TAX_RATE` variable within the .env file to specific your location's specific tax rate.

```sh
# the .env file

SENDER_EMAIL_ADDRESS="me@example.com"
SENDGRID_API_KEY="abc123"
SENDGRID_TEMPLATE_ID="templ789"
TAX_RATE="0.1"
```

> NOTE: the ".env" file is usually the place for passing configuration options and secret credentials, so as a best practice we don't upload this file to version control (which is accomplished via a corresponding entry in the [".gitignore"](/.gitignore) file). This means we need to instruct each person who uses our code needs to create their own local ".env" file.

## Usage

Run the Python script:

```py
python shopping_cart.py
```

> NOTE: if you see an error like "ModuleNotFoundError: No module named '...'", it's because the given package isn't installed, so run the `pip` command above to ensure that package has been installed into the virtual environment.

## Reference
Thank you to Professor Rossetti for providing great assistance during this project, as well as a reference README file and SendGrid configuration instructions within GitHub.
1. Source: https://raw.githubusercontent.com/prof-rossetti/my-first-python-app/main/README.md
1. Source: https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/sendgrid.md#setup
1. Source: https://github.com/s2t2/shopping-cart-with-email-receipts