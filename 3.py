def Html (tag):
    def Wrapper (fun):
        def wrapper (a):
            return "<" + tag + ">" + fun(a) + "</" + tag + ">"
        return wrapper
    return Wrapper


@Html("div")
@Html("h1")
def Lab3 (a):
    return a

print(Lab3("Hello world!"))