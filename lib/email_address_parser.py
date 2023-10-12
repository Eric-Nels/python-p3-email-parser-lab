import re

class EmailAddressParser:
    def __init__(self, email_address):
        self.email_address = email_address

    def parse(self):

        email_list = re.split(r'[,\s]+', self.email_address)

        pattern = r'([A-z]+)(\.\w+)?@(\w+)\.com'

        email_regex = re.compile(pattern)

        final_list = [email for email in email_list if email_regex.match(email)]

        return sorted(final_list)

    