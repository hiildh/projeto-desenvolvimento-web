# Projeto Django - Celulares

Este é um projeto Django para gerenciar notícias sobre celulares, links de venda e comentários. O projeto usa CockroachDB como banco de dados.

## Configuração do Ambiente

### Pré-requisitos

- Python 3.9+
- Django 4.0+
- CockroachDB
- CA Cert (Apenas uma vez)
<!-- - [CockroachDB CLI](https://www.cockroachlabs.com/docs/stable/install-cockroachdb.html) (para gerar o certificado de segurança) -->

### Passos para rodar o projeto localmente

#### 1. Clone o repositório
```bash
git clone https://github.com/hiildh/projeto-desenvolvimento-web.git
cd projeto-desenvolvimento-web
```
#### 2. Crie e ative o ambiente virtual
No terminal, crie um ambiente virtual para o projeto:
```bash
python -m venv venv
```
Ative o ambiente virtual:
 - No Windows:
 ```bash
 venv\Scripts\activate
 ```
 - No macOS/Linux:
 ```bash
 source venv/bin/activate
 ```
#### 3. Instale as dependências
Com o ambiente virtual ativo, instale as dependências listadas no ``requirements.txt``:
```bash
pip install -r requirements.txt
```
#### 4. Configuração do CockroachDB

##### a. Baixar o Certificado CA (somente uma vez)

O CockroachDB requer um certificado CA para verificação do servidor. Siga as instruções abaixo de acordo com o seu sistema operacional:

##### **Windows**
Execute o seguinte comando no PowerShell para baixar o certificado CA para a verificação do servidor:

```bash
mkdir -p $env:appdata\postgresql\; Invoke-WebRequest -Uri https://cockroachlabs.cloud/clusters/ae57a6f8-893b-4f15-8c9b-a3f46b2bb873/cert -OutFile $env:appdata\postgresql\root.crt
````

#### **Linux / macOS**
Execute o seguinte comando para baixar o certificado CA para a verificação do servidor:

```bash
curl --create-dirs -o $HOME/.postgresql/root.crt 'https://cockroachlabs.cloud/clusters/ae57a6f8-893b-4f15-8c9b-a3f46b2bb873/cert'
```
#### 5. Executar o servidor
Agora, você pode rodar o servidor localmente:
```bash
python manage.py migrate
```
O servidor estará disponível no endereço ``http://127.0.0.1:8000/``.

> ### Observações:
> 
> 1. **Alterações no `models.py`**: Se realizar alteração no `models.py`, tem que rodar o migrations direcionando a pasta core assim:
>    ```bash
>    python manage.py makemigrations core
>    ```
> 
> 2. **Rota para adicionar notícias**: Para adicionar notícias, utilize a rota `/adicionar-noticia` no seu navegador após iniciar o servidor e inserir as informações da notícia manualmente pelo editor de código no dicionário abaixo.
>   ```python
>       noticia = Noticia.objects.create(
>            titulo="título da notícia",
>            conteudo="pequeno resumo",
>            autor="autor",  # O nome do site ou fonte da notícia
>            link="link da noticia",
>            imagem_link="link da imagem da noticia"
>        )
>   ```

