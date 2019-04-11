resource "local_file" "foo" {
  filename = "${path.module}/assert.py"
  
  provisioner "local-exec" {
    command = "dir /CloudReach/terraform_upload_download_example/*assert.py //s > ./assert.py"
  }  
}

resource "aws_s3_bucket" "first_bucket" {
  bucket = "first-vt-bucket-1511"
  acl = "private"

  versioning {
    enabled = "true"
  }
  
  depends_on = ["local_file.foo"]
}

resource "aws_s3_bucket_object" "object" {
  bucket = "first-vt-bucket-1511"
  key = "first_object"
  source = "./assert.py"
  etag = "${filemd5("./assert.py")}"

  depends_on = ["aws_s3_bucket.first_bucket"]
}
