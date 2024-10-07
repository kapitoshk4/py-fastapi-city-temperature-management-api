# City Temperature Management API

This FastAPI application manages city data and corresponding temperature data. It consists of two main components: a CRUD API for managing city data and an API that fetches and stores current temperature data for all cities in the database.

## Getting Started
### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/kapitoshk4/py-fastapi-city-temperature-management-api.git
   cd fastapi-city-temperature-management-api
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   alembic upgrade head
    ```
2. Go to [weather api](https://www.weatherapi.com/) and get api key
3. Copy .env.sample -> .env and populate with all required data
4. Run the development server:
    ```
    uvicorn main:app --reload --log-level debug
    ```

## Features

### Part 1: City CRUD API
- Create, Read and Delete city data.
- Each city has the following attributes:
  - **id**: Unique identifier for the city.
  - **name**: Name of the city.
  - **additional_info**: Additional information about the city.

### Part 2: Temperature API
- Fetch and store current temperature data for all cities.
- Each temperature record has the following attributes:
  - **id**: Unique identifier for the temperature record.
  - **city_id**: Reference to the city.
  - **date_time**: Date and time when the temperature was recorded.
  - **temperature**: Recorded temperature.

## API Endpoints

### City Endpoints
- `POST /cities`: Create a new city.
- `GET /cities`: Retrieve a list of all cities.
- `GET /cities/{city_id}`: Retrieve details of a specific city.
- `DELETE /cities/{city_id}`: Delete a specific city.

### Temperature Endpoints
- `POST /temperatures/update`: Fetch and store current temperature data for all cities.
- `GET /temperatures`: Retrieve a list of all temperature records.
- `GET /temperatures/?city_id={city_id}`: Retrieve temperature records for a specific city.
