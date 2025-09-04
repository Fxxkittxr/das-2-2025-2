# Design e Arquitetura de Software II 2025/2

[AWS Canvas](https://awsacademy.instructure.com/courses/129676)

## Aula 30/07
- Well Architect Framework:
  Guia da AWS para construir sistemas na nuvem com foco em cinco pilares: segurança, performance, confiabilidade, eficiência de custo e excelência operacional. O objetivo é criar arquiteturas sólidas e eficientes.
- Trade-offs:
  Conceito fundamental em arquitetura. É a necessidade de fazer escolhas que sacrificam um atributo em favor de outro, como trocar custo por maior performance ou latência por consistência.
  
## Aula 06/08
- Modelo de responsabilidade compartilhada
  A segurança na nuvem é uma responsabilidade mútua entre a AWS (segurança da nuvem, ou seja, a infraestrutura física) e o cliente (segurança na nuvem, ou seja, a configuração de segurança dos recursos e dados).
- Princípio do privilégio mínimo
  Prática de segurança que concede a usuários, grupos e serviços apenas as permissões estritamente necessárias para realizar suas tarefas.
- Autenticação e Autorização
  Autenticação é o processo de verificar a identidade de um usuário ou serviço. Autorização é o processo de determinar quais permissões essa identidade tem.
- IAM User
  IAM User é uma identidade para uma pessoa ou aplicação. IAM Role é uma identidade que pode ser temporariamente assumida para acessar recursos sem a necessidade de credenciais permanentes.
- IAM Role

## Aula 13/08
- Identity Based Policies
  Políticas de permissão que são anexadas a uma identidade do IAM (usuário, grupo ou role).
  
- Resource Based Policies
  Políticas de permissão que são anexadas diretamente a um recurso, como um bucket S3.
  
- Fazer: [Module 2 Knowledge Check](https://awsacademy.instructure.com/courses/113113/assignments/1270651?module_item_id=10653588)
- Fazer: [Guided Lab: Exploring AWS Identity and Access Management (IAM)](https://awsacademy.instructure.com/courses/113113/assignments/1270605?module_item_id=10653616)
- Fazer: [Module 3 Knowledge Check](https://awsacademy.instructure.com/courses/113113/assignments/1270652?module_item_id=10653624)

## Aula 20/08
- Block Storage
  Tipo de armazenamento ideal para sistemas operacionais e bancos de dados, que requerem acesso de alta performance.
- File Share
  Sistema de armazenamento em rede que permite que múltiplos usuários e aplicações acessem arquivos compartilhados simultaneamente.
- Object Store
  Armazenamento para dados não estruturados, como imagens, vídeos, backups e logs. É altamente escalável e durável.
- S3 resumo geral
  O serviço de object store da AWS. É um dos serviços de armazenamento mais duráveis e escaláveis do mercado, amplamente utilizado para hospedagem de sites estáticos, data lakes e backup.
- Fazer: [lab: Creating a Static Website for the Cafe](https://awsacademy.instructure.com/courses/129676/assignments/1485129?module_item_id=12389220)

## Aula 27/08
- O S3 é um sistema de armazenamento de objetos, não de arquivos. Ele trabalha com dados e metadados. Isso significa que cada arquivo guardado no S3 vem junto com informações adicionais, como uma chave de criptografia, facilitando o gerenciamento e a segurança.
- Bucket: É o contêiner onde os dados são armazenados no S3.
  
- Considerações de escolha da região para criar o bucket: A escolha da região é crucial e deve levar em conta:
    - Leis de privacidade de dados e conformidade regulatória: Para garantir que os dados atendam aos requisitos legais de onde estão localizados.
    - Proximidade dos usuários aos dados: Para reduzir a latência e melhorar a performance de acesso.
    - Disponibilidade e recursos do serviço: Certas regiões podem ter serviços ou recursos mais recentes.
    - Custo-benefício: Os custos de armazenamento e transferência de dados podem variar entre as regiões.
- Amazon S3 Inventário do Bucket: Ferramenta para gerenciar de forma automatizada e detalhada o conteúdo de um bucket. Ele gera relatórios com a lista de todos os objetos e seus metadados, o que ajuda a organizar e auditar o que está armazenado.

## Aula 03/09
- Diferença entre S3 e EC2
    - s3 site estatico, entrega a interface
    - EC2 site dinamico, entrega o backend

- VMs - Amazon elastic compute cloud

- VPS - Amazon Lightsail

- PaaS - AWS Elastic Beanstalk

- Serverless
  - AWS Lampda
  - AWS Fargate
    
- Containers
  - Amazon Elastic Kubernetes Services
  - Amazon Elastic Container Service
