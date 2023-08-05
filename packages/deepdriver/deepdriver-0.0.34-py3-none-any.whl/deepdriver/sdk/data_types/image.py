import hashlib
import json
import os
import random
import string
from typing import Union

import PIL
from assertpy import assert_that

from deepdriver import logger
from deepdriver.sdk.data_types.media import LOG_TYPE_IMAGE, Media
from deepdriver.sdk.data_types.run import Run
from deepdriver.sdk.interface import interface


class Image(Media):

    def __init__(self, data: Union[str, PIL.Image.Image]) -> None:
        super().__init__(log_type=LOG_TYPE_IMAGE)

        assert_that(data).is_not_none()
        if isinstance(data, str):
            # str인 경우 local_path로 지정하고 data 에는 해당 경로 파일을 로드한 PIL.Image 객체를 지정함
            self.local_path = data
            self.data = PIL.Image.open(self.local_path)
            self.height = self.data.size[1]
            self.width = self.data.size[0]
            self.format = self.data.format
        elif isinstance(data, PIL.Image.Image):
            self.data = data
            # data가 PIL.Image 객체인 경우 7자리의 random id값을 생성한후 {random_id}.{file_format}으로 저장
            random_id = "".join(random.choice(string.digits) for _ in range(7))
            self.local_path = f"{random_id}.{data.format}"
            logger.debug(f"PIL Image save to local:local_path:{self.local_path}")
            data.save(self.local_path)
            self.height = self.data.size[1]
            self.width = self.data.size[0]
            self.format = self.data.format
        else:
            raise Exception(f"unknown data type {type(data)}")

    def to_json(self, key_name: str) -> str:
        assert_that(key_name).is_not_none()
        with open(self.local_path, "rb") as f:
            digest = hashlib.md5(f.read()).hexdigest()

        value_type = __class__.__name__
        return json.dumps({
            "log_type": self.log_type,
            # "hash": digest,
            "size": os.stat(self.local_path).st_size,
            "path": self.get_path(key_name),
            "height": self.height,
            "width": self.width,
            "format": self.format,
        })

    # json으로 구성된 메타데이터 전송
    def upload_file(self, run: Run, key_name: str) -> None:
        value_type = __class__.__name__
        with open(self.local_path, "rb") as f:
            digest = hashlib.md5(f.read()).hexdigest()

        # 저장한 파일을 Interface.py의 upoad_file을 호출하여 전송
        value_type = __class__.__name__
        root_path = self.get_root_path(run.run_id)
        path = self.get_path(key_name)
        logger.debug(f"file upload[image] : local_path=[{self.local_path}], root_path=[{root_path}], path=[{path}]")
        interface.upload_file(upload_type="RUN", local_path=self.local_path, root_path=root_path, path=path,
                              run_id=run.run_id, artifact_id=0, last_file_yn="Y", teamName=run.team_name, expName=run.exp_name,
                              run_name=run.run_name,
                              artifact_name="", artifact_type="", artifact_digest="", entry_digest=digest,
                              entry_list=[], file_index=0)

    def get_path(self, key_name: str) -> str:
        # server 패스
        return f"{key_name}.{self.format}"


    def get_root_path(self, run_id: int) -> str:
        return os.path.join(str(run_id), "media")