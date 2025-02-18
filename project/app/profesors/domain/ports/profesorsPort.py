class ProfesorPort:

    def get_profesor(self, **kwargs):
        raise NotImplementedError

    def get_profesor_by_identification_card(
        self,
        identification_card: int
    ):
        raise NotImplementedError
