#!/usr/bin/env python3

import typing
import random


players = ["alice", "bob", "charlie", "dylan"]
actions = [
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


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


def consume_event(
    events: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        index = random.randrange(len(events))
        event = events.pop(index)
        yield event


print("=== Game Data Stream Processor ===")

events = gen_event()

for i in range(1000):
    event = next(events)
    print(f"Event {i}: Player {event[0]} did action {event[1]}")

event_list = []

events = gen_event()

for i in range(10):
    event_list.append(next(events))

print(f"Built list of 10 events: {event_list}")

for event in consume_event(event_list):
    print(f"Got event from list: {event}")
    print(f"Remains in list: {event_list}")