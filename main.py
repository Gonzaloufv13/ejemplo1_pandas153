import pandas as pd

ventas_enero = pd.DataFrame({"producto": ["A", "B"], "unidades": [10, 5]})
ventas_febrero = pd.DataFrame({"producto": ["A", "C"], "unidades": [7, 3]})

ventas_totales = ventas_enero.append(ventas_febrero, ignore_index=True)
print(ventas_totales)
