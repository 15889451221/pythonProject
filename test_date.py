
def test_date():
    x = [1,2,3,4]
    y = [1,2]
    for i in x:
        for j in y:
            if x[i-1]==y[j-1]:
                x[i-1]=""
                break
    print(x)