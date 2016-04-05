#!/usr/bin/python
# coding: utf-8


class AbstractAlbum(object):
    def __init__(self):
        self.pictures = []

    def get_pictures(self):
        return self.pictures

    def remove_picture(self, pic):
        self.pictures.remove(pic)

    def add_picture(self, pic):
        self.pictures.append(pic)


class Album(AbstractAlbum):
    pass


class View(AbstractAlbum):
    pass
