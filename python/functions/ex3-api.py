from functools import partial
user = {
    'name': "John",
    'networks': [
        {
            'name': 'facebook',
            'profile_image': "",
            'cover_image': "image1"
        },
        {
            'name': 'facebook',
            'profile_image': "image2",
            'cover_image': ""
        }
    ]
}


def get_profile_image(user):
    for net in user['networks']:
        if net['cover_image']:
            return net["profile_image"]
    return 'default'


def get_cover_image(user):
    for net in user['networks']:
        if net['cover_image']:
            return net["cover_image"]
    return 'default'


def get_image(which_image, user):
    for net in user['networks']:
        if net[which_image]:
            return net[which_image]
    return 'default'


get_profile_image = partial(get_image, 'profile_image')
get_cover_image = partial(get_image, 'cover_image')

print('partial output end')
print(get_profile_image(user))
print(get_cover_image(user))
