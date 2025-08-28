import boto3

s3_client = boto3.client('s3', region_name='us-east-1')

s3_client.create_bucket(Bucket='palomateixeira2002')

print ("bucket criado com sucesso")