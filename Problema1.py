{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMo6EQtPmQ+9koORrNXOiED",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/IronGhost2007/Carpeta-Semana1---Jorge-Antonio-Galv-n-Segovia-1999636/blob/main/Problema1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9B14l3RhiZ9Z",
        "outputId": "6588a309-5540-429d-cde5-f315b346e807"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Ingrese el primer número entero: fes\n",
            "Error: Ingrese solo números enteros.\n"
          ]
        }
      ],
      "source": [
        "def operaciones_basicas():\n",
        "    try:\n",
        "        # Solicitar entrada de dos números enteros\n",
        "        num1 = int(input(\"Ingrese el primer número entero: \"))\n",
        "        num2 = int(input(\"Ingrese el segundo número entero: \"))\n",
        "\n",
        "        # Realizar operaciones\n",
        "        suma = num1 + num2\n",
        "        resta = num1 - num2\n",
        "        multiplicacion = num1 * num2\n",
        "\n",
        "        # Manejo de división por cero\n",
        "        if num2 != 0:\n",
        "            division = num1 / num2\n",
        "            division_piso = num1 // num2\n",
        "            residuo = num1 % num2\n",
        "        else:\n",
        "            division = \"Indefinida (división por cero)\"\n",
        "            division_piso = \"Indefinida (división por cero)\"\n",
        "            residuo = \"Indefinido (división por cero)\"\n",
        "\n",
        "        # Mostrar resultados\n",
        "        print(f\"Suma: {suma}\")\n",
        "        print(f\"Resta: {resta}\")\n",
        "        print(f\"Multiplicación: {multiplicacion}\")\n",
        "        print(f\"División: {division}\")\n",
        "        print(f\"División de piso: {division_piso}\")\n",
        "        print(f\"Residuo: {residuo}\")\n",
        "\n",
        "    except ValueError:\n",
        "        print(\"Error: Ingrese solo números enteros.\")\n",
        "\n",
        "# Ejecutar la función\n",
        "operaciones_basicas()\n",
        "\n"
      ]
    }
  ]
}