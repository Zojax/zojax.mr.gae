import os
import urllib2
from zipfile import *


class Extension(object):
    def __init__(self, buildout):
        self.buildout = buildout
        self.buildout_dir = buildout['buildout']['directory']
        self.buildout_parts_dir = buildout['buildout']['parts-directory']
        self.url = self.buildout['gae_source']['url']
        self.packages = self.buildout['gae_source']['eggs'].split()
        self.extraxt_dir = self.buildout['gae_source']['extraxt_dir']
        if not self.extraxt_dir[0] == '/':
            self.extraxt_dir = os.path.join(self.buildout_dir, self.extraxt_dir)

    def download_package(self):
        filename = self.url.split('/')[-1]
        path_to_file = os.path.join(self.buildout_dir, 'downloads', filename)
        try:
            localFile =open(path_to_file, 'r')
            return localFile
        except IOError as e:
            remotefile = urllib2.urlopen(self.url)
            #print remotefile.info()['Content-Disposition']
            if not os.path.exists(os.path.join(self.buildout_dir, 'downloads')):
                os.makedirs(os.path.join(self.buildout_dir, 'downloads'))
            localFile = open(path_to_file, 'wb')
            print 'Downloading file %s to %s' % (filename, os.path.join(self.buildout_dir, 'downloads', filename))
            localFile.write(remotefile.read())
            localFile.close()
            print 'Download complete'
            return self.download_package()

    def extract_package(self, archive):
        if is_zipfile(archive):
            print 'Start extracting %s to %s/parts' % (archive.name, os.path.join(self.buildout_dir, 'parts'))
            zip_file = ZipFile(archive)
            zip_file.extractall(os.path.join(self.buildout_dir, 'parts'))
        else:
            print "File %s is not zip" % archive.name

    def chenge_develop_cection(self):
        for package in self.packages:
            path = os.path.join(self.buildout_dir, 'parts/google_appengine/lib', package)
            if os.path.exists(path):
                self.buildout['buildout']['develop'] += '\n' + path
            else:
                print "Package %s is not found." % package


    def __call__(self):
        if not os.path.exists(os.path.join(self.extraxt_dir, 'google_appengine')):
            gae_archive = self.download_package()
            self.extract_package(gae_archive)
            self.chenge_develop_cection()
        else:
            print 'GAE is currently downloaded'

def extension(buildout=None):
    return Extension(buildout)()
