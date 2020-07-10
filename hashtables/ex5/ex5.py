# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    
    dictionary = {}
    
    for f in files:
        f_type = f.split('/')[-1]
        dictionary[f_type] = f
        
    result = []
        
    for query in queries:
        if query in dictionary:
            result.append(dictionary[query])

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
