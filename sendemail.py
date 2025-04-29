import sys
sys.dont_write_bytecode = True

import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import EMAIL_ADDRESS, EMAIL_PASSWORD, SMTP_SERVER, SMTP_PORT, RECIPIENT_EMAIL

def format_email_body(summaries):
    today = datetime.now().strftime("%A, %B %d, %Y")
    
    body = f"<h2>Hey Lauren! 👋</h2>"
    body += f"<p>Here's your news for {today}:</p>"
    
    for idx, (title, summary, url) in enumerate(summaries, 1):
        body += f"<p><b>{idx}. {title}</b><br>{summary}<br>"
        body += f"<a href='{url}'>Read full article here</a></p>"
    
    body += "<p>Have an amazing day! 🌟</p>"
    return body

def send_newsletter(summaries):
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = "🗞️ Your Daily News Newsletter"

    # Format the body using HTML
    body = format_email_body(summaries)
    msg.attach(MIMEText(body, 'html'))  # <<< Note: now sending as 'html' instead of 'plain'

    # Send the email
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Error sending email: {e}")
