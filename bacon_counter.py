from mrjob.job import MRJob

class Bacon_count(MRJob):
    def mapper(self, _, line):
        