import feedparser
import os
import unidecode
import wx
import wx.html2 as webview

from ObjectListView import ObjectListView, ColumnDefn


class Rss(object):
    def __init__(self, title, link, website, summary, all_data):
        self.title = title
        self.link = link
        self.all_data = all_data
        self.website = website
        self.summary = summary
