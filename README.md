# FastAPI Names API

This is a simple API built with FastAPI that allows you to manage a list of names. It supports basic operations like retrieving, adding, and deleting names.

## Features

- Retrieve a list of all names.
- Retrieve a specific name by its ID.
- Add a new name to the list.
- Delete a name by its ID.

## Endpoints

### Retrieve all names

- **Method:** `GET`
- **Endpoint:** `/nombres`
- **Description:** Retrieves the list of names.

### Retrieve a specific name

- **Method:** `GET`
- **Endpoint:** `/nombres/{nombre_id}`
- **Description:** Retrieves a specific name by ID.
- **Parameters:**
  - `nombre_id`: The ID of the name you want to retrieve.

### Add a new name

- **Method:** `POST`
- **Endpoint:** `/nombres`
- **Description:** Adds a new name.
- **Request Body:**
  - JSON object with the following fields:
    - `nombre`: The first name.
    - `apellido`: The last name.
    - `edad`: The age.

### Delete a name

- **Method:** `DELETE`
- **Endpoint:** `/nombres/{nombre_id}`
- **Description:** Deletes a specific name by ID.
- **Parameters:**
  - `nombre_id`: The ID of the name you want to delete.

## Example Usage

**To get all names, you can use the following command:**

```bash
curl -X GET "http://127.0.0.1:8000/nombres"
```

**To retrieve a specific name by ID, you can use the following command:**

```bash
curl -X GET "http://127.0.0.1:8000/nombres/1"
```

## Requirements

- Python 3.7 or higher
- FastAPI
- Uvicorn

## Installation

You can install the required packages using the following command:

```bash
pip install fastapi uvicorn
```

## Running the Application

To start the server, run:
uvicorn main:app --reload

Then, visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to access the interactive API documentation, where you can test the endpoints directly.

## License

This project is open-source and available under the [MIT License](LICENSE).
