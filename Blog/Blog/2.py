from Blog.stack import Stack
s=Stack(20)
for i in range(3):
    s.push(i)
s.pop()
print(s.isempty())