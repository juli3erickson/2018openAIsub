def extract(query):
    """extract takes in a `query` API function (which returns the first 5 usernames, lexicographically sorted,
    that start with a prefix) and returns the sorted list of all usernames in the database.
    For example, the `query` function in provided in `main` works as follows:

    query("a") #=> ["abracadara", "al", "alice", "alicia", "allen"]
    query("ab") #=> ["abracadara"]
    The following implementation would pass the assertion in `main`, but is not a correct solution since it
    works only for that example `query`:
    def extract(query):
        return query("ab") + query("al") + query("altercation") + query("b") + query("el") + query("ev") + query("m")
    Your goal is to write an `extract` method that is correct for any provided `query`.
    """
    # YOUR CODE HERE
    i = 1 #Keeps the while loop on until criteria is met to exit loop
    j = 0 #Counter
    k = 0 #Counter
    alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] #Alphabet
    delta = alpha[j]  # Placeholder for iterated string to search in query
    beta = query(delta) #Initial value for iteration
    gamma = [] #Placeholder for building the database
    epsilon = str()
    zeta = str()
    eta = str()
    theta = str()
    while i == 1:
        if not beta:
            j = alpha.index(delta[-1])
            delta[-1] = alpha[j+1]
            beta = query(delta)
        elif len(beta) < 5:
            gamma.append(beta)
            j = alpha.index(delta[-1])
            delta[-1] = alpha[(j+1)]
            beta = query(delta)
        else:
            gamma.append(beta)
            print(gamma)
            epsilon = beta[-1]
            zeta = beta[-2]
            eta = list(set([c for c in epsilon if c in zeta]))
            delta = epsilon[(len(eta)+1)]
            beta = query(str(delta))

    return [gamma]

def main():
    """Runs your solution -- no need to update (except to maybe try out different databases)."""
    # Sample implementation of the autocomplete API
    database = ["abracadara", "al", "alice", "alicia", "allen", "alter", "altercation", "bob", "element", "ello", "eve",
                "evening", "event", "eventually", "mallory"]
    query = lambda prefix: [d for d in database if d.startswith(prefix)][:5]
    assert extract(query) == database

main()