import boto3

s3_client = boto3.client('s3', region_name='us-east-1')
s3_client.upload_file('./s3/exemplo.txt', 'palomateixeira2002', 'exemplo.txt')#origem do arquivo, nome do bucket, nome do arquivo no bucket

print ("upload feito com sucesso") #arquivo exemplo.txt foi enviado para o bucket palomateixeira2002

