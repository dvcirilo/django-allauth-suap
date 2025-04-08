# Social Login Provider do SUAP para o django-allauth

Esse projeto permite a autenticação OAuth2 do [SUAP](https://portal.suap.ifrn.edu.br/) para projetos [Django](https://www.djangoproject.com/) que usem a biblioteca [django-allauth](https://docs.allauth.org/en/latest/).

## Instalação
- Instale e configure o Django Allauth conforme a [documentação](https://docs.allauth.org/en/latest/)
- Instale o pacote `django-allauth-suap`:
```
pip install django-allauth-suap
```
### `settings.py`
- Adicione ao `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...
    # Padrão do allauth
    allauth
    allauth.account
    allauth.socialaccount

    # SUAP Provider
    allauth_suap
    ...
]
```
- Não esqueça das demais configurações do `allauth` em `AUTHENTICATION_BACKENDS`, `MIDDLEWARE` e `urls.py`.
- Gere as chaves de API do SUAP em https://suap.ifrn.edu.br/admin/api/aplicacaooauth2/ com as seguintes informações:
```
Name: Nome do App
Authorization grant type: Authorization code
# Em desenvolvimento usar o exemplo abaixo e em produção ajustar o domínio, porta e protocolo (HTTPS), mantendo o endpoint.
Redirect URIs:
http://127.0.0.1:8000/accounts/suap/login/callback/
Client type: Confidential # Já que as chaves ficam seguras no back-end.
Algorithm: No OIDC support
Ativo: check
```
- Guarde o `Client secret` pois não será mostrado novamente;
- Adicione ao `settings.py` do projeto:
```python
SOCIALACCOUNT_PROVIDERS = {
    "suap": {
        # Talvez funcione para outras instituições apenas
        # mudando a URL, mas só foi testado no IFRN.
        "SUAP_URL": "https://suap.ifrn.br",
        # Escopo básico. Para acessar dados como CPF, adicione
        # "documentos_pessoais".
        "SCOPE": ["identificacao", "email"]
        "APP": {
            # IMPORTANTE! Use algum mecanismo para ler esses valores
            # de um .env, por exemplo.
            # Não suba suas chaves para o repositório!!
            "client_id": "seu_client_id",
            "secret": "seu_client_secret",
        },
    }
}
```

## Uso
- O Provider apenas recupera as informações básicas do usuário padrão Django: `username` (matrícula), `email`, `first_name` e `last_name`.
- Caso seja necessário recuperar mais dados (ex. cpf, campus), crie um SocialAcountAdapter customizado e use os métodos disponíveis, conforme a [documentação do allauth](https://docs.allauth.org/en/latest/socialaccount/adapter.html).

## Exemplos
- O projeto [Paca CMS](https://github.com/IFRN-SPP/paca-cms) usa esse pacote.

## Contribuições
O projeto está aberto a contribuições, inclusive para adequações que permitam o funcionamento com outras instituições que usem o SUAP.

## Referências
- [Documentação da API SUAP](https://suap.ifrn.edu.br/api/docs/)
- [suapi](https://github.com/IFRN/suapi)
- [suap-api-php](https://github.com/IFRN/suap-api-php)
- [cliente_suap_django](https://github.com/ifrn-oficial/cliente_suap_django)
- [cliente_suap_javascript](https://github.com/dvcirilo/cliente_suap_javascript)
