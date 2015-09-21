import os
from pelican import signals


def add_gallery_post(generator):

    contentpath = generator.settings.get('PATH')
    gallerycontentpath = os.path.join(contentpath,'people')

    for article in generator.articles:
        if 'headshot' in article.metadata.keys():
            name = article.metadata.get('title')
            headshot = article.metadata.get('headshot')
            position = article.metadata.get('position')
            headshot = article.metadata.get('headshot')
            galleryimages = []


            articlegallerypath = os.path.join(gallerycontentpath, album)

            if(os.path.isdir(articlegallerypath)):
                for i in os.listdir(articlegallerypath):
                    if not i.startswith('.') and os.path.isfile(os.path.join(os.path.join(gallerycontentpath, album), i)):
                        galleryimages.append(i)

            article.album = album
            article.galleryimages = sorted(galleryimages)


def add_gallery_page(generator):

    contentpath = generator.settings.get('PATH')
    gallerycontentpath = os.path.join(contentpath,'people')

    for page in generator.pages:
        if 'gallery' in page.metadata.keys():
            album = page.metadata.get('gallery')
            galleryimages = []

            pagegallerypath=os.path.join(gallerycontentpath, album)

            if(os.path.isdir(pagegallerypath)):
                for i in os.listdir(pagegallerypath):
                    if not i.startswith('.') and os.path.isfile(os.path.join(os.path.join(gallerycontentpath, album), i)):
                        galleryimages.append(i)

            page.album = album
            page.galleryimages = sorted(galleryimages)


def generate_gallery_page(generator):

    contentpath = generator.settings.get('PATH')
    people_path = os.path.join(contentpath,'people')

    for page in generator.pages:
        if page.metadata.get('template') == 'people':
            people = dict()

            for person in os.listdir(people_path):
                if not person.startswith('.') and os.path.isdir(os.path.join(people_path, a)):

                    for i in os.listdir(os.path.join(people_path, a)):
                        if not a.startswith('.') and os.path.isfile(os.path.join(os.path.join(people_path, a), i)):
                            people.setdefault(a, []).append(i)
                    people[a].sort()

            page.people = people

def register():
    signals.article_generator_finalized.connect(add_gallery_post)
    signals.page_generator_finalized.connect(generate_gallery_page)
    signals.page_generator_finalized.connect(add_gallery_page)
