import h5py
import matplotlib.pyplot as plt

def graficar_hd5(nombre_archivo):
    """
    Lee los datasets 'x', 'y' y 'e' de un archivo HDF5
    y grafica y(x) con barras de error.
    """

    with h5py.File(nombre_archivo, "r") as archivo:

        # Verificar que existan los datasets necesarios
        for dataset in ["x", "y", "e"]:
            if dataset not in archivo:
                raise KeyError(
                    f"El archivo no contiene el dataset '{dataset}'."
                )

        # Leer los datasets como arreglos
        x = archivo["x"][:]
        y = archivo["y"][:]
        e = archivo["e"][:]

    # Comprobar que tengan la misma longitud
    if not (len(x) == len(y) == len(e)):
        raise ValueError(
            "Los datasets 'x', 'y' y 'e' deben tener la misma longitud."
        )

    # Comprobar que las incertidumbres no sean negativas
    if (e < 0).any():
        raise ValueError("Las barras de error no pueden ser negativas.")

    # Crear el gráfico
    plt.figure(figsize=(9, 6))

    plt.errorbar(
        x,
        y,
        yerr=e,
        fmt="o",
        color="blue",
        ecolor="red",
        capsize=5,
        elinewidth=1.5,
        label="Datos con incertidumbre"
    )

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Resultados experimentales")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()
graficar_hd5("resultados_ejemplo.hd5")