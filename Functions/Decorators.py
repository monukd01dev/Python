#decorators functon is like HOC -> higher Order component type thing in python which is an application of closure

def knowShiva (shiv):
    # closure environtment
    def wrapper() : #wrapper is important
        print("AADI")
        shiv()
        print("ANANTA")
    return wrapper # and returning is wrapper is also important why u are lacking in it sucks!

@knowShiva # shiv = knowShiva(shiv) # but please define shiv first
def shiv():
    print(" SHIVA!")

shiv()