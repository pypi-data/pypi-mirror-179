# coding: utf8
# https://blog.csdn.net/qq_45797116/article/details/123609056
from multiprocessing.dummy import Pool


def multi_pro(thread_num, func, param_list, is_ret=False):
    """
    多线程

    Parameters
    ----------
    :param thread_num: 线程数
    :param func: 循环数
    :param param_list: 参数
    :param is_ret: 是否返回最终结果

    Examples
    --------
    >>> def func(num):
    >>>     # 平方函数
    >>>     return num * num

    >>> param_list = [0, 1, 2]
    >>> res = multi_pro(3, func, param_list)
    >>> print(f'计算1-10的平方分别为：{res}')

    """
    # 定义n个线程池
    pool = Pool(thread_num)
    # 利用map让线程池中的所有线程‘同时’执行func函数
    result = pool.map(func, param_list)
    if is_ret:
        return result
