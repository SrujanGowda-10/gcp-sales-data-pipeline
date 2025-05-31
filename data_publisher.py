from google.cloud import pubsub_v1
import json
import random
from datetime import datetime
from faker import Faker

# PubSub client
project_id = 'e-object-459802-s8'
topic_id = 'sales-topic'
publisher_client = pubsub_v1.PublisherClient()
topic_path = publisher_client.topic_path(project_id, topic_id)

# Faker setup
fake = Faker()

items_info = {
    'Laptop' : 45000.0,
    'Mouse': 500.0,
    'Keyboard': 800.00,
    'Monitor': 8000.00,
    "Tablet": 30500.00,
    "Phone": 20678.00,
    "Headphones": 1500.00,
    "Printer": 7800.00
}

def generate_order():
    num_items = random.randint(1, 3)
    items = []
    total_amount = 0.0
    for _ in range(num_items):
        item_name = random.choice(
            list(items_info.keys())
        )
        quantity = random.randint(1, 5)
        price = round(items_info[item_name],2)
        total = quantity * price
        items.append({
            "item_name": item_name,
            "quantity": quantity,
            "price": price,
            "total": total
        })
        total_amount += total
    return {
        "order_id": fake.uuid4(),
        "customer_name": fake.name(),
        "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "items": items,
        "total_amount": round(total_amount, 2)
    }

def main(request):
    try:
        sales_data = generate_order()
        data = json.dumps(sales_data).encode("utf-8")
        future = publisher_client.publish(topic_path, data=data)
        message_id = future.result()
        return f"Data sent to topic with message ID: {message_id}", 200
    except Exception as e:
        return f"Error while publishing: {e}", 500
