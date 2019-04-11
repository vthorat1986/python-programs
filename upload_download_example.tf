resource "aws_s3_bucket" "first_bucket" {
  bucket = "first-vt-bucket-1511"
  acl = "private"

  versioning {
    enabled = "true"
  }
}

resource "aws_s3_bucket_object" "object" {
  bucket = "first-vt-bucket-1511"
  key = "first_object"
  source = "${path.module}/assert.py"
  etag = "${filemd5("${path.module}/assert.py")}"

  depends_on = ["aws_s3_bucket.first_bucket"]
}
