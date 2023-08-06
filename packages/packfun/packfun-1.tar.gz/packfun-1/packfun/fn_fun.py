import math

__all__ = ['f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', 'f13']


def f5(k):
    fn = math.cos(math.fabs(2 * k)) / 1.12 - math.cos(3 * k - 2) + 6.15
    return fn


def f6(k):
    fn = math.sin(k) * math.cos(pow(k, 2)) * math.sin(k + 1.4) + 5.14
    return fn


def f7(k):
    fn = math.fabs(math.sin(2 * k - 1.5) + 3 * math.sin(pow(k, 2))) + 2.38
    return fn  # for task_3


def f8(k):
    fn = math.cos(pow(k, 2)) * math.sin(2 * k - 1) + 4.29
    return fn


def f9(k):
    fn = math.cos(pow(k, 2) + 1) - math.fabs(math.sin(2 * k) - 5.76)
    return fn  # for task_6


def f10(k):
    fn = math.sin(k) - math.cos(pow(k, 3)) * math.sin(pow(k, 2) - 4.2) + 4.27
    return fn  # for task_7


def f11(k):
    fn = math.fabs(math.sin(12 * k) * math.cos(math.fabs(2 * k)) / 3) + 4.21
    return fn  # for task_8


def f12(k):
    fn = math.cos(pow(k, 3)) / 2.1 + math.cos(pow(k, 2)) / 1.1 - 8.3 * math.sin(3 * k + 1)
    return fn  # for task_9


def f13(k):
    fn = math.sin(pow(k, 2)) * math.cos(pow(k, 3)) - math.sin(k) + 5.2
    return fn  # for task_10
