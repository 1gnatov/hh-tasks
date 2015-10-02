def memoize_sorted(f):
    cache = {}
    def decorated_function(*args):
    	args = tuple(sorted(args))
    	#print(args)
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorated_function

#@memoize_sorted