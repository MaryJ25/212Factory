{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Tesla Factory",
      "provenance": [],
      "authorship_tag": "ABX9TyOBccxY9xwfkr1OTBz7UQWh",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
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
        "<a href=\"https://colab.research.google.com/github/MaryJ25/212Factory/blob/main/Tesla_Factory.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "aObrlZu_6mHX"
      },
      "source": [
        "class Tesla:\r\n",
        "    # WRITE YOUR CODE HERE\r\n",
        "    def __init__(self, model: str, color: str, autopilot: bool = False, efficiency: float = 0.3):\r\n",
        "        self.__autopilot = autopilot\r\n",
        "        self.__model = model\r\n",
        "        self.__battery_charge = 99.9\r\n",
        "        self.__is_locked = True\r\n",
        "        self.__seats_count = 5\r\n",
        "        self.__color = color\r\n",
        "        self.__efficiency = efficiency\r\n",
        "        \r\n",
        "    @property\r\n",
        "    def color(self) -> str:\r\n",
        "        return self.__color\r\n",
        "\r\n",
        "    @property\r\n",
        "    def seats_count(self) -> str:\r\n",
        "        return self.__seats_count\r\n",
        "        \r\n",
        "    def welcome(self) -> str:\r\n",
        "        raise NotImplementedError\r\n",
        "\r\n",
        "    def autopilot(self, obstacle: str) -> str:\r\n",
        "      if self.__autopilot:\r\n",
        "        return f\"Tesla model {self.__model} avoids {obstacle}\"\r\n",
        "      return \"Autopilot is not available\"\r\n",
        "\r\n",
        "    def open_doors(self) -> str:\r\n",
        "      if self.__is_locked:\r\n",
        "        return \"Car is locked!\"\r\n",
        "      return \"Doors open sideways\"\r\n",
        "\r\n",
        "    def unlock(self) -> str:\r\n",
        "      self.__is_locked = False\r\n",
        "\r\n",
        "    @seats_count.setter\r\n",
        "    def seats_count(self, new_seats_count: str) -> None:\r\n",
        "        self.__seats_count = new_seats_count\r\n",
        "\r\n",
        "    @property\r\n",
        "    def check_battery_level(self) -> str:\r\n",
        "      return f\"Battery charge level is {self.__battery_charge}%\"\r\n",
        "\r\n",
        "    def charge_battery(self):\r\n",
        "      self.__battery_charge = 100\r\n",
        "\r\n",
        "    def drive(self, travel_range: float):\r\n",
        "      battery_discharge_percent = travel_range * self.__efficiency\r\n",
        "      if self.__battery_charge - battery_discharge_percent >= 0:\r\n",
        "        self.__battery_charge = self.__battery_charge - battery_discharge_percent\r\n",
        "        return self.check_battery_level\r\n",
        "      else:\r\n",
        "        return  \"Battery charge level is 0%, please charge!\""
      ],
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "q83vJ5-uEtoq"
      },
      "source": [
        "tesla = Tesla(\"S\", \"black\")"
      ],
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "D3rslNpV6wKG"
      },
      "source": [
        "class ModelX(Tesla):\r\n",
        "  def __init__(self, color: str, autopilot: bool = False):\r\n",
        "    super().__init__(\"X\", color, autopilot, 0.125)\r\n",
        "\r\n",
        "  def open_doors(self):\r\n",
        "    return \"Doors open towards the roof\"\r\n",
        "\r\n",
        "  def welcome(self) -> str:\r\n",
        "    return \"Hello from ModelX!\""
      ],
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hZ315kYFGF0H"
      },
      "source": [
        "modelx = ModelX(\"black\")\r\n",
        "modelx.unlock()\r\n",
        "assert modelx.open_doors() == \"Doors open towards the roof\""
      ],
      "execution_count": 6,
      "outputs": []
    }
  ]
}
