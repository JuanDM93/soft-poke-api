# soft-poke-api

Pokemon Teams API

This is a simple API that allows you to create and manage Pokemon teams. It is built using Django and Django Rest Framework.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need to have [Python 3](https://www.python.org/downloads/) installed on your machine.

Once cloned, you may want to create a virtual environment for the project. You can do so by running the following command:

```bash
python3 -m venv venv
```

#### Installing

To install the project dependencies, run the following command:

```bash
pip install -r requirements.txt
```

#### Database

The project uses [PostgreSQL](https://www.postgresql.org/) as its database. You will need to have it installed on your machine.

Once installed, you will need to create a database for the project. You can do so by running the following command:

```bash
createdb soft-poke-api-db
```

#### Migrations

You will need to run the migrations for the project. You can do so by running the following command:

```bash
python manage.py migrate
```

### Running the server

Before running the server, you will need to create a `.env` file in the root directory of the project. You can use the `.env-example` file as a template.

To run the server, run the following command:

```bash
python manage.py runserver
```

## Usage

### Djando Admin

The Django admin is available at `/admin/`. You can create a superuser by running the following command:

```bash
python manage.py createsuperuser
```

### Basic Authentication

Almost all of the endpoints require authentication. You can create a trainer by sending a `POST` request to the `api/trainers/signup` endpoint. The request body should contain the following fields:

```json
{
  "username": "username",
  "password": "password"
}
```

You can then use the username and password to authenticate your requests.

### Endpoints

#### Trainers

- `POST /api/trainers/signup/` - Create a trainer

- `GET /api/trainers/` - Get all trainers
- `GET /api/trainers/:uuid/` - Get a trainer by uuid
- `PUT /api/trainers/:uuid/` - Update a trainer by uuid
- `DELETE /api/trainers/:uuid/` - Delete a trainer by uuid

## Acknowledgments

- [PokeAPI](https://pokeapi.co/) - The Pokemon API used

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
