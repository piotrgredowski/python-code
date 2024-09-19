import abc


# Observer
class Subscriber(abc.ABC):
    @abc.abstractmethod
    def update(self, message: str) -> None:
        pass


# Subject
class Publisher(abc.ABC):
    def __init__(self) -> None:
        self._subscribers: list[Subscriber] = []

    @abc.abstractmethod
    def attach(self, subscriber: Subscriber) -> None:
        pass

    @abc.abstractmethod
    def detach(self, subscriber: Subscriber) -> None:
        pass

    @abc.abstractmethod
    def notify(self) -> None:
        pass


class PressAgency(Publisher):
    def __init__(self):
        super().__init__()

        self._news = []

    def attach(self, subscriber):
        self._subscribers.append(subscriber)

    def detach(self, subscriber):
        self._subscribers.remove(subscriber)

    def notify(self):
        latest_news = self._news[-1]
        for subscriber in self._subscribers:
            subscriber.update(latest_news)

    def add_news(self, news):
        print(f">>>>>> News from press agency: {news} <<<<<<\n")
        self._news.append(news)
        self.notify()


class CCB(Subscriber):
    def print_news(self, news: str):
        print(f"CCB reports: {news}")
        print()

    def update(self, message: str) -> None:
        self.print_news(message)


class WeeklyMail(Subscriber):
    def format_news(self, news: str):
        return f"Weekly Mail exclusive news: {news} Only in Weekly Mail!"

    def print_news(self, news: str):
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(self.format_news(news))
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print()

    def update(self, message: str) -> None:
        self.print_news(message)


class TheMoon(Subscriber):
    def format_news(self, news: str):
        return f"The Moon reveals: {news}"

    def print_news(self, news: str):
        print(self.format_news(news))
        print()

    def update(self, message: str) -> None:
        if "COVID" not in message.upper():
            self.print_news(message)


class IphoneNews(Subscriber):
    def format_news(self, news: str):
        return f"IPHONE NEWS: {news}"

    def print_news(self, news: str):
        print(self.format_news(news))
        print()

    def update(self, message: str) -> None:
        if "IPHONE" in message.upper():
            self.print_news(message)


class NewsSubscriber(Subscriber):
    def __init__(self, name: str):
        self.name = name

    def update(self, news: str):
        print(f"{self.name} got the news: {news}")


if __name__ == "__main__":
    agency = PressAgency()
    bbc = CCB()
    daily_mail = WeeklyMail()
    the_sun = TheMoon()

    agency.attach(bbc)
    agency.attach(daily_mail)
    agency.attach(the_sun)

    agency.add_news("COVID-19 vaccine is ready!")
    print("\n\n")
    agency.add_news("New president elected!")
    print("\n\n")

    agency.attach(NewsSubscriber("John"))
    iphone_news = IphoneNews()
    agency.attach(iphone_news)

    agency.add_news("New iPhone released!")
    print("\n\n")
    agency.add_news("New Tesla model announced!")
