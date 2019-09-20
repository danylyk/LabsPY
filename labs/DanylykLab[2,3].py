def Wrapper (fun):
    def wrapper (*args, **kwargs):
        print("------SSA------")
        print(fun(*args, **kwargs))
        print("---------------")
    return wrapper


@Wrapper
def Lab3 (data, options):
    for k, i in options.items():
        data = data.replace(k, i)
    return data

options = {"%": "&exp;", "#": "&hash;"}
v = "Hello %%world##"
print(v + "\n")
Lab3(v, options)