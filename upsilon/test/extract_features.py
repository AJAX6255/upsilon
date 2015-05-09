__author__ = 'kim'

import time

from upsilon.extract_features.extract_features import ExtractFeatures
from upsilon.datasets.base import load_EROS_lc
from upsilon.utils.utils import sigma_clipping_without_error
from upsilon.utils.utils import sigma_clipping


def run():
    """
    Test UPSILoN package.

    :return: None
    """

    date, mag, err = load_EROS_lc()

    index = mag < 99.999
    date = date[index]
    mag = mag[index]
    err = err[index]

    print '# Before sigma-clipping: %d data points' % len(date)
    #date, mag, err = sigma_clipping_without_error(date, mag)
    date, mag, err = sigma_clipping(date, mag, err)
    print '# After sigma-clipping: %d data points' % len(date)

    for i in range(1):
        print '-----------------------------------------------'
        start = time.time()
        e_features = ExtractFeatures(date, mag, err)
        end = time.time()
        print '# Initializing time: %.4f seconds.' % (end - start)

        start = time.time()
        e_features.shallow_run()
        end = time.time()
        print '# Shallow-run processing time: %.4f seconds.' % (end - start)

        start = time.time()
        e_features.deep_run()
        end = time.time()
        print '# Deep-run processing time: %.4f seconds.' % (end - start)

    print '-----------------------------------------------'
    print '# Extracted features:'
    features = e_features.get_features()
    print features
    for key, value in features.iteritems():
        print ' %s: %f' % (key, value)

    print '----------------------------------------------'
    print '# Finished.'

if __name__ == '__main__':
    run()