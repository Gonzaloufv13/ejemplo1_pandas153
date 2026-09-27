# Ejemplo 1: entorno con pandas 1.5.3 (append)

Une dos tablas de ventas con `DataFrame.append()`, método que solo existe en pandas 1.x. Por eso este proyecto tiene su propio entorno virtual con `pandas==1.5.3` (y `numpy==1.26.4`, ya que pandas 1.5.3 no es compatible con numpy 2).

## Cómo ejecutarlo (Windows, PowerShell en VS Code)

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

En macOS/Linux: `python3 -m venv venv`, `source venv/bin/activate`.

En VS Code: `Ctrl+Shift+P` → **Python: Select Interpreter** → elegir `.\venv\Scripts\python.exe`.

## Resultado

```
  producto  unidades
0        A        10
1        B         5
2        A         7
3        C         3
```
(pandas muestra un `FutureWarning` avisando de que `append` desaparecerá: es lo esperado en esta versión).
