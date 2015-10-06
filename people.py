
from collections import defaultdict
import logging
import os
import sys

from pelican import signals, logger
# logger = logging.getLogger(__name__)

# def add_gallery_post(generator):
#
#     contentpath = generator.settings.get('PATH')
#     gallerycontentpath = os.path.join(contentpath,'people')
#
#     for article in generator.articles:
#         if article.metadata.get('template') == 'person':
#             name = article.metadata.get('title')
#             headshot = article.metadata.get('headshot')
#             position = article.metadata.get('position')
#
#
# def add_person_page(generator):
#
#     contentpath = generator.settings.get('PATH')
#     gallerycontentpath = os.path.join(contentpath, 'people')
#
#     for article in generator.articles:
#         if article.metadata.get('template') == 'person':
#             logger.debug(article.title)
            # album = page.metadata.get('gallery')
            # galleryimages = []
            #
            # pagegallerypath=os.path.join(gallerycontentpath, album)
            #
            # if(os.path.isdir(pagegallerypath)):
            #     for i in os.listdir(pagegallerypath):
            #         if not i.startswith('.') and os.path.isfile(os.path.join(os.path.join(gallerycontentpath, album), i)):
            #             galleryimages.append(i)
            #
            # page.album = album
            # page.galleryimages = sorted(galleryimages)


# def generate_people_page(generator):
#     logger.debug('Generating people page ...')
#
#     contentpath = generator.settings.get('PATH')
#     people_path = os.path.join(contentpath, 'people')
#     people_image_path = os.path.join(contentpath, 'images', 'people')
#
#     for page in generator.pages:
#         if page.metadata.get('template') == 'people':
#             people = dict()
#
#             # for article in generator.articles:
#             #     if article.metadata.get('template') == 'person':
#             #         name = article.metadata.get('title')
#             #         people[name] = article
#             for person in os.listdir(people_path):
#                 if not person.startswith('.'):
#                     prefix = person.split('.md')[0]
#                     logger.debug('prefix: \t{0}'.format(prefix))
#                     html = '{0}.html'.format(prefix)
#                     people[person] = html
#
#             page.people = people

# def generate_people_page(pages, persons):
#     logger.debug('Generating people page ...')
#     # articles, pages, statics = tuple(generators)
#     # logger.debug('Articles: {}'.format(str(articles)))
#     # logger.debug('Pages: {}'.format(str(pages)))
#     # logger.debug('Statics: {}'.format(str(statics)))
#
#     # people = dict()
#     #
#     # for person in articles.articles:
#     #     logger.debug('\t Adding {}'.format(person.title))
#     #     if person.metadata.get('template') == 'person':
#     #         people[person.title] = person
#     # logger.debug('People: {}'.format(str(people)))
#
#     for page in pages.pages:
#         if page.metadata.get('template') == 'people':
#             page.persons = persons
#
#     logger.debug('\tDone.')

def generate_people_page(generator):
    current = defaultdict(dict)
    alumni = defaultdict(dict)
    i = 0
    logger.debug('Gathering persons for people page ...')
    for page in generator.pages:
        if page.metadata.get('template') == 'person':
            i += 1
            if page.alumni_or_current.lower() == 'alumni':
                alumni[page.position][page.title] = page
            else:
                current[page.position][page.title] = page
            logger.debug('\tPage {}: {}'.format(page.title, dir(page)))
            logger.debug('\tPage {}: {}'.format(page.title, repr(page.__dict__)))
    logger.debug('\t Done. Found {} person pages.'.format(i))

    logger.debug('Adding persons to people page ...')
    for page in generator.pages:
        # logger.debug('Iterating over pages again ... {}'.format(page.title))
        if page.metadata.get('template') == 'people':
            page.persons = current
        if page.metadata.get('template') == 'alumni':
            page.persons = alumni
    logger.debug('\t Done.')


def register():
    # signals.article_generator_finalized.connect(add_gallery_post)

    # Order is important here. Need to create the invidual "person" pages
    # before adding the people page.
    # signals.all_generators_finalized.connect(generate_people_page)
    # signals.article_generator_finalized.connect(add_person_page)
    signals.page_generator_finalized.connect(generate_people_page)
    # signals.page_generator_finalized.send(generate_people_page, persons=persons)
    # signals.page_generator_finalized.connect(add_gallery_page)
