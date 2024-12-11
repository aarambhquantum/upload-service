import aioboto3
from src.configs.env import get_settings
import logging
from src.configs.error_constants import ErrorMessages
from src.exceptions.errors.generic import FileUploadException

config = get_settings()
logger = logging.getLogger()


class AWS_S3:
    def __init__(self):
        self.session = aioboto3.Session(
            region_name=config.aws_region_name,
            aws_access_key_id=config.aws_access_key_id,
            aws_secret_access_key=config.aws_secret_access_key,
        )

    async def upload_to_s3(self, file, path: str, content_type: str = "video/mp4"):
        try:
            async with self.session.client("s3") as s3:
                await s3.upload_fileobj(
                    file,
                    config.aws_bucket_name,
                    path,
                    ExtraArgs={"ContentType": content_type},
                )
                return f"https://{config.aws_bucket_name}.s3.{config.aws_region_name}.amazonaws.com/{path}"
        except Exception as e:
            logger.exception(ErrorMessages.FILE_UPLOAD_ERROR)
            raise FileUploadException(ErrorMessages.FILE_UPLOAD_ERROR)

    async def initiate_multipart_upload(self, filename: str):
        try:
            async with self.session.client("s3") as s3:
                response = await s3.create_multipart_upload(
                    Bucket=config.aws_bucket_name, Key=filename
                )
                upload_id = response.get("UploadId")
                return upload_id
        except Exception as e:
            logger.exception(
                f"{ErrorMessages.FILE_MULTIPART_UPLOAD_ERROR} for {filename}: {str(e)}"
            )
            raise FileUploadException(ErrorMessages.FILE_MULTIPART_UPLOAD_ERROR)

    async def generate_presigned_part_url(
        self,
        filename: str,
        upload_id: str,
        part_number: int,
        expiration: int = 60 * 60 * 24,
    ):
        """
        expiration: in seconds.
        """
        try:
            async with self.session.client("s3") as s3:
                presigned_url = await s3.generate_presigned_url(
                    "upload_part",
                    Params={
                        "Bucket": config.aws_bucket_name,
                        "Key": filename,
                        "UploadId": upload_id,
                        "PartNumber": part_number,
                    },
                    ExpiresIn=expiration,
                )
                return presigned_url
        except Exception as e:
            logger.exception(
                f"{ErrorMessages.PRESIGNED_URL_GENERATION_FAILED} for part {part_number} of {filename}: {str(e)}"
            )
            raise FileUploadException(ErrorMessages.PRESIGNED_URL_GENERATION_FAILED)

    async def generate_presigned_url(
        self,
        filename: str,
        expiration: int = 60 * 60 * 24,  # Default expiration time is 24 hours
    ):
        """
        Generate a presigned URL for uploading a file to S3.

        :param filename: The S3 object key for the file.
        :param expiration: The expiration time in seconds.
        :return: The presigned URL for uploading the file.
        """
        try:
            async with self.session.client("s3") as s3:
                # Generate presigned URL for PUT request to upload the file
                presigned_url = await s3.generate_presigned_url(
                    "put_object",
                    Params={
                        "Bucket": config.aws_bucket_name,
                        "Key": filename,
                    },
                    ExpiresIn=expiration,
                )
                return presigned_url
        except Exception as e:
            logger.exception(
                f"{ErrorMessages.PRESIGNED_URL_GENERATION_FAILED} for {filename}: {str(e)}"
            )
            raise FileUploadException(ErrorMessages.PRESIGNED_URL_GENERATION_FAILED)

    async def complete_multipart_upload(
        self, filename: str, upload_id: str, parts: list
    ):
        """
        Completes a multipart upload by assembling previously uploaded parts.

        :param filename: The key (filename) in the S3 bucket.
        :param upload_id: The upload ID of the multipart upload.
        :param parts: List of dictionaries containing ETag and PartNumber.
        :return: Response from S3 on successful completion.
        """
        try:
            async with self.session.client("s3") as s3:
                response = await s3.complete_multipart_upload(
                    Bucket=config.aws_bucket_name,
                    Key=filename,
                    UploadId=upload_id,
                    MultipartUpload={
                        "Parts": sorted(
                            [part.dict() for part in parts],
                            key=lambda x: x["PartNumber"],
                        )
                    },
                )
                return response
        except Exception as e:
            logger.exception(
                f"{ErrorMessages.ERROR_WHILE_COMPLETING_FILE_UPLOAD} for {filename}: {str(e)} {parts}"
            )
            raise FileUploadException(ErrorMessages.ERROR_WHILE_COMPLETING_FILE_UPLOAD)
