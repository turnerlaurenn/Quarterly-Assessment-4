# Quarterly-Assessment-4
## AI-Powered News Newsletter Generator

This project automates the process of fetching the latest news articles, summarizing them, and sending them as a daily email.

It utilizes the following tools:

* **Python 3.x:** For scripting.
* **News API (or custom API like BBC, Reuters, etc.):** For fetching news.
* **OpenAI API:** For summarizing articles.
* **SMTP (Outlook, Gmail, etc.):** To send emails.
* **Cron job (macOS):** To schedule the task to run daily.

## Features

* Fetches the latest news based on pre-defined topics of interest.
* Summarizes the articles using OpenAI's GPT model.
* Sends a daily email with the latest news and summaries at 8 AM every day.
* Automatically wakes up the MacBook to run the script even when it's asleep (with the help of `pmset`).

## Setup

### 1. Prerequisites

Ensure you have the following installed:

* **Python 3.x:** Download it from [python.org](https://www.python.org/downloads/).
* **News API key:** Obtain an API key from [NewsAPI](https://newsapi.org/).
* **OpenAI API key:** Sign up at [OpenAI](https://beta.openai.com/signup/) to get the API key.

### 2. Install Dependencies

Clone the repository and install the required Python libraries:

\`\`\`bash
git clone <repo-url>
cd <project-directory>
pip install -r requirements.txt
\`\`\`

Here are the dependencies listed in `requirements.txt`:

\`\`\`
requests
openai
smtplib
python-dotenv
schedule
\`\`\`

### 3. Setup Environment Variables

Create a `.env` file in the root directory and add the following keys:

\`\`\`ini
NEWS_API_KEY=your_news_api_key
OPENAI_API_KEY=your_openai_api_key
EMAIL_ADDRESS=your_email@example.com
EMAIL_PASSWORD=your_email_password
SMTP_SERVER=smtp.example.com
SMTP_PORT=587
RECIPIENT_EMAIL=recipient@example.com
\`\`\`

### 4. Configure Mac for Scheduling

To ensure the script runs at 8 AM every day:

Open Terminal and run the following command to set your Mac to wake up at a specific time:

\`\`\`bash
sudo pmset repeat wakeorpoweron MTWRFSU 08:00:00
\`\`\`

Set up a cron job to run the script at 8 AM every day:

\`\`\`bash
crontab -e
\`\`\`

Then, add the following line to schedule the script to run:

\`\`\`bash
0 8 * * * /usr/bin/python3 /path/to/your/script/main.py
\`\`\`

Ensure `/path/to/your/script/main.py` points to the actual location of your `main.py` file.

### 5. Run the Project

Once everything is set up:

The script will automatically fetch news articles, summarize them, and send the email at 8 AM every day.

To manually run the script, simply execute:

\`\`\`bash
python3 main.py
\`\`\`

### 6. Troubleshooting

If your Mac does not stay awake for the scheduled task, ensure it's connected to power and the lid is open or using clamshell mode with an external display/keyboard.

Check the `pmset` status by running the command:

\`\`\`bash
pmset -g sched
\`\`\`

This will show if the wake-up schedule is set correctly.

## Project Structure

\`\`\`bash
├── fetchnews.py     # Contains the logic for fetching news articles
├── summarize.py     # Contains the logic for summarizing the articles
├── sendemail.py     # Contains the logic for sending emails with the summaries
├── config.py        # Manages environment variables and settings
├── .env             # Environment variables (don't forget to add this to .gitignore)
├── requirements.txt # List of Python dependencies
├── main.py          # Main script to fetch, summarize, and send email
└── README.md        # Project documentation
\`\`\`

## License

This project is licensed under the MIT License - see the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.
"""
