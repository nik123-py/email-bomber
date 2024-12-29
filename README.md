# Email Bomber Script

This script allows users to send multiple emails to a recipient in an automated manner using Gmail's SMTP server. It is designed for educational purposes only and should not be used for malicious activities. Misuse of this script may violate laws and terms of service.

## Features

- **SMTP Server Connection**: Establishes a secure connection to Gmail's SMTP server.
- **User Authentication**: Prompts users for their email and password to log in.
- **Customizable Message**: Users can input a message and specify the number of times it should be sent.
- **Error Handling**: Gracefully handles authentication errors and other exceptions during the email-sending process.
- **Secure Password Input**: Uses `getpass` to hide the password during input.

## Requirements

- Python 3.x
- An active Gmail account
- Internet connection

## Installation

1. Clone or download this repository.
2. Ensure you have Python 3 installed on your system.
3. Install any required modules (if not pre-installed):
   ```bash
   pip install smtplib
   ```

## Usage

1. Run the script:
   ```bash
   python email_bomber.py
   ```
2. Follow the on-screen prompts:
   - Enter your Gmail address and password.
   - Provide the recipient's email address.
   - Specify the number of emails to send.
   - Type the message you want to send.
3. The script will begin sending emails and display the status of each attempt.

## Notes

- **Google Account Security**: If you encounter authentication issues, you may need to enable "Allow less secure apps" in your Google account settings or create an app-specific password if you have 2-factor authentication enabled.
- **Ethical Use**: Use this script responsibly and only for authorized purposes. Unauthorized email spamming is illegal and unethical.

## Example Output

```
Enter Your Email: example@gmail.com
Enter Your Password: 
Successfully signed in.
Enter Recipient's Email: victim@example.com
Enter the number of messages to send: 5
Enter your message: 
Hello, this is a test message.
Starting to send emails...
[1] Email sent successfully.
[2] Email sent successfully.
[3] Email sent successfully.
[4] Email sent successfully.
[5] Email sent successfully.
All emails sent.
SMTP server connection closed.
```

## Disclaimer

This script is intended for educational purposes only. The developers are not responsible for any misuse of this script. Ensure compliance with applicable laws and service terms when using it.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
