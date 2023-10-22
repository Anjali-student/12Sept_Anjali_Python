d1={"Name":"Anjali" , "Rollno.":23}
d2={"City": "Rajkot", "Gender": "Female"}
d3={"Mark":450}
d4 = {}
for d in (d1, d2, d3): d4.update(d)
print(d4)