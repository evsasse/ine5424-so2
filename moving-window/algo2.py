def algo2(values, window_size):
    window = []
    avgs = []

    for value in values:
        window = avgs[-(window_size-1):]
        window.append(value)
        
        avgs.append(sum(window) / len(window))


    return avgs