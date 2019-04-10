/*provider "aws" {
  access_key = "AKIAJ34BCF73VWY57ZDQ"
  secret_key = "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"
  region     = "us-east-1"
}

resource "aws_s3_bucket" "first_bucket" {
  bucket = "first-vt-bucket-1510"
  acl = "private"

  versioning {
    enabled = "true"
  }
}

resource "aws_s3_bucket_object" "object" {
  bucket = "first-vt-bucket-1510"
  key = "first_object"
  source = "./assert.py"
  etag = "${filemd5("./assert.py")}"

  depends_on = ["aws_s3_bucket.first_bucket"]
}*/
