# FASTAPI X REACT JS EXAMPLE PROJECT


![Continuous Integration and Delivery](https://github.com/megacoderkim/fastapireact/workflows/Continuous%20Integration%20and%20Delivery/badge.svg?branch=master)

## About

A simple fast api api backend with a react frontend.

## Running the project

The project uses docker with docker-compose

Run `docker-compose up --build`

The frontend app should be available at http://localhost:3000
The backend api should be available at  http://localhost:8004

## Testing

### Backend API
Run `docker-compose exec web python -m pytest`