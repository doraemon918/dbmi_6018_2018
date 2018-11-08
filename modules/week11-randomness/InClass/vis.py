"""
Functions and classes for visualization
"""
class styleIterator(object):
    def __init__(self, styles):
        self.index = 0
        self.styles = styles
        self.nstyles = len(styles)
        
    def nextStyle(self):
        result = self.styles[self.index % self.nstyles]
        self.index += 1
        return result