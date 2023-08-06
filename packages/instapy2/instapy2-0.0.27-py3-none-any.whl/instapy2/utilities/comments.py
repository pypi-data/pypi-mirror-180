from .utility_base import UtilityBase

from instagrapi import Client
from instagrapi.types import Media

from typing import List, Tuple

class CommentsUtility(UtilityBase):
    def __init__(self, session: Client):
        super().__init__(session)

        self.comments = []
        self.enabled = False
        self.enabled_for_liked_media = False
        self.percentage = 0

    def set_comments(self, comments: List[str]):
        """
            Sets the comments to be used when commenting on media.

            :param comments: comments=['comment 1', ' comment 2', ' comment 3 {}']
            
            Adding {} will tag the user of the media.
        """
        self.comments = comments

    def set_enabled(self, enabled: bool):
        """
            Enables the ability to comment on media.

            :param enabled: enabled=True means media will be commented on.
        """
        self.enabled = enabled

    def set_enabled_for_liked_media(self, enabled: bool):
        """
            Enabled the ability to comment on liked media.

            :param enabled: enabled=True means media that is liked will be commented on.
        """
        self.enabled_for_liked_media = enabled

    def set_percentage(self, percentage: int):
        """
            Set the percentage of media to be commented on.

            :param percentage: percentage=25 means every 4th media is to be commented on.
        """
        self.percentage = percentage


    def comment(self, media: Media, text: str) -> Tuple[Exception, bool]:
        try:
            commented = self.session.media_comment(media_id=media.id, text=text.format(media.user.username))
            return (None, commented is not None)
        except Exception as error:
            return (error, False)