data "local_file" "foo" {
    filename = "./assert.py"
}

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
  source = "${local_file.foo.filename}"
  etag = "${filemd5("${local_file.foo.filename}")}"

  depends_on = ["aws_s3_bucket.first_bucket"]
}
