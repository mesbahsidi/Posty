from store import PostStore, Post

post_store = PostStore()
dummy_posts = [
    Post(id=1,
         photo_url='https://images.pexels.com/photos/415829/pexels-photo-415829.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=50&w=50', 
         name='Sara', 
         body='Lorem Ipsum'),
    Post(id=2,
         photo_url='https://images.pexels.com/photos/736716/pexels-photo-736716.jpeg?auto=compress&cs=tinysrgb&dpr=1&h=100&w=100', 
         name='John', 
         body='Lorem Ipsum'),
]


def store_should_add_posts():
    for post in dummy_posts:
        post_store.add(post)
    
    # check if posts list has same length as dummy_posts list
    assert len(post_store.get_all()) == len(dummy_posts)


def get_by_id_should_retrieve_same_object():
    second_post = dummy_posts[1]
    retrieved_second_post = post_store.get_by_id(2)

    assert second_post is retrieved_second_post


store_should_add_posts()
get_by_id_should_retrieve_same_object()

print('All tests passed successfully!')