import time

def show_time(func):   # 装饰器函数
    def inner(x, y):      # 闭包函数
        start_time = time.time()
        print(func(x, y))  # 如果原函数中的返回值使用return返回的，在装饰器函数中添加print函数
        end_time = time.time()
        run_time = end_time - start_time
        return run_time

    # this is source function  ,need add some new functions now
    return inner   
@show_time      # 对原函数名进行重新赋值  @show_time = (add = show_time(add))
def add(x, y):   # 原函数
    result = x + y
    time.sleep(3)
    return result

print(add(1, 3))
