import cgi

class Problem:
    def __init__(self,intro,test):
        self.intro=intro
        self.test =test

problems = {}
problems[1] = Problem(intro='Write a function fact(n) that calculates the factorial of n.',test= """
def f(n):
  if (n == 0): return 1
  else: return n * f(n-1)
for i in range(10):
  assert(fact(i) == f(i))
""")

problems[2] = Problem(intro="""Write a function that solves <a href=http://stackoverflow.com/questions/1480023/code-golf-lasers> Code Golf: Lasers </a> when given the maze as its single argument. Sample testcase:
<pre>
assert(laser(r""\"
##########
#   / \  #
#        #
#   \   x#
# >   /  #
########## 
""\") == True)
</pre>
""", test=r''' 
def laser2(b):
    l='>v<^';x={'/':'^<v>','\\':'v>^<',' ':l};r=p=0
    b=b.split('\n')
    b[0]=1
    for row in b[1:]:
        r+=1
        for g in l:
            c=row.find(g)
            if-1<c:p=c+1j*r;d=g
    while' '<d:z=l.find(d);p+=1j**z;c=b[int(p.imag)][int(p.real)];d=x.get(c,' '*4)[z]
    return '#'<c
assert(laser(r"""
##########
#   / \  #
#        #
#   \   x#
# >   /  #
########## 
"""))
assert(not(laser(r"""
##########
#   v x  #
# /      #
#       /#
#   \    #
##########
""")))
assert(not(laser(r"""
#############
#     #     #
# >   #     #
#     #     #
#     #   x #
#     #     #
#############
""")))
assert(laser(r"""
##########
#/\/\/\  #
#\\//\\\ #
#//\/\/\\#
#\/\/\/x^#
##########
"""))
''')
"""
def laser(b):
    l='>v<^';x={'/':'^<v>','\\':'v>^<',' ':l};r=p=0
    b=b.split('\n')
    b[0]=1
    for row in b[1:]:
        r+=1
        for g in l:
            c=row.find(g)
            if-1<c:p=c+1j*r;d=g
    while' '<d:z=l.find(d);p+=1j**z;c=b[int(p.imag)][int(p.real)];d=x.get(c,' '*4)[z]
    return '#'<c
"""