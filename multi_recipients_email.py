import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, recipients, subject, message_body):
    # Server setting
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Email headers
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ", ".join(recipients)  # Join all recipients with commas
    msg['Subject'] = subject

    # Attach message to the email
    msg.attach(MIMEText(message_body, 'plain'))

    try:
        # start the connection
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure connection with TLS

        # Log in to email account
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, recipients, msg.as_string())

        # Close the server connection
        server.quit()

        print(f"Email sent successfully to {', '.join(recipients)}")

    except Exception as e:
        print(f"Failed to send email. Error: {e}")

# Usage
if __name__ == "__main__":
    sender_email = "user.account@gmail.com"  # email
    sender_password = "userpassword"      # password
    
    # List of recipients
    recipients = ["recipient1@outlook.com", "recipient2@yahoo.com", "recipient3@icloud.com"]
    
    # Email subject and message
    subject = "Test Email"
    message_body = "This is a test email sent from Python."

    # Send the email
    send_email(sender_email, sender_password, recipients, subject, message_body)