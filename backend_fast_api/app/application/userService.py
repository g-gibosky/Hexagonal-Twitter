from ..domain.user import User
from ..infrastructure.userRepository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, user_data: dict) -> User:
        return self.user_repository.save(user_data)
    
    def update_user(self, user_data: dict, user_id:int) -> User:
        return self.user_repository.update(user_data, user_id)

    # Additional methods for user management
