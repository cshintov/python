'''exercise 6.11 vectorize a function over a list'''

def vectorize(func):
    def vector_func(lst):
        result = []
        for item in lst:
            result.append(func(item))
        return result
    return vector_func

@vectorize
def square(x): return x*x

@vectorize
def double(x): return x+x

if __name__ == "__main__":
    lst = [1,2,3,4]
    print square(lst)
    print double(lst)
