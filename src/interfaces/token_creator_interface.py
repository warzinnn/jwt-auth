from abc import ABC, abstractmethod


class TokenCreatorInterface(ABC):
    @abstractmethod
    def get_token(self, username, role):
        raise NotImplementedError

    @abstractmethod
    def _get_private_key(self):
        raise NotImplementedError

    @abstractmethod
    def _encode_token(self, username, role):
        raise NotImplementedError
