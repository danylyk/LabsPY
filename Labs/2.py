import html

def Wrapper (fun):
    def wrapper (a):
        a = html.escape(a)
        fun(a)
    return wrapper


@Wrapper
def Lab3 (a):
    print(a)

Lab3("<h1>Hello world!</h1>")