"""Module for the custom Django loadposts command."""

from curses import meta
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from posts.models import Post

class Command(BaseCommand):
    """Class for the custom loadposts command."""

    help = "Loads Markdown posts into the database."

    def handle(self, *args, **options):
        """Automatically called when the loadposts command is given."""

        for filename in os.listdir(settings.POST_ASSETS_DIR):
            abs_filename = os.path.abspath(os.path.join(settings.POST_ASSETS_DIR, filename))
            self.stdout.write(f'Processing post file: {abs_filename}')

            with open(abs_filename, 'r') as f:
                file_contents = f.read().split('===')

            try:
                raw_post_metadata = file_contents[1]
            except IndexError:
                self.stderr.write(f'ERROR: Post file {abs_filename} is missing a metadata block surrounded by "===".')

            try:
                post_content = file_contents[2]
            except IndexError:
                self.stderr.write(f'ERROR: Post file {abs_filename} is missing a content block.')

            post_metadata = parse_post_metadata(raw_post_metadata, abs_filename)

            post, created = Post.objects.update_or_create(
                slug=post_metadata['slug'],
                defaults={
                    'author': post_metadata['author'],
                    'title': post_metadata['title'],
                    'markdown_content': post_content,
                },
            )

            if created:
                term = 'Created'
            else:
                term = 'Updated'
            self.stdout.write(f'{term} post {post}')


def parse_post_metadata(raw_post_metadata, abs_filename):
    """Parse and check post metadata values."""

    metadata = {}
    valid_metadata_keys = ['title', 'slug', 'author']
    required_metadata_keys = ['title', 'slug', 'author']
    metadata_separator = ':'

    # Load metadata into dictionary
    metadata_lines = raw_post_metadata.split('\n')
    for line in metadata_lines:
        if metadata_separator in line:
            key, value = line.split(metadata_separator)
            key = key.lower()
            value = value.strip()
            if key in valid_metadata_keys:
                metadata[key] = value

    # Check required keys are present
    for key in required_metadata_keys:
        if key not in metadata:
            raise KeyError(f'ERROR: Post file {abs_filename} is missing metadata for {key}.')

    return metadata
