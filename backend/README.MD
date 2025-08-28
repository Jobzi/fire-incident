## Backend

The backend is built with Python and FastAPI. It handles all the business logic and data storage for the fire incident reporting system.

### Directory Structure

```
backend/
├── src/
│   ├── implementations/
│   │   └── json_service.py
│   ├── domain/
│   │   ├── incident.py
│   │   └── incident_enum.py
│   ├── cases/
│   │   ├── create_incident_use_case.py
│   │   └── get_incident_use_case.py
│   ├── main.py
│   └── storage/
│       └── incident.json
└── tests/
    ├── conftest.py
    └── test_create_incident.py
```

## HOW TO RUN

Create a venv with makefile commands:

```bash
make venv
```

Activate the venv:

```bash
source venv/bin/activate
```

Install the dependencies:

```bash
make install
```

Run the application:

```bash
make run
```

## Stack

- Python
- FastAPI
- Pydantic
- Uvicorn

## TO DO

- [ ] implement pagination for incident list
- [ ] add user authentication and authorization
- [ ] create a frontend for the incident reporting system

## IA

- [x] Storage and serve images
- [x] Config Vite Proxy server
