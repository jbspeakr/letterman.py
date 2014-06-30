# !/usr/bin/env python
# coding: utf-8


class SimpleLetter(object):
    title = ''
    subject = ''
    author = ''
    keywords = []
    creator = ''

    sender = []
    recipient = []
    text = []
    date = ''

    def __init__(self, **kwargs):
        self._init_metadata(kwargs)
        self._init_content(kwargs)

    def _init_metadata(self, **kwargs):
        self.title = kwargs.pop('title', self.title)
        self.subject = kwargs.pop('subject', self.subject)
        self.author = kwargs.pop('author', self.author)
        self.keywords = kwargs.pop('keywords', self.keywords)
        self.creator = kwargs.pop('creator', self.creator)

    def _init_content(self, **kwargs):
        self.sender = kwargs.pop('sender', self.sender)
        self.recipient = kwargs.pop('recipient', self.recipient)
        self.text = kwargs.pop('text', self.content)
        self.date = kwargs.pop('date', self.date)
