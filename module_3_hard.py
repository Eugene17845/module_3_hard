def calculate_structure_sum(data_structure):
    kolwo = 0
    if isinstance (data_structure, dict):
        for a, b in data_structure.items():
            kolwo += calculate_structure_sum(a)
            kolwo += calculate_structure_sum(b)
    elif isinstance(data_structure, (list, tuple, set)):
        for i in data_structure:
            kolwo += calculate_structure_sum(i)
    elif isinstance(data_structure, (int, float)):
        kolwo += data_structure
    elif isinstance(data_structure, str):
        kolwo += len(data_structure)
    return kolwo


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)