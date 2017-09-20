#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import json
import sys
import getopt


def dlfile(url, count):
    localpath = "image-download/%d" % (count)
    urllib.urlretrieve(url, localpath)


def getData(tokenId):
    urls = []
    currentPageIndex = 1
    limit = 20
    while 1:
        url = (
            "https://api.disneyphotopass.com.cn/p/getPhotosByConditions?tokenId=%s&currentPageIndex=%d&limit=%d&sortField=shootOn&order=-1" % (
                tokenId, currentPageIndex, limit))
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        if not data:
            break

        result = data["result"]
        if not result:
            break

        photos = result["photos"]
        if not photos:
            break

        print "Page: %d, count: %d" % (currentPageIndex, len(photos))
        if len(photos) == 0:
            break

        currentPageIndex = currentPageIndex + 1
        for x in xrange(0, len(photos)):
            photo = photos[x]
            if photo["enImage"]:
                thumbnail = photo["thumbnail"]
                en1024 = thumbnail["en1024"]
                url = en1024["url"]
                if not url:
                    continue
                urls.append("http://www.disneyphotopass.com.cn:4000/" + url)

    return urls


def main(argv):
    tokenId = ""
    try:
        opts, args = getopt.getopt(argv, "ht:", ["tokenId="])
    except getopt.GetoptError:
        print 'export.py -t <tokenId>'
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print 'export.py -t <tokenId>'
            sys.exit()
        elif opt in ("-t", "--tokenId"):
            tokenId = arg

    if not tokenId:
        print "tokenId must not empty!"
        sys.exit()

    print "tokenId: %s" % (tokenId)
    # Get urls
    urls = getData(tokenId)
    if not urls:
        return
    if len(urls) == 0:
        return

    # Download
    print "need download %d photos" % (len(urls))
    for x in xrange(0, len(urls)):
        print "downloading... %d" % (x + 1)
        dlfile(urls[x], x + 1)

    print 'download done.'

    # Analysis
    for x in xrange(0, len(urls)):
        print "analysis... %d" % (x + 1)
        path = "image-download/%d" % (x + 1)
        with open(path, 'rb') as f:
            orihex = f.read(1024000).encode('hex')
            try:
                newhex = orihex.split('ffd9ffd8')[1]
                newhex = 'ffd8' + newhex
                newjpg = newhex.decode('hex')
                path_out = "image/%d" % (x + 1) + ".jpg"
                with open(path_out, 'wb') as w:
                    w.write(newjpg)
            except IndexError:
                print 'It seems not to find ffd9ffd8.'

    print 'All Done.'


if __name__ == '__main__':
    main(sys.argv[1:])