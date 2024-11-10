# Brazilian National Football Competition Scraper & Email Service

This project provides a scraper for fetching match data from Brazilian national football competitions (Série A) and sends the data in an Excel format via email. It is built using **FastAPI** for the backend and uses **scraping** techniques to collect competition data from a website. 

This project was developed as part of the evaluation requirement for the **"Project and System Analysis"** course.

## Project files structure

```
|___ notebooks # show the logic behind the project in a more linear form
|___ src
      |__ scrap # contains the entire logic of the project
```

## Features

- **Scraping match data**: The scraper fetches match details like date, time, teams (host and visitor), score, round, competition name, and season.
- **Excel export**: The collected data is saved as an Excel file (.xlsx) for easy use and distribution.
- **Email service**: The project includes an email service that sends the Excel file as an attachment to a specified email address.
- **Asynchronous architecture**: The project uses FastAPI's async features for non-blocking, high-performance scraping and email sending.

## Main Libraries

- **FastAPI**: The backend framework used to build the API. It is asynchronous and fast, allowing for scalable performance.
- **BeautifulSoup**: A Python library used for parsing HTML and extracting data from web pages.
- **Requests**: A simple HTTP library used for making requests to the scraping targets.
- **Pandas**: Used to structure and manipulate the scraped data before exporting it as an Excel file.
- **OpenPyXL**: Required for exporting data to Excel format.
- **aiosmtplib**: An asynchronous SMTP client for sending emails without blocking the event loop.
- **Regex (re)**: Used for extracting dates, times, and other relevant data from the HTML content.

## Installation

To set up the project, follow these steps:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/football-scraper.git
    cd football-scraper
    ```

2. **Create and activate a virtual environment**:

    For Linux/macOS:
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```

    For Windows:
    ```
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Install the dependencies**:

    Open up the project virtual project environment as show above and then execute the follow command:

    ```
    pip install -r requirements.txt
    ```

4. **Configure your environment**:
    First of all, create a `app password` at your gmail account, [click here](https://knowledge.workspace.google.com/kb/how-to-create-app-passwords-000009237?hl=pt-br) to find how.

    Add your email credentials to the `.env`

    ```python
    FROM_EMAIL_ADDRESS = 'your-email@gmail.com'
    FROM_EMAIL_PASSWORD = 'your-email-password'
    ```

## Running the Project

To run the FastAPI app, use the following command:

1. Open up a terminal at the root project and execute the follow command `fastapi dev src/main.py`

## API Endpoints

### POST /send_email
Send an email with the scraped competition data as an Excel file.

#### Request Body
```
{
  "email": "recipient-email@example.com",
  "seasons": [2023, 2024]
}
```

- **email**: The email address to send the Excel file to.
- **seasons**: The seasons you want to scrape data for (e.g., 2023, 2024).

#### Response

```
{
  "message": "Excel file was successfully sent!"
}
```

##### Example
Use curl or any HTTP client (e.g., Postman) to send the request:

```
curl -X 'POST' \
  'http://localhost:8000/send_email' \
  -H 'Content-Type: application/json' \
  -d '{
  "email": "recipient@example.com",
  "seasons": [2023, 2024]
}'
```
The system will scrape the match data, create an Excel file, and send it to the specified email address.

## Contributing
If you want to contribute to this project, please fork the repository and submit a pull request. Feel free to open an issue if you encounter any problems or have suggestions for improvements.