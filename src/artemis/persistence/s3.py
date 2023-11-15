import os
import boto3
from botocore.exceptions import ClientError

from artemis.persistence.base import BasePersistence

S3_BUCKET = os.getenv('S3_BUCKET')


class S3Persistence(BasePersistence):

    def __init__(self, s3_client=None):
        self.s3_client = s3_client or boto3.client(
            's3',
            aws_access_key_id=os.environ.get('AWS_ACCESS_KEY'),
            aws_secret_access_key=os.environ.get('AWS_ACCESS_SECRET'),
            region_name='us-east-1'
            )

    def write_binary(self, path, value):
        try:
            result = self.s3_client.put_object(
                Bucket=S3_BUCKET,
                Key=path,
                Body=value,
            )
            return True
        except ClientError:
            return False

    def read_binary(self, path):
        try:
            result = self.s3_client.get_object(
                Bucket=S3_BUCKET,
                Key=path
            )
            return result.get('Body').read()
        except ClientError:
            return None

    def get_exists_status(self, path):
        response = self.s3_client.list_objects_v2(Bucket=S3_BUCKET, Prefix=path)
        for obj in response.get('Contents', []):
            if obj.get('Key') == path:
                return True
        return False

    def get_presigned_url(self, path):
        try:
            return self.s3_client.generate_presigned_url(
                ClientMethod='get_object',
                Params={
                    'Bucket': S3_BUCKET,
                    'Key': path
                },
                ExpiresIn=3600
            )
        except ClientError:
            return None
