def range_check(param, param_name, begin, end):
    try:
        if (param in range(begin, end)) == False:
            raise ValueError('Parameter {} is over range of num.'.format(param_name))
    except ValueError as e:
        print("ValueError : {}".format(e))

range_check(8, 'test', 0, 9)
