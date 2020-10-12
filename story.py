class Post:
    def __init__(self, id, photo_url, name, body):
        self.id = id
        self.photo_url = photo_url
        self.name = name
        self.body = body

post1 = Post(id=1,
             photo_url='https://images.pexels.com/photos/415829/pexels-photo-415829.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=50&w=50',
             name='Sara',
             body='Lorem Ipsum')
post2 = Post(id=2,
             photo_url='https://images.pexels.com/photos/736716/pexels-photo-736716.jpeg?auto=compress&cs=tinysrgb&dpr=1&h=100&w=100',
             name='John',
             body='Lorem Ipsum')

updated_fields = {'name': 'Maryam',
                  'photo_url': 'https://images.pexels.com/photos/736716/pexels-photo-736716.jpeg?auto=compress&cs=tinysrgb&dpr=1&h=100&w=100',
                  'body': 'Lorem Ipsum'}

posts = [post1, post2]

class PostStore:
    
    def get_all(self):
        return posts

    def add(self, post):
        posts.append(post)

    def get_by_id(self, id):
        result = None

        for post in posts:
            if post.id == id:
                result = post
                break

        return result

    def delete(self, id):
        posts.remove(id)

    def update(self, id, fields, store):
        post = self.get_by_id(id)

        post.name = fields['name']

        post.photo_url = fields['photo_url']

        post.body = fields['body']
        
        store.update(1, updated_fields)



        