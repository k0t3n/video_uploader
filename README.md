# Video uploader

Video uploader is Django-based application used for uploading, saving and transcoding video files. This app is part of
the Stepik interview.

## Setting up development environment

### System Requirements

* Python 3.9
* [Poetry](https://python-poetry.org/docs/)
* MySQL client

### Installation

Virtual environment:
> poetry env use python3.9

Packages:
> poetry install

### Configuration

Configure MySQL using script:
> mysql -e "source scripts/db_init.sql"k

Create .env file and configure params
> cp .env.example .env
