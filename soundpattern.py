from scipy.io.wavfile import read

file = "13_55.wav"

file2 = "Dog2.wav"

def calc_distances(file):

    min_val = 5000
    
    fs, data = read(file)
    data_size = len(data)
    
    focus_size = int(0.15 * fs)
    
    focuses = []
    distances = []
    idx = 0
    
    while idx < len(data):
        if data[idx] > min_val:
            mean_idx = idx + focus_size // 2
            focuses.append(float(mean_idx) / data_size)
            if len(focuses) > 1:
                last_focus = focuses[-2]
                actual_focus = focuses[-1]
                distances.append(actual_focus - last_focus)
            idx += focus_size
        else:
            idx += 1
    return distances

def calc_distances2(file2):

    min_val = 5000
    
    fs, data = read(file2)
    data_size = len(data)
    
  
    focus_size = int(0.15 * fs)
    
    focuses = []
    distances = []
    idx = 0
    
    while idx < len(data):
        if data[idx] > min_val:
            mean_idx = idx + focus_size // 2
            focuses.append(float(mean_idx) / data_size)
            if len(focuses) > 1:
                last_focus = focuses[-2]
                actual_focus = focuses[-1]
                distances.append(actual_focus - last_focus)
            idx += focus_size
        else:
            idx += 1
    return distances



    
if __name__=="__main__":

    calc_distances(file)
    calc_distances2(file2)

    a = float(sum(calc_distances(file)))

    b = float(sum(calc_distances(file2)))

    print(a)

    print(b)

    dif = a - b

    if -1 < dif < 1:
        print("less go")

    else:
        print("not less go")




    
    