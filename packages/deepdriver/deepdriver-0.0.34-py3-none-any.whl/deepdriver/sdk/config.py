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

    def get(self, *args):
        pass

    def Items(self):
        pass

    def keys(self):
        pass

    def __getattr__(self, name):
        value = "Value for %s" % name
        setattr(self, name, value)
        return value
