from .utility_base import UtilityBase

from instagrapi import Client
from instagrapi.types import Media

from typing import List

import random

class MediaUtility(UtilityBase):
    def __init__(self, session: Client):
        super().__init__(session)
        
        self.ignore_to_skip_if_contains = []
        self.required_hashtags = []
        self.to_skip = []

    def ignore(self, hashtags: List[str]): # ignore skip if caption contains any
        self.ignore_to_skip_if_contains = hashtags

    def require(self, hashtags: List[str]): # only like if all in caption
        self.required_hashtags = hashtags

    def skip(self, hashtags: List[str]): # don't like if any in caption, may still unfollow
        self.to_skip = hashtags

    def validated_for_interaction(self, media: Media) -> bool:
        if all(hashtag in media.caption_text for hashtag in self.required_hashtags):
            if any(hashtag in media.caption_text for hashtag in self.to_skip):
                return any(hashtag in media.caption_text for hashtag in self.ignore_to_skip_if_contains)
            else:
                return True
        else:
            return False
        

    # helper functions for main script
    def medias_location(self, amount: int, location: int, randomize_media: bool, skip_top: bool) -> List[Media]:
        medias = []
        if skip_top:
            medias += [media for media in self.session.location_medias_recent(location_pk=location, amount=amount) if not any(username in media.user.username for username in self.configuration.people.users_to_skip)]
        else:
            medias += [media for media in self.session.location_medias_top(location_pk=location) if not any(username in media.user.username for username in self.configuration.people.users_to_skip)]
            medias += [media for media in self.session.location_medias_recent(location_pk=location, amount=amount - len(medias)) if not any(username in media.user.username for username in self.configuration.people.users_to_skip)]

        if randomize_media:
            random.shuffle(x=medias)

        limited = medias[:amount]

        print(f'[INFO]: Found {len(limited)} of {amount} valid media with the current configuration.')
        return limited


    def medias_tag(self, amount: int, tag: str, randomize_media: bool, skip_top: bool) -> List[Media]:
        medias = []
        if skip_top:
            medias += [media for media in self.session.hashtag_medias_recent(name=tag, amount=amount) if not any(username in media.user.username for username in self.configuration.people.users_to_skip)]
        else:
            medias += [media for media in self.session.hashtag_medias_top(name=tag) if not any(username in media.user.username for username in self.configuration.people.users_to_skip)]
            medias += [media for media in self.session.hashtag_medias_recent(name=tag, amount=amount - len(medias)) if not any(username in media.user.username for username in self.configuration.people.users_to_skip)]

        if randomize_media:
            random.shuffle(x=medias)

        limited = medias[:amount]

        print(f'[INFO]: Found {len(limited)} of {amount} valid media with the current configuration.')
        return limited
    

    def medias_username(self, amount: int, username: str, randomize_media: bool) -> List[Media]:
        try:
            medias = self.session.user_medias(user_id=self.session.user_id_from_username(username=username), amount=amount)
            
            if randomize_media:
                random.shuffle(x=medias)
            
            return medias[:amount]
        except Exception as error:
            print(f'Failed to get media for user: {username}. {error}.')
            return []