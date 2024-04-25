import csv
import mailbox
from email.parser import BytesParser
from email import policy
from email.utils import parseaddr

# Path to your mbox file
mbox_file_path = "/PATH/TO/Mboxtakeout.mbox"

# Keywords to search for in the emails, need to be hardcoded in this case
keywords = ["", "", ""] 

# Output CSV file path
csv_file_path = "/PATH/TO/outputfile.csv"

# Set to keep track of unique senders
unique_senders = set()

# Open the mbox file for reading
mbox = mailbox.mbox(mbox_file_path)

# Open the CSV file for writing
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header row
    csv_writer.writerow(["Name", "Email", "Subject"])

    # Iterate through each message in the mbox file
    for message in mbox:
        # Parse the email message using BytesParser
        msg = BytesParser(policy=policy.default).parsebytes(message.as_bytes())

        # Extract sender's name and email address
        sender = msg['From']
        sender_name, sender_email = parseaddr(sender)

        # Check if sender is not a repeat and not yourself
        if sender_email not in unique_senders and sender_name != "YOUR NAME":
            unique_senders.add(sender_email)

            # Initialize the body variable
            body = ""

            # Iterate through the parts of the message
            for part in msg.walk():
                # Check if the part is plain text
                if part.get_content_type() == 'text/plain':
                    # Add the plain text content to the body variable
                    body += part.get_payload()

            # Check if any of the keywords are found in the message content
            found_keywords = [keyword for keyword in keywords if keyword.lower() in body.lower()]

            # If any keywords are found, write the Name, Email, and Subject fields to the CSV file
            if found_keywords:
                # Write Name, Email, and Subject fields to CSV file
                csv_writer.writerow([sender_name, sender_email, msg['Subject']])

# Close the mbox file
mbox.close()
