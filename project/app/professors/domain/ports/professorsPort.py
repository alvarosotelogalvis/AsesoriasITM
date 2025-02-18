class professorPort:

    def get_professor(self, **kwargs):
        raise NotImplementedError

    def get_professor_by_identification_card(
        self,
        identification_card: int
    ):
        raise NotImplementedError

    def create_professor(self, **kwargs):
        raise NotImplementedError

    def update_professor(self, identification_card: int, **kwargs):
        raise NotImplementedError
