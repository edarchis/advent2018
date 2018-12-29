import datetime
import re
from collections import namedtuple, defaultdict
from operator import itemgetter

LogEntry = namedtuple("LogEntry", ["date_time", "wakes_up", "begins_shift", "asleep"])
Siesta = namedtuple("Siesta", ["guard", "sleep_from", "sleep_to"])


def load_file(filename):
    log_matcher = re.compile(r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\] (.*)")
    guard_matcher = re.compile(r"Guard #(\d+) begins shift")
    logs = []
    for line in open(filename):
        log_matched = log_matcher.match(line)
        if log_matched:
            str_date = log_matched.group(1)
            str_action = log_matched.group(2)
            guard_matched = guard_matcher.match(str_action)
            parsed_date = datetime.datetime.strptime(str_date, '%Y-%m-%d %H:%M')
            logs.append(
                LogEntry(
                    parsed_date,
                    True if "wakes up" in str_action else False,
                    int(guard_matched.group(1)) if guard_matched else None,
                    True if "falls asleep" in str_action else False,
                )
            )
    return sorted(logs, key=lambda k: k.date_time)


def compute_siestas(notes):
    current_guard = None
    asleep_start = None
    guards_siestas = []
    for log_entry in notes:
        if log_entry.begins_shift:
            current_guard = log_entry.begins_shift
        elif log_entry.asleep:
            asleep_start = log_entry.date_time
        elif log_entry.wakes_up:
            guards_siestas.append(
                Siesta(current_guard, asleep_start, log_entry.date_time)
            )
    return guards_siestas


def compute_guard_sleep_time(siestas):
    guards_sleep = defaultdict(lambda: 0)
    for siesta in siestas:
        guards_sleep[siesta.guard] += int((siesta.sleep_to - siesta.sleep_from).seconds / 60)
    return guards_sleep


def sleepiest_guard(guards_sleep):
    return max(guards_sleep.items(), key=lambda kv: kv[1])


def sleep_minutes(siestas, guard=None):
    guard_minutes = defaultdict(lambda: 0)
    for siesta in siestas:
        if guard is None or guard == siesta.guard:
            for minute in list(range(siesta.sleep_from.minute, siesta.sleep_to.minute)):
                guard_minutes[minute] += 1
    return guard_minutes


sample_notes = load_file("sample.txt")
print(sample_notes)
sample_siestas = compute_siestas(sample_notes)
sample_guards_sleep = compute_guard_sleep_time(sample_siestas)
max_guard = sleepiest_guard(sample_guards_sleep)
print("max guard:", max_guard)
sample_minutes = sleep_minutes(sample_siestas, max_guard[0])
max_minute = max(sample_minutes.items(), key=itemgetter(1))
print("max minute", max_minute)
print("solution:", max_minute[0] * max_guard[0])

actual_notes = load_file("input.txt")
print(actual_notes)
actual_siestas = compute_siestas(actual_notes)
actual_guards_sleep = compute_guard_sleep_time(actual_siestas)
max_guard = sleepiest_guard(actual_guards_sleep)
print("max guard:", max_guard)
actual_minutes = sleep_minutes(actual_siestas, max_guard[0])
max_minute = max(actual_minutes.items(), key=itemgetter(1))
print("max minute", max_minute)
print("solution:", max_minute[0] * max_guard[0])
pass
