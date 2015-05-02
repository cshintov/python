"""

This program is part of an exercise in
Think Python: An Introduction to Software Design
Allen B. Downey

WARNING: this program contains a NASTY bug.  I put
it there on purpose as a debugging exercise, but
you DO NOT want to emulate this example!

"""

class Kangaroo(object):
    """a Kangaroo is a marsupial"""
    
    def __init__(self, contents=None):
        """initialize the pouch contents; the default value is
        an empty list
        The bug was : setting the default value of the contents as a mutable object ,list
        all the new class objects with default content will get the reference to the same list,
        which becomes shared between all those objects
        That is instead of getting the empty list , they get assigned with the already populated shared list
        """
        if contents == None:
          contents = []
        self.pouch_contents = [contents]

    def __str__(self):
        string = repr(self)+'with contents\n'
        for item in self.pouch_contents:
            string += repr(item)+'\n' 
        return string.strip('\n')
    def put_in_pouch(self, item):
        """add a new item to the pouch contents"""
        self.pouch_contents.append(item)

kanga = Kangaroo()
roo = Kangaroo()
kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
kanga.put_in_pouch(roo)

print kanga
print 
print roo
'''
If you run this program as is, it seems to work.
To see the problem, try printing roo. prints the same content
After fixing the bug with the if construct in init
they print the correct contents
'''
