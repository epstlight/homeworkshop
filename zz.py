blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'A', 'B', 'O', 'B', 'AB']
blood = {}

for blood_type in blood_types:
    if blood_type in blood:
        blood[blood_type] += 1
    else : 
        blood[blood_type] = 1
       

print(blood)