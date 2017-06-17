def algo1(values, window_size):
    window = []
    avgs = []

    for value in values:
        window.append(value)

        if len(window) > window_size:
            window.pop(0)
        
        avgs.append(sum(window) / len(window))


    return avgs