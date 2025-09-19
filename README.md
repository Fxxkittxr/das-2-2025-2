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
- Serviços Computacionais da AWS:
    - Serviços que permitem rodar aplicações e processar dados na nuvem, variando do controle total de servidores virtuais (IaaS) até soluções completamente gerenciadas (Serverless).

- Amazon Elastic Compute Cloud (EC2):
    - É o serviço de IaaS (Infraestrutura como Serviço) da AWS. Ele permite alugar servidores virtuais (instâncias) para rodar sistemas operacionais e aplicações. É ideal quando você precisa de controle total sobre o ambiente de computação.

- Amazon Machine Images (AMI):
    - Um template pré-configurado que contém o sistema operacional, software e configurações para lançar uma instância EC2. É como uma "imagem" de um servidor pronta para ser usada.

- Tipos de Instâncias:
    - As instâncias EC2 são classificadas por famílias, otimizadas para diferentes cargas de trabalho (computação intensiva, memória, armazenamento, etc.). Por exemplo, as instâncias t são para uso geral e as c para cargas de trabalho de computação.

- Tipos de Storage (EBS/Instance Store):
  - Amazon Elastic Block Store (EBS): Oferece volumes de armazenamento em blocos persistentes que podem ser anexados a uma instância EC2. Os dados persistem mesmo se a instância for encerrada.
  - Instance Store: Armazenamento temporário e de alta performance que é fisicamente conectado ao servidor host da instância EC2. Os dados são perdidos quando a instância é interrompida ou encerrada.
    
- Acesso via SSH: 
  - O Secure Shell (SSH) é um protocolo de rede usado para acessar e gerenciar instâncias EC2 Linux de forma segura através da linha de comando. Para instâncias Windows, o acesso geralmente é feito via RDP (Remote Desktop Protocol).


## Aula 10/09

- Elastic File System (EFS) / FSx:
  - Amazon EFS: Um serviço de armazenamento de arquivos escalável e sem servidor para instâncias EC2. Ele é projetado para ser compartilhado por várias instâncias ao mesmo tempo, ideal para cargas de trabalho que precisam de acesso a arquivos compartilhados.
  - Amazon FSx: Oferece sistemas de arquivos nativos da Microsoft (FSx for Windows File Server) e do Lustre (FSx for Lustre) na nuvem, facilitando a migração de workloads que dependem desses sistemas.

- EC2 Windows: 
  - Assim como as instâncias EC2 Linux, você pode lançar instâncias EC2 com o sistema operacional Windows Server, usando-as para rodar aplicações Microsoft.

- Lab: 
  -  Fazer: [Guided lab: Introducing Amazon Elastic File System (Amazon EFS)](https://awsacademy.instructure.com/courses/129676/assignments/1485164?module_item_id=12389242)


## Aula 17/09

- EC2:
  - Serviço de computação que permite lançar e gerenciar instâncias virtuais na AWS, com flexibilidade de configuração e escalabilidade.

- User Data:
  - Script que pode ser configurado na inicialização da instância para automatizar tarefas, como instalação de pacotes ou execução de comandos.

- Instance Metadata:
  - Informações acessíveis de dentro da instância, como ID, tipo, região e credenciais temporárias.

- Placement:
  - Define como as instâncias EC2 são fisicamente distribuídas dentro das zonas de disponibilidade para melhorar redundância, latência ou performance.

- VPC (Virtual Private Cloud):
  - Rede virtual isolada na AWS, onde você pode configurar endereçamento IP, sub-redes, tabelas de rotas e gateways.

- Subnets Públicas e Privadas:
  - Subnet pública: acessível diretamente pela internet.
  - Subnet privada: isolada da internet, geralmente usada para recursos internos.

- Security Group e NACL:
  - Security Group: Firewall em nível de instância, que controla tráfego de entrada e saída.
  - Network ACL (NACL): Firewall em nível de subnet, que controla tráfego de rede entre sub-redes.

- VPN Site-to-Site:
  - Conexão segura entre sua rede local (on-premises) e a VPC na AWS.

- Peering:
  - Conexão entre duas VPCs diferentes para permitir comunicação entre recursos, sem precisar de VPN ou internet.
