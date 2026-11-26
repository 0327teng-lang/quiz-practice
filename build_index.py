import json
import pathlib

root = pathlib.Path(__file__).parent / "exams"
items = []

for f in sorted(root.glob("*.json")):
    if f.name == "index.json":
        continue
    data = json.loads(f.read_text(encoding="utf-8"))
    items.append({
        "id": data.get("id", f.stem),
        "title": data["title"],
        "subject": data.get("subject", "未分類"),
        "year": data.get("year"),
        "file": f.name,
        "count": len(data["questions"]),
    })

items.sort(key=lambda x: (-(x["year"] or 0), x["title"]))
(root / "index.json").write_text(
    json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"完成，共 {len(items)} 份考卷")
