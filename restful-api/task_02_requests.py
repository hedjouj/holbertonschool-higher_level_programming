import requests
import csv 

def fetch_and_print_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    if response.status_code == 200:
        posts = response.json()

        clean_posts = []
        for post in posts:
            clean_posts.append({
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            })

        with open('post.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(clean_posts)
    else:
        print("Failed to retrieve posts for saving.")