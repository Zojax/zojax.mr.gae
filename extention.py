import logging
from nevow.livepage import self
import os
import re
import sys
import urllib2
from zipfile import *



class Extension(object):
    def __init__(self, buildout):
        self.buildout = buildout
        self.buildout_dir = buildout['buildout']['directory']


    def download_package(self):
        url = self.buildout['gae_source']['url']
        path_to_save = self.buildout_dir
        filename = url.split('/')[-1]

        remotefile = urllib2.urlopen(url)
        #print remotefile.info()['Content-Disposition']
        localFile = open(path_to_save + filename, 'w')
        print 'Downloading file ' + filename
        localFile.write(remotefile.read())
        localFile.close()
        print 'Download complete'
        return path_to_save + url.split('/')[-1]

    def extract_package(self):
        if is_zipfile(archive):
            print 'Start extracting %s to %s/parts' % archive
            zip_file = ZipFile(archive)
            zip_file.extractall(self.buildout_dir + '/parts')
        else:
            print "File %s is not zip" % archive

    def create_symbolic_links(self):
        source = self.buildout_dir + '/parts/google_appengine/lib'
        link_dir = self.buildout_dir + 'src/'
        print "create links"
        for root, dirs, files in os.walk(self.buildout_dir + '/parts/google_appengine/lib'):
            for dir in dirs:
                if not os.path.exists(link_dir):
                    if not os.path.islink(dst_dir + dir):
                        print "link to " + self.buildout_dir +  dir
                        os.symlink(source + dir, link_dir + dir)
                    else:
                        print '%s is already exist' %(link_dir + dir)
            break


    def __call__(self):
        self.download_package()
        self.extract_package()
        self.create_symbolic_links()

def extension(buildout=None):
    return Extension(buildout)()
