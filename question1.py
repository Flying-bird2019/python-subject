a=input()
b=input()
print(int(a)+int(b))


j=int(input())
k=int(input())
l=int(input())
print(2*(j*k+k*l+j*l),"\n",j*k*l)


a=9/4
b=9//4
c=9%4
print(a,b,c)


print("=================================="+"\n"+
    "=        欢迎进入到身份认证系统V1.0")
print("= 1. 登录"+"\n"+"= 2. 退出"+"\n"+"= 3. 认证"+"\n"+"= 4. 修改密码")
print(" ==================================")



print("请依次输入姓名、QQ、手机号，学校地址")
name=input()
QQ=input()
phone=input()
address=input()
print("姓名："+name)
print("QQ："+QQ)
print("手机号"+phone)
print("学校地址"+address)


name="liuhao"
key="666"
inname=input()
inkey=input()
if name!=inname or inkey!=key:
    print("密码或者用户名错误")
else:
    print("欢迎登陆"+name)


print("请输入三个字符串")
list=[]
a=input()
list.append(a)
b=input()
list.append(b)
c=input()
list.append(c)
print(list)



print("请依次输入姓名、性别、年龄")
a = {
    'name': "" ,
    'sex': "" ,
    'age': "" ,
    }
a['name']=input()
a['sex']=input()
a['age']=input()
print(a)



import time
time_format = '%Y-%m-%d %X'
print(time.strftime(time_format, time.localtime()))
