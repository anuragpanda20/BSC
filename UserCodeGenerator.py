import random
import string

class UserCodeGenerator:
    def generate_code(self):
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        return code