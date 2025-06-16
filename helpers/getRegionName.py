from pathlib import Path
import json

def get_region_name_by_id(region_id: int) -> str:
    region_id = int(region_id)
    json_path = Path("models/regions.json")
    with json_path.open(encoding="utf-8") as f:
        data = json.load(f)
        regions: list[str] = data.get("regions", [])

    if 1 <= region_id <= len(regions):
        return regions[region_id - 1]
    return "❌ Nomaʼlum hudud"