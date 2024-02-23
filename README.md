<p align="center">
    <img width="400" height="200" src=".github/logo.png" title="Logo do projeto"> <br />
    <img src="https://img.shields.io/maintenance/yes/2020?style=for-the-badge" title="Status do projeto">
    <img src="https://img.shields.io/github/workflow/status/ccuffs/guia-tcc/ci.uffs.cc?label=Build&logo=github&logoColor=white&style=for-the-badge" title="Status do build">
</p>

# Sistema de monitoração patrimonial integrado a detecção de incêndio e acionamento.
Este repositório possui os códigos-fonte, DockerImages, ClusterConfigs, e outros arquivos necessários para a contrução do projeto.
O sistema propõe a monitoração de patrimônios, utilizando principamente de sistemas de monitoramento, sistemas de alarme e sistemas de abertura de fechaduras remotamente.
## Vídeomonitoramento
### Circuito de câmeras:
O sistema de monitoramento conta com um circuito de câmeras, posicionadas de acordo com a necessidade do cliente e em locais estratégicos visando cobrir a maior área do imóvel possível. Essa rede de câmeras é conectada a uma raspberry, tecnologia que possui um sistema operacional linux, responsável por tratar as imagens recebidas das câmeras a partir da inteligência artificial, descrita abaixo. Após o tratamento das inagens, as mesmas são enviadas a partir de um POST ao servidor de banco de dados, onde serão armazenadas as imagens para consulta do cliente.
### Raspberry Pi
A raspberry possui um sistema operacional Linux, ambiente responsável por receber as imagens recebidas a partir de um módulo de imagem, enviadas a partir do circuito de câmeras acima. Após o recebimento, o SO executa a Inteligência artificial descrita abaixo passando as imagens recebidas como parâmetro para tratamento. Após o tratamento da imagem, os arquivos são enviados a um servidor responsável por armazenar no banco de dados e apresentar ao cliente.
### Inteligência artificial
A inteligência artificial é responsável por analisar as imagens recebidas como parâmetro, com o objetivo de detectar possíveis frames onde exista principios de incêndios. Após a análise, um script deve formatar a imagem em <extensão do arquivo> e enviar ao servidor (descrição abaixo).
Caso o retorno seja verdadeiro para incêndio, um script deve fazer um POST na API destinada, informando o incêndio, após realizar o POST, a ML deve continuar a validação para a próxima imagem. Em caso de não detecção, o sistema deve seguir a validação para a próxima imagem.
### Servidor
O ambiente do servidor está rodando no Google Cloud Provider, orquestrando as tecnologias implementadas a partir do kubernetes. O servidor possui o Kong como API gateway, responsável por receber as imagens.
- Kong:
  
      Envia os dados recebidos para o service NGINX.
  
- Service NGINX:

      O Service NGINX é responsável por enviar os dados para o deployment definido na configuração, a partir de um parâmetro enviado do pelo Kong.

- Deployment:
    - Deployment de dados:
    
          O deployment é responsável por formatar os dados para o formato exigido pelo banco de dados e inseri-lo no banco de dados.
