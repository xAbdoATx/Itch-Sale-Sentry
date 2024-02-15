import time
import json
import sqlite3
import requests
from datetime import datetime
from discord_webhook import DiscordWebhook, DiscordEmbed


with open('config.json') as config_file:
    config = json.load(config_file)

track_url = config["track_url"]
webhook_url = config["webhook_url"]
webhook_image = config["webhook_image"]
webhook_name = config["webhook_name"]

conn = sqlite3.connect('update_tracker.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS updates (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_url TEXT,
        last_update TEXT,
        sent_item_ids TEXT
    )
''')
conn.commit()

def get_file_content(file_url):
    response = requests.get(file_url)
    return response.json()

def send_discord_notification(embed, sender_name):
    current_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
    footer_text = f"Coded BY ✨ {sender_name} ✨ - ⏰ {current_time}"

    embed.set_footer(text=footer_text)
    
    webhook = DiscordWebhook(url=webhook_url, avatar_url=webhook_image, username=webhook_name)
    webhook.add_embed(embed)
    webhook.execute()

def convert_to_readable_date(date_str):
    return datetime.fromisoformat(date_str[:-1]).strftime('%Y-%m-%d %H:%M:%S UTC')

def track_updates(file_url):
    last_update_info = cursor.execute('SELECT last_update, sent_item_ids FROM updates WHERE file_url = ?', (file_url,)).fetchone()
    last_update = last_update_info[0] if last_update_info else None
    sent_item_ids = set(json.loads(last_update_info[1])) if last_update_info and last_update_info[1] else set()

    current_content = get_file_content(file_url)

    if last_update != current_content:
        current_content_json = json.dumps(current_content, default=lambda x: list(x) if isinstance(x, set) else x)
        sent_item_ids_json = json.dumps(list(sent_item_ids))
        cursor.execute('INSERT OR REPLACE INTO updates (file_url, last_update, sent_item_ids) VALUES (?, ?, ?)', (file_url, current_content_json, sent_item_ids_json))
        conn.commit()

        new_sent_item_ids = set()

        for category, items in current_content.items():
            for item in items:
                item_id = item.get('id')

                if item_id not in sent_item_ids:
                    sales_link = f"https://itch.io{item['sales_link']}" if item['sales_link'] else None

                    embed = DiscordEmbed(title=f"{item['title']}",
                                         description=f":page_facing_up: **Description:** {item['description']}\n\n"
                                                     f":bust_in_silhouette: **Author:** ``{item['author']}``\n"
                                                     f":file_folder: **Category:** ``{category.upper()}``\n"
                                                     f":hourglass_flowing_sand: **End Date:** ``{convert_to_readable_date(item['end_date'])}``\n\n"
                                                     f"[Open in browser 🡥]({item['link']})  -  [Sales Link 🡥]({sales_link})"
                                                     )
                    embed.set_image(url=item['img_link'])

                    try:
                        send_discord_notification(embed, "xAbdoAT")
                        print(f"[Done] {category}, Title: {item['title']}")
                        new_sent_item_ids.add(item_id)
                    except Exception as e:
                        print(f"[Fail] {category}, Title: {item['title']}")
                        print(f"Error: {e}")

                    time.sleep(1)

        cursor.execute('UPDATE updates SET sent_item_ids = ? WHERE file_url = ?', (json.dumps(list(sent_item_ids.union(new_sent_item_ids))), file_url))
        conn.commit()

track_updates(track_url)

conn.close()
