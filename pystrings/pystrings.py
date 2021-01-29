class create_strings():
    def __init__(self, *args):
        for i in args:
           for j in i:
                j = str(j)
                exec ('%s = %s' % (j, 'j'))
                exec ('self.%s = %s' % (j, j))
