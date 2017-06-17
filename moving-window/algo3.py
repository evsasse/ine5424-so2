def algo3(values, window_size, alpha=0.5):
    window = []
    avgs = []

    for value in values:
        window = avgs[-(window_size-1):]

        window_avg = sum(window) / max(1, len(window))
        
        avgs.append(window_avg*(1-alpha) + value*alpha)


    return avgs