d = {'小李':90,'小张':85,'小易':60}
print(d['小易'])
print(d['小李'])
print(d['小张'])
d['学霸'] = 100
d['学渣'] = 50
print(d['学霸'])
#判断key是否在当前map里
print('学霸' in d)
print(d.get('qqq'))
print(d)
#删除一个 key
d.pop('学渣')
print(d)
#set
s =set([1,2,3])
print(s)
#重复元素会被过滤
s =set([1,2,3,3,2,5,1])
print(s)
#添加
s.add(6)
print(s)
#删除
s.remove(6)
print(s)
#交集& 并集|
s1= set([1,2,3,4])
s2= set([2,3,4,5])
print(s1 & s2)
print(s1 | s2)