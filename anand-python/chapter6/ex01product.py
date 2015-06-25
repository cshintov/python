'''exercise 6.1 implement product by recursive addition'''
import sys
def product(a,b):
    min_num = min(a,b)
    max_num = max(a,b)
    if min_num == 0:
        return 0
    return max_num + product(max_num,min_num-1)

if __name__ == '__main__':
    print 'usage: python ex01product.py num_a num_b'
    print product(int(sys.argv[1]),int(sys.argv[2]))
