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

#### Running the tests

To run the tests, run the following command:

```bash
python manage.py test
```

## Usage

### Djando Admin

The Django admin is available at `/admin/`. You can create a superuser by running the following command:

```bash
python manage.py createsuperuser
```

### Basic Authentication

Almost all of the endpoints require authentication. You can create a trainer by sending a `POST` request to the `api/trainers/signup` endpoint.

You can then use the username and password to authenticate your requests.

### Endpoints

#### Trainers

- `POST /api/trainers/signup` - Create a trainer

To create a trainer, send a `POST` request to the `api/trainers/signup` endpoint. The request body should contain the following fields:

```json
{
  "username": "username",
  "password": "password"
}
```

Only admins can edit or delete trainers.

- `GET /api/trainers/` - Get all trainers
- `GET /api/trainers/:uuid/` - Get a trainer by uuid
- `PUT /api/trainers/:uuid/` - Update a trainer by uuid
- `DELETE /api/trainers/:uuid/` - Delete a trainer by uuid

#### Teams

Trainers can create, edit, and delete their own teams.

- `GET /api/teams/` - Get all teams
- `GET /api/teams/:uuid/` - Get a team by uuid
- `POST /api/teams/` - Create a team

```json
{
  "name": "team_name"
}
```

- `PUT /api/teams/:uuid/` - Update a team by uuid
- `DELETE /api/teams/:uuid/` - Delete a team by uuid

Actions can be performed on a team's pokemon with the following endpoints:

- `POST /api/teams/:uuid/pokemon/` - Add a pokemon to a team

```json
{
  "name": "pokemon_name"
}
```

- `DELETE /api/teams/:uuid/pokemon/:pk/` - Remove a pokemon from a team
- `PUT /api/teams/:uuid/pokemon/:pk/` - Update a pokemon on a team
- `GET /api/teams/:uuid/pokemon/` - Get all pokemon on a team
- `GET /api/teams/:uuid/pokemon/:pk/` - Get a pokemon detail on a team

#### Docs

The API docs (swagger) are available at `/api/docs/`.

- `GET /api/docs/swagger` - Get the swagger UI
- `GET /api/docs/swagger.<ext>` - Get the swagger schema in the specified format (json, yaml)
- `GET /api/docs/redoc` - Get the redoc UI

## Acknowledgments

- [PokeAPI](https://pokeapi.co/) - The Pokemon API used

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
