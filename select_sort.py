#/usr/bin/env python
__author__ = 'kevin'


def select_sort(array):
    n = len(array)

    for i in range(n):
        m_in = i
        for j in range(i + 1, n):
            if array[j] < array[m_in]:
                m_in = j

        array[m_in], array[i] = array[i], array[m_in]

    return array


if __name__ == "__main__":
    array = [4, 9, 1, 3, 7, 2]
    print '########original: ', array
    print '########after sort: ', select_sort(array)
