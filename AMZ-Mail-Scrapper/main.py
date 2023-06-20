import os
import imaplib
import email
import csv

# Email account settings
IMAP_SERVER = 'imap.example.com'
IMAP_PORT = 993
USERNAME = 'your-email@example.com'
PASSWORD = 'your-password'

# Sender email address to filter
SENDER_EMAIL = 'sender@example.com'

# Directory to save downloaded attachments
SAVE_DIRECTORY = 'attachments'

# Function to connect to the email account
def connect_to_email():
    mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
    mail.login(USERNAME, PASSWORD)
    mail.select('inbox')
    return mail

# Function to fetch email attachments
def fetch_attachments(mail):
    _, data = mail.search(None, 'FROM', f'"{SENDER_EMAIL}"')
    email_ids = data[0].split()
    attachments = []

    for email_id in email_ids:
        _, response = mail.fetch(email_id, '(RFC822)')
        raw_email = response[0][1]
        msg = email.message_from_bytes(raw_email)

        for part in msg.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue

            filename = part.get_filename()
            if filename:
                attachments.append((email_id.decode(), filename, part.get_payload(decode=True)))

    return attachments

# Function to convert attachment data to CSV
def convert_to_csv(attachment_data):
    csv_data = []

    for email_id, filename, data in attachment_data:
        csv_data.append([email_id, filename, data])

    return csv_data

# Function to save attachment data as CSV
def save_as_csv(csv_data):
    if not os.path.exists(SAVE_DIRECTORY):
        os.makedirs(SAVE_DIRECTORY)

    csv_path = os.path.join(SAVE_DIRECTORY, 'attachments.csv')
    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Email ID', 'Filename', 'Attachment Data'])
        writer.writerows(csv_data)

    print(f'Attachments saved as CSV: {csv_path}')

# Main function
def main():
    # Connect to the email account
    mail = connect_to_email()

    # Fetch attachments from the specified sender
    attachments = fetch_attachments(mail)

    if attachments:
        # Convert attachment data to CSV
        csv_data = convert_to_csv(attachments)

        # Save attachment data as CSV
        save_as_csv(csv_data)
    else:
        print('No attachments found from the specified sender.')

if __name__ == '__main__':
    main()
