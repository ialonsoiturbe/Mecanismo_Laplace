# IBM diffprivlib
from diffprivlib.mechanisms import Laplace

ibm = Laplace(
    epsilon=0.5,
    sensitivity=1.0
)

resultado_ibm = ibm.randomise(200)


# OpenDP
import opendp.prelude as dp

dp.enable_features("contrib")

espacio = (
    dp.atom_domain(T=float, nan=False),
    dp.absolute_distance(T=float)
)

opendp = dp.m.make_laplace(
    *espacio,
    scale=2.0
)

resultado_opendp = opendp(200.0)
epsilon = opendp.map(d_in=1.0)


# Resultados
print("Resultado original:", 200)
print("IBM diffprivlib:", resultado_ibm)
print("OpenDP:", resultado_opendp)
print("Epsilon de OpenDP:", epsilon)

############################################################

# casos distintos niveles de privacidad
import numpy as np

def mecanismo_laplace(valor, sensibilidad, epsilon):
    escala = sensibilidad / epsilon
    ruido = np.random.laplace(0, escala)
    return valor + ruido

# el resultado real de una consulta estadística antes de añadir ruido:
conteo_real = 200

for epsilon in [0.1, 0.5, 1, 2]:
    resultado = mecanismo_laplace(
        conteo_real,
        sensibilidad=1,
        epsilon=epsilon
    )
    print(f"ε={epsilon}: {resultado:.2f}")

