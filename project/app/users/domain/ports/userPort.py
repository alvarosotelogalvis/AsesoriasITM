class UserPort:

    def get_user_by_username(self, username: str):
        raise NotImplementedError
    
    def create_user(self, **kwargs):
        raise NotImplementedError
    
    def delete_user(self, professor_id: str):
        raise NotImplementedError
