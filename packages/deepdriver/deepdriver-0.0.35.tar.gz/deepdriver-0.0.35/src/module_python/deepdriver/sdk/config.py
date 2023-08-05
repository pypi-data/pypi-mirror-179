from typing import Dict


class Config:

    def __init__(self, init_dict: Dict = None) -> None:
        pass

    # 하이퍼 파리미터와 같은 config 값 update
    def update(self) -> None:
        # 서버로 config() 전송
        pass

    def __setitem__(self):
        pass

    def __getitem__(self):
        pass

    def __contains__(self):
        pass

    def get(self, key: str):
        return self.__dict__[key]

    def Items(self):
        return list(self.__dict__.items())

    def keys(self) -> list:
        return list(self.__dict__.keys())

    def values(self) -> list:
        return list(self.__dict__.values())
