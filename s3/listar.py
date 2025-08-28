import boto3

s3_client = boto3.resource('s3', region_name='us-east-1') #usar resource para listar objetos por ser alto nivel

bucket = s3_client.Bucket("palomateixeira2002")#nome do bucket
for obj in bucket.objects.all():#percorrer todos os objetos do bucket
    print(f" - {obj.key} - {obj.size} bytes")#exibir nome e tamanho do arquivo

    