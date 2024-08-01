# TikTok Video Downloader

This project is a web application that allows users to download videos from TikTok. The application is built using Flask and can be run either directly or using Docker.

## Demo

Check out the live demo of the application [here](https://koalka.toadres.pl/).


## Features

- Download TikTok videos by providing a URL.
- Responsive design using Bootstrap.
- Dockerized for easy deployment.

## Requirements

- Python 3.9+
- Flask
- yt-dlp
- Gunicorn

## Installation



### Running Locally

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/simple_tiktok_downloader.git
    cd simple_tiktok_downloader
    ```

2. **Create a virtual environment:**

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Run the application:**

    ```sh
    flask run
    ```

    The application will be available at `http://127.0.0.1:5000`.

### Running with Docker

1. **Build the Docker image:**

    ```sh
    docker build -t simple_tiktok_downloader .
    ```

2. **Run the Docker containers using `docker-compose`:**

    ```sh
    docker-compose up -d
    ```

    The application will be available at `http://localhost:80`.

## Configuration

The application uses the following configuration files:

- `docker-compose.yml`: Defines the services and their configurations.
- `Dockerfile`: Defines the Docker image for the application.
- `nginx.conf`: Configuration for the Nginx server.

In the `templates/index.html` file, you can optionally translate the names to English.

In the `nginx.conf` file, change the domain name to your own domain.

## Project Structure
- `app.py`: Main application file.
- `docker-compose.yml`: Docker Compose configuration.
- `Dockerfile`: Docker image configuration.
- `nginx.conf`: Nginx configuration.
- `requirements.txt`: Python dependencies.
- `templates/index.html`: HTML template for the web application.

## License

This project is licensed under the MIT License