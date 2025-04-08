from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider
from .views import SuapOAuth2Adapter


class SuapAccount(ProviderAccount):
    def get_avatar_url(self):
        return self.account.extra_data.get("foto")


class SuapOAuth2Provider(OAuth2Provider):
    id = "suap"
    name = "SUAP"
    account_class = SuapAccount
    oauth2_adapter_class = SuapOAuth2Adapter

    def get_default_scope(self):
        scope = ["identificacao", "email"]
        return scope

    def extract_uid(self, data):
        return str(data.get("identificacao"))

    def extract_common_fields(self, data):
        nome_completo = data.get("nome_registro")
        if nome_social := data.get("nome_social"):
            nome_completo = nome_social
        primeiro_nome, *_, ultimo_nome = nome_completo.split()
        return dict(
            username=data.get("identificacao"),
            email=data.get("email"),
            first_name=primeiro_nome,
            last_name=ultimo_nome,
        )


provider_classes = [SuapOAuth2Provider]
