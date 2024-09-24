# mbox-to-csv-email-filter
Mbox Email Parser and Keyword Filter to CSV

You can use this script to extract email addresses from your Mbox based on the content of the emails. The script searches for emails containing specific keywords that you define.  

The keywords will need to be hardcoded in the script :  
`keywords = ["", "", ""] `

if 'keywords' is left blank, the script will just return all emails.  

Make sure you replace "YOUR NAME" with your actual name so it doesn't return your own emails too.  
`if sender_email not in unique_senders and sender_name != "YOUR NAME": `

The output is a csv file containing : name, email, subject.  
You can import the csv in a google sheet to have your data in a sheet format easily and start working with a list of contact that is relevant to you. 

