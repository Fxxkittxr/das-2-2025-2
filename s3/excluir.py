import boto3

# Cria um recurso S3 usando boto3 na região us-east-1
s3_client = boto3.resource('s3', region_name='us-east-1')  # usar resource para listar objetos por ser alto nível

# Seleciona o bucket pelo nome
bucket = s3_client.Bucket("palomateixeira2002")  # nome do bucket

# Percorre todos os objetos do bucket e exclui cada um
for obj in bucket.objects.all():  # percorrer todos os objetos do bucket
    print(f"Excluindo: {obj.key} - {obj.size} bytes")  # exibe o nome e tamanho do arquivo que será excluído
    obj.delete()  # exclui o objeto

print("Todos os objetos foram excluídos do bucket.")  # confirma que todos os objetos foram excluídos