"""
simplest possible abstraction around object storage
"""

from sys import prefix
from typing import List
import boto3


class ObjectStorage:
    def __init__(self, key_prefix: str) -> None:
        ssm_client = boto3.client('ssm')
        param = ssm_client.get_parameter(Name='/wdig/dev/databucket/name')
        self.data_bucket_name = param['Parameter']['Value']
        self.s3_client = boto3.client('s3')
        self.key_prefix = key_prefix

    def health_check(self):
        self.s3_client.list_objects_v2(Bucket=self.data_bucket_name)

    def test_access(self):
        self.s3_client.put_object(Bucket=self.data_bucket_name, Key=f'test-access.txt', Body=b'hello - this file is for testing access to S3')
        self.s3_client.get_object(Bucket=self.data_bucket_name, Key=f'test-access.txt')

    def save_file(self, key: str, path_to_file: str) -> None:
        self.s3_client.upload_file(path_to_file, self.data_bucket_name, f'{self.key_prefix}/{key}')

    def list_files(self) -> List[str]:
        response = self.s3_client.list_objects_v2(Bucket=self.data_bucket_name, Prefix=f'{self.key_prefix}/')
        return list(map(lambda obj: obj['Key'], response['Contents']))


class BankFileObjectStorage(ObjectStorage):
    def __init__(self) -> None:
        super().__init__('wdig-bank-files')


if __name__ == "__main__":
    os = BankFileObjectStorage()
    os.health_check()
    os.test_access()
    os.list_files()
    pass
