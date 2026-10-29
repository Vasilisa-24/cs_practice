import csv
import json
import re
from io import StringIO

def csv_to_records(text):
    reader = csv.DictReader(StringIO(text))
    return [dict(row) for row in reader]

def _parse_value(value):
    value = value.strip()
    if value.lower() in ("true", "yes"):
        return True
    if value.lower() in ("false", "no"):
        return False
    if re.fullmatch(r"[+-]?\d+", value):
        return int(value)
    if re.fullmatch(r"[+-]?(?:\d+\.\d*|\.\d+)", value):
        return float(value)
    return value

def parse_settings(lines):
    settings = {}
    current_list_key = None
    for line in lines:
        line = line.split("#", 1)[0].strip()
        if not line:
            continue
        if line.startswith("- "):
            if current_list_key is not None:
                settings[current_list_key].append(_parse_value(line[2:]))
            continue
        current_list_key = None
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value == "":
            settings[key] = []
            current_list_key = key
        else:
            settings[key] = _parse_value(value)
    return settings
def merge_by_key(rows: list[dict], extra: dict, key: str = "id",):
    result = []
    for row in rows:
        additional_fields = extra.get(row.get(key), {})
        result.append({**additional_fields, **row})
    return result

def records_to_json(records):
    return json.dumps(records,indent=2,sort_keys=True,ensure_ascii=False)
