<p align="center">
    <img width="400" height="200" src=".github/logo.png" title="Logo do projeto"><br />
    <img src="https://img.shields.io/maintenance/yes/2020?style=for-the-badge" title="Status do projeto">
    <img src="https://img.shields.io/github/workflow/status/ccuffs/guia-tcc/ci.uffs.cc?label=Build&logo=github&logoColor=white&style=for-the-badge" title="Status do build">
</p>
# Sistema de monitoração patrimonial integrado a detecção de incêndio e acionamento.
Este repositório possui os códigos-fonte, DockerImages, ClusterConfigs, e outros arquivos necessários para a contrução do projeto.
O sistema propõe a monitoração de patrimônios, utilizando principamente de sistemas de monitoramento, sistemas de alarme e sistemas de abertura de fechaduras remotamente. 
### Sistema de câmeras:
O sistema de monitoramento conta com uma rede de câmeras, posicionadas de acordo com a necessidade do cliente e em locais estratégicos visando cobrir a maior área do imóvel possível. Essa rede de câmeras é conectada a uma raspberry, tecnologia que possui um sistema operacional linux, responsável por tratar as imagens recebidas das câmeras a partir da inteligência artificial, descrita abaixo. Após o tratamento das inagens, as mesmas são enviadas a partir de um POST ao servidor de banco de dados, onde serão armazenadas as imagens para consulta do cliente.

