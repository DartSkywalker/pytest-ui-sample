class DataGenerator:
    """
    Workaround on managing test data
    (would be better to keep it in DB or delete user if tests were passed)
    """

    def __init__(self, email):
        self.email = email

    @staticmethod
    def __get_email_id():
        with open('./utils/email_ids.dat', 'r') as f:
            first_id = str(f.readline()).replace('\n', '')
            content = f.readlines()
        with open('./utils/email_ids.dat', 'w') as f:
            f.writelines(content)
        return first_id

    def get_login_data(self):
        email_id = self.__get_email_id()
        return f"{self.email.split('@')[0]}+{email_id}@{self.email.split('@')[1]}"

