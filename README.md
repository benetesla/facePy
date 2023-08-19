# facePY - Sistema de Identificação de Idade com Base no Tamanho do Rosto

O facePY é um sistema simples em Python que utiliza o OpenCV para detectar rostos em tempo real e estimar a idade dos usuários com base nas dimensões dos rostos.

## Pré-requisitos

- Python 3.x
- Biblioteca OpenCV instalada (`pip install opencv-python`)
- Câmera (interna ou externa) para a detecção de rostos em tempo real

## Instalação

1. Clone este repositório para o seu ambiente local:
2. git clone https://github.com/benetesla/facePy.git
   
## Uso

1. Execute o script `identificar_idade.py`:

2. Uma janela de visualização será aberta, exibindo a câmera e a detecção de rostos em tempo real.
3. A idade estimada será exibida acima de cada rosto detectado, com base nas dimensões do rosto.

## Notas

- Este sistema utiliza uma estimativa simplificada da idade com base no tamanho do rosto detectado. Os resultados podem não ser precisos.
- A detecção de rostos depende da iluminação, ângulo da câmera e qualidade da imagem.
- Para obter resultados mais precisos, um modelo de Machine Learning treinado para identificação de idade seria necessário.

## Contribuições

Contribuições são bem-vindas! Se você deseja contribuir para este projeto, siga estas etapas:

1. Crie um fork deste repositório.
2. Crie uma branch com uma descrição clara da sua contribuição: `git checkout -b nome-da-sua-feature`.
3. Faça as alterações necessárias e adicione/commit as mudanças.
4. Envie um pull request explicando as mudanças que você fez.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.




