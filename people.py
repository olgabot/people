
from collections import defaultdict
import logging
import os
import sys

from pelican import signals, logger

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
            # logger.debug('\tPage {}: {}'.format(page.title, dir(page)))
            # logger.debug('\tPage {}: {}'.format(page.title, repr(page.__dict__)))
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
    signals.page_generator_finalized.connect(generate_people_page)
