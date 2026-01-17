import csv
import json
import os

def parse_tools(tools_str):
    """
    Parse tools string format: "Name|Url;Name2|Url2"
    Returns list of dicts: [{"name": "Name", "url": "Url"}, ...]
    """
    if not tools_str:
        return []
    
    tools = []
    items = tools_str.split(';')
    for item in items:
        if '|' in item:
            name, url = item.split('|', 1)
            tools.append({"name": name.strip(), "url": url.strip()})
    return tools

def main():
    csv_file = 'prompts.csv'
    json_file = 'data.json'

    if not os.path.exists(csv_file):
        print(f"Error: {csv_file} not found.")
        return

    data = []
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Parse ID
            try:
                id_val = int(row['id'])
            except ValueError:
                continue # Skip rows with invalid ID

            # Parse Tags (comma separated)
            tags = [t.strip() for t in row['tags'].split(',') if t.strip()]

            # Parse Tools
            tools = parse_tools(row.get('tools', ''))

            # Handle Image (empty string -> None)
            image = row['image'] if row['image'].strip() else None

            # Construct Item
            item = {
                "id": id_val,
                "title": row['title'],
                "image": image,
                "prompt": row['prompt'],
                "category": row['category'],
                "tags": tags,
                "tools": tools
            }
            data.append(item)

    # Write JSON
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"Successfully converted {len(data)} items from {csv_file} to {json_file}")

if __name__ == "__main__":
    main()
