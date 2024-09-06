import dataclasses


@dataclasses.dataclass
class _AppSettings:
    title: str
    should_shout: bool = False
    skip_country_codes: list = dataclasses.field(default_factory=list)

    def print_app_title(self):
        title = self.title.upper() if self.should_shout else self.title
        print(title)


settings = _AppSettings(title="Divisions Finder", skip_country_codes=["DE"])
