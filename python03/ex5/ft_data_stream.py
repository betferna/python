    #!/usr/bin/env python3
    import random
    from typing import Generator

    PLAYERS = ["alice", "bob", "charlie", "dylan"]
    ACTIONS = [
        "run",
        "eat",
        "sleep",
        "grab",
        "move",
        "climb",
        "swim",
        "release",
        "use",
    ]


    def gen_event() -> Generator[tuple[str, str], None, None]:
        while True:
            player = random.choice(PLAYERS)
            action = random.choice(ACTIONS)
            yield (player, action)


    def consume_event(events_list: list) -> Generator[tuple[str, str], None, None]:
        while events_list:
            index = random.randrange(len(events_list))
            event = events_list.pop(index)
            yield event


    def main() -> None:
        print("=== Game Data Stream Processor ===")

        stream = gen_event()

        for i in range(1000):
            player, action = next(stream)
            print(f"Event {i}: Player {player} did action {action}")

        ten_events = [next(stream) for _ in range(10)]
        print(f"Built list of 10 events: {ten_events}")

        for event in consume_event(ten_events):
            print(f"Got event from list: {event}")
            print(f"Remains in list: {ten_events}")


    if __name__ == "__main__":
        main()