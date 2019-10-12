def Wraps (fun):
  def Wrapper (fn):
    fn.__name__ = fun.__name__
    fn.__doc__ = fun.__doc__
    return fn
  return Wrapper

def Wrapper (fun):
  @Wraps(fun)
  def wrapper (a):
    fun(a)
  return wrapper

@Wrapper
def Lab3 (a):
  """I am here"""
  pass

print(Lab3.__name__)
print(Lab3.__doc__)