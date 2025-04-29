import sys
sys.dont_write_bytecode = True

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import EMAIL_ADDRESS, EMAIL_PASSWORD, SMTP_SERVER, SMTP_PORT, RECIPIENT_EMAIL

def send_newsletter(summaries):
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = "📰 Your Daily News Newsletter"

    # Format the email body
    body = "Here are today's top news summaries:\n\n"
    for idx, (title, summary) in enumerate(summaries, 1):
        body += f"{idx}. {title}\n{summary}\n\n"

    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Error sending email: {e}")
