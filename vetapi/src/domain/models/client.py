from vetapi.src.domain.models.contact import Contact


class Client(Contact):
    id_client: int | None = None
