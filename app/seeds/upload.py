from werkzeug.utils import secure_filename
import boto3
import os
import requests
import uuid
from dotenv import load_dotenv
load_dotenv()


def allowed_file(filename): return '.' in filename and filename.rsplit(
    '.', 1)[1].lower() in set(['png', 'jpg', 'jpeg'])


BUCKET_NAME = os.environ.get("S3_BUCKET")
S3_LOCATION = f"https://{BUCKET_NAME}.s3.amazonaws.com/"
CLOUDFRONT_LOCATION = "https://d1irxr40exwge2.cloudfront.net/"

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.environ.get("S3_KEY"),
    aws_secret_access_key=os.environ.get("S3_SECRET")
)


def upload_image_to_bucket(image, image_name, acl="public-read"):
    print(f"upload_image_to_bucket: Uploading {image_name}", "-"*50)
    image_name = str(uuid.uuid1()) + "-" + image_name
    bucket_url = f"{CLOUDFRONT_LOCATION}{image_name}"
    try:
        s3.upload_fileobj(
            image,
            BUCKET_NAME,
            image_name,
            ExtraArgs={
                "ACL": acl,
            }
        )
    except Exception as e:
        # in case the our s3 upload fails
        return {"errors": str(e)}
    print(bucket_url, "-"*50)
    return bucket_url


def upload_image_to_bucket_from_url(url, acl="public-read"):
    image_name = secure_filename(os.path.basename(url))
    bucket_url = f"{CLOUDFRONT_LOCATION}{image_name}"

    # Don't bother the third party if we already have the image
    try:
        s3.head_object(Bucket=BUCKET_NAME, Key=image_name)
    except Exception:
        print("Downloading", url)
        response = requests.get(url, stream=True)
        try:
            s3.upload_fileobj(
                response.raw,
                BUCKET_NAME,
                image_name,
                ExtraArgs={
                    "ACL": acl,
                }
            )
        except Exception as e:
            # in case the our s3 upload fails
            return {"errors": str(e)}

    return bucket_url
