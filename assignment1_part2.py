#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Classes"""


class Book(Exception):
    author = ""
    title = ""


    def __init__(self, author, title):
        self.author = author
        self.title = title




def display(Book):
    return "{}, written by {}.".format(title, author)


display("Of Mice And Men", "John Steinbeck")
display("To Kill a Mockingbird", "Harper Lee")



