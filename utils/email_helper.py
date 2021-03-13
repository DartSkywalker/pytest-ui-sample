import base64
import imaplib
import re
import time

from utils.constants import EMAIL_USER, EMAIL_PASS, EMAIL_IMAP, EMAIL_RELOAD_WAIT, SUPPORT_EMAIL, REG_CODE_REGEX


class EmailHelper:
    """
    Utils class to handle gathering confirmation codes from Gmail box
    """

    def __init__(self):
        self.user = EMAIL_USER
        self.password = EMAIL_PASS
        self.imap_url = EMAIL_IMAP
        self.waiting_time = EMAIL_RELOAD_WAIT

    def __search(self, key, value, con):
        result, data = con.search(None, key, '"{}"'.format(value))
        return data

    def __get_body(self, msg):
        if msg.is_multipart():
            return self.__get_body(msg.get_payload(0))
        else:
            return msg.get_payload(None, True)

    def __get_emails(self, result_bytes):
        msgs = []
        for num in result_bytes[0].split():
            typ, data = self.con.fetch(num, '(RFC822)')
            msgs.append(data)
        return msgs

    def get_registration_code(self):
        registration_codes = []
        attempts = 0
        while attempts < 7:
            # Connection created outside of __init__ because of needing to reload mailbox data after each attempt
            self.con = imaplib.IMAP4_SSL(self.imap_url)
            self.con.login(self.user, self.password)
            self.con.select('Inbox')
            msgs = self.__get_emails(self.__search('FROM', SUPPORT_EMAIL, self.con))
            try:
                for msg in msgs[::-1]:
                    for sent in msg:
                        if type(sent) is tuple:
                            content = str(sent[1], 'utf-8').split('Content-Transfer-Encoding: base64')
                            decoded = base64.urlsafe_b64decode(content[-1]).decode('UTF-8')
                            code = re.search(REG_CODE_REGEX, decoded).group(1)
                            registration_codes.append(code)
                            email_id = str(sent[0], 'utf-8').split(' ')[0]
                            self.con.store(email_id, "+FLAGS", "\\Deleted")
                if len(registration_codes) == 0:
                    self.con.logout()
                    attempts += 1
                    print(f'Email is not found...waiting {self.waiting_time} seconds')
                    raise IndexError
                else:
                    return registration_codes[0]
            except IndexError:
                time.sleep(self.waiting_time)
