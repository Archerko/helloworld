# -*- coding: utf-8 -*-
# Filename:classChain.py


class Chain(object):
    def __init__(self, path=''):
        self.path = path

    def __getattr__(self, item):
        return Chain('%s/%s' % (self.path, item))

    def __str__(self):
        return self.path

print Chain().www.jjj.kkk
print '----------------------------------------------------'


class GitChain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, item):
        return GitChain('%s/%s' % (self._path, item))

    def __str__(self):
        return self._path

    __repr__ = __str__

    def users(self, username):
        return GitChain(self._path + '/users/' + username)

print GitChain().status.user.timeline.list  # /status/user/timeline/list
print GitChain().users('devin').repos   # /users/devin/repos
print GitChain().data.users('devin').repos   # /data/users/devin/repos



