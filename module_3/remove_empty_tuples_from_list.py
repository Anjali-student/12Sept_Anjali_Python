def rem_fun(tup1):
    for i in tup1:
        if len(i) == 0:
            tup1.remove(i)
    return tup1


tuples = [(), ('A', 'B', 'C'), (), ('1', '2'),
          ('gondal', 'Rajkot', 'Jamnagar'), ('', ''), ()]
print(rem_fun(tuples))