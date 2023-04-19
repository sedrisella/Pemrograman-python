{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM5P16+tIjHsy4dKkJjzxih",
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
        "<a href=\"https://colab.research.google.com/github/sedrisella/Pemrograman-python/blob/main/Task%207%20Modul%2010.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#TASK 7 MODUL 10"
      ],
      "metadata": {
        "id": "PmgUoRCngITN"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "##Machine Learning : Prediksi Pembeli Asuransi dengan Regresi Logistik\n",
        "\n",
        "\n",
        "####Perbedaan Kegunaan Metode Regresi Linear dan Regresi Logistik\n",
        "\n"
      ],
      "metadata": {
        "id": "IpkfuxwigByq"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "\n",
        "\n",
        "\n",
        "> Perbedaan utama antara regresi linear dan regresi logistik adalah pada jenis variabel dependen dan tujuan penggunaannya. Regresi linear digunakan untuk memprediksi nilai variabel dependen yang bersifat kontinu, sedangkan regresi logistik digunakan untuk memprediksi nilai variabel dependen yang bersifat biner.\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "ldMHS8BLgutb"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "uIHaAJ40gAm4"
      },
      "outputs": [],
      "source": [
        "#Import Library\n",
        "import pandas as pd \n",
        "from matplotlib import pyplot as plt \n",
        "import seaborn as sb\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Read CSV\n",
        "df=pd.read_csv('dataasuransi.csv')"
      ],
      "metadata": {
        "id": "KEthxLRxiPU5"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Menampilkan DataFrame\n",
        "df.head(5)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "RDMB8buZiaMm",
        "outputId": "69be4b39-4265-4a65-a699-d1556aa4a39b"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   umur  membeli_asuransi\n",
              "0    22                 0\n",
              "1    25                 0\n",
              "2    47                 1\n",
              "3    52                 0\n",
              "4    46                 1"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-47733d61-8bff-45d1-9c3e-d4854d2aaba9\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>umur</th>\n",
              "      <th>membeli_asuransi</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>22</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>25</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>47</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>52</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>46</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-47733d61-8bff-45d1-9c3e-d4854d2aaba9')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-47733d61-8bff-45d1-9c3e-d4854d2aaba9 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-47733d61-8bff-45d1-9c3e-d4854d2aaba9');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Menampilkan ke dalam plot\n",
        "sb.regplot(x='umur',y='membeli_asuransi',data=df,logistic=True,color='red')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 467
        },
        "id": "6b5BFxR2ih2z",
        "outputId": "55396cad-0666-4f32-98f9-d6a497c79545"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<Axes: xlabel='umur', ylabel='membeli_asuransi'>"
            ]
          },
          "metadata": {},
          "execution_count": 4
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAjcAAAGwCAYAAABVdURTAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAABYx0lEQVR4nO3deXiTVdoG8Dtp032ndAHKIqvIVllqWQTHMrigIoNT/UZBUBEHUMQZFlkdFRQVEUGqKKKOCsLIuICAlGVQKso2gCgIskNLCzTdt+R8f5xp09AW0jTJSd7cv+vKVXLyJn3SNM3Nec+iE0IIEBEREWmEXnUBRERERI7EcENERESawnBDREREmsJwQ0RERJrCcENERESawnBDREREmsJwQ0RERJriq7oAVzObzTh37hxCQ0Oh0+lUl0NEREQ2EEIgPz8fTZo0gV5/9b4Zrws3586dQ0JCguoyiIiIyA6nT59Gs2bNrnqM14Wb0NBQAPKHExYWprgaIiIiskVeXh4SEhKqPsevxuvCTeWpqLCwMIYbIiIiD2PLkBIOKCYiIiJNYbghIiIiTWG4ISIiIk1huCEiIiJNYbghIiIiTWG4ISIiIk1huCEiIiJNYbghIiIiTWG4ISIiIk3xuhWKSRGzGdi7F8jJAaKjgcRE4BobnxHVi9Z+x2x9Po4+TmWNKmnp5+2Mx/O011ootG3bNjF48GARHx8vAIg1a9Zc8z5btmwRiYmJws/PT7Ru3Vq8//779fqeRqNRABBGo9G+oqn+0tOFGDhQiObNhYiLk18HDpTtRI6gtd8xW5+Po49TWaNKWvp5O+Px3OS1rs/nt04IIVwfqaRvvvkG33//Pbp3746hQ4dizZo1GDJkSJ3HHz9+HJ06dcKYMWPw6KOPIj09HRMmTMDatWsxaNAgm75nXl4ewsPDYTQaubeUK2zeDDz+OJCfDzRqBPj7A6WlwMWLQGgo8PbbwB/+oLpK8mRa+x2z9fk4+jiVNaqkpZ+3Mx7PjV7r+nx+Kw031el0umuGm8mTJ2Pt2rU4ePBgVdv999+P3NxcrF+/3qbvw3DjQmYzcNttwP79QNOmQPXNzoQAzp4FunQB1q93vy5q8gxa+x2z9fmsWwfccYfjjqvPz8fRNap8bbT087b1MevzeIBbvdb1+fz2gHe7RUZGBlJSUqzaBg0ahIyMjDrvU1pairy8PKsLucjevcDhwzLFX7mLq04HREXJ2/fuVVMfeT6t/Y7Z+nxWrHDscfX5+Ti6RpWvjbN+3lFR8jYhLBcAiIwEfv0V2LPH+rbqF7PZ+rJ7t7zPtR5z9+6a963tYuvj7dolL7Yc+8knNY+r7efjwtfaowYUZ2ZmIjY21qotNjYWeXl5KC4uRmBgYI37zJ07F88995yrSqTqcnKAsjLZPVmbgADg8mV5HJE9tPY7ZuvzOXnSscfl5NT+IVvbh+/p00BJCRARAZhM1h9kAODrK28/dEh+DQsDystrfm8fH6C4WH4oxsVZHqf649X337Zcr962fz9QVASEhMhaa1NUJANBUREQHGz7caWlNY/R6eRz/u9/5c/FFvv3y/uEhFz9MffvB8LDHfd4Bw7I67Ycu3ev9XE6nfXvnIL3oUeFG3tMnToVEydOrLqel5eHhIQEhRV5kehowM9P/rLXEjxRUiJvj452fW2kDVr7HbP1+bRoIb+WlMjjrgwGRUUyPERGyq8FBfIDplLlccXF8oOoqAj47TfbajSb5WMWFlo/ZqXiYuvvXVxc93G+vrL+wkLbvrejhYcDBoP8eddWY2mpvL1JE/m1rMwxx0VG2l5jZKRjH7O+j+eI563gfehRp6Xi4uKQlZVl1ZaVlYWwsLBae20AwN/fH2FhYVYXcpHERKB9ezmgrLb/TV26JG9PTFRTH3k+rf2Ode0KtG0r/4dbUSEv5eXyUloKZGcDzZsDPXsCzZoBFy7ID46yMnkpL5dfL16UAWjAAPn10iXZy1J5aqKyZyY3F2jVCrj+ettr7NhR3ic3t/afudEob7/zTtuO69ixYT+zhnD0c3HGc7a1Rlsfsz6P56ifj4L3oUeFm+TkZKSnp1u1ffvtt0hOTlZUEV2VXg9MmSJHyp89K/93aDbLr2fPym7ZKVM8Y6AnuSdP+x0zmWQYyc+Xf/CzsoAzZ4ATJ4CjR4Hffwceekj+7/fMGXlcebnseTl/Xp7uePRR2dsyerS8npUle0HMZvk1K0ueHhg9WvaM2HJcfX4+er267+1ojn4uKn/etj5mfR6voT8fhe9DpbOlCgoKcPToUQBAYmIi5s+fj1tuuQVRUVFo3rw5pk6dirNnz+LDDz8EYJkKPnbsWIwaNQqbN2/Gk08+yang7m7zZuCll+SAsrIy2T3Zvr38ZVc9DZS0wd1+xyp7Uq68mM223T8jA3jnHeD4cRluDAb5P+PRo4Hq/5lz9HH1ofJ7O5qWft7OeLz6Pu8TJ+TvuoPfhx4zFXzr1q245ZZbarSPGDECy5cvx8MPP4wTJ05g69atVvd5+umncejQITRr1gwzZszAww8/bPP3ZLhRxF1WrSTtUvE7JoQ8XVRSIr9WXhzxZ9VsloNyL1+W4x86dqx7RVhHHqeyRpW09PN2xuPV53kfOSIHFDv4fegx4UYFhhsisltFhexqLy62jHXxrj+hRNdW2bPjYPX5/Nb8bCkiIruVl1vCTHFx7VOaicjtMNwQEVUymeS05KIieamoUF0REdmB4YaIvFtFhZyNVFAgAw0ReTyGGyLyPhUVcpp1fn7dK84SkcdiuCEi72AyWQJNcbHqaojIiRhuiEjbiorkSqoFBZzZROQMZrPcc+zXX+VaU0eOyEUpP/0USEpSUhLDDRFpj8kkA43RyBlORI5UVib3ITt0SF5++UUGmtrGq+3bx3BDRNRgZWVyfxujkb00RA1VXi6DzMGDlsuRI7b/h2H/fufWdxUMN0Tk+YqL5cqpBQWqKyHyTELI/cz27wf++1/59eef5X8YbKHTyU1dO3SQG7EOGAB07+7Ukq+G4YaIPFdhodyAkgOEieqntFSGl717LZecHNvuazDIPaM6dpRB5vrrgXbt5MaZlbc7YYXi+mC4ISLPU1AAXLwo/0AT0bXl5wN79gC7dwO7dsmeGVtOL1UGmU6d5KVzZ6B1a9nuxhhuiMhzFBXJ/11ybRqiq8vPlyHmxx+BnTvlwF9bdqVv0QLo0gXo2lVeOnSQu3t7GIYbInJ/JSUy1HAFYaLalZbKnpkdO+Tl0KFrh5mAABlkEhOBbt3kJSrKFdU6HcMNEbkvIYDsbDkDiogshJBTsLdvB77/Xp5uutbg34gI4MYbgR495KVjR7c/vWQvhhsick8lJUBmpu2zNYi0LjdXBpnt24HvvpPB/2oiIoBevSyXtm0Bvd4VlSrHcENE7kUIOQPq4kXVlRCpJYRc6XfLFmDbNjmjyWSq+/igIKBnT6B3b+Cmm+QMJi8JM1diuCEi91FcDFy4wFlQ5L0qKuQppvR0eTlzpu5jdTo5e6lvX6BPHzl+xgMH/zoDww0RqVdeLrvYuQgfeaPSUnmaaeNGYOvWq48xa9QI6NcPuPlmIDlZMwOAHY3hhojUMZvlKajLl7ldAnmXoiLgP/+RgWbLlqvPBLzhBrni74ABcq0ZLz3VVB8MN0SkRkGBPAVVUaG6EiLXKC2Vg4HXrQM2b657ZW2DQY6ZufVW4A9/AGJjXVunBjDcEJFrVVTIUMNTUOQNTCbghx+Ar74Cvv227t/7oCDZMzNwoDzlFBLi0jK1huGGiFwnN1cuxmfLSqlEnkoIuSLwl18CX39d95TtkBDZMzNokBwUHBDg2jo1jOGGiJzPbAaysuSS8ERalZMDfPEFsGYN8NtvtR8TGChPN91+uxwY7O/v2hq9BMMNETlXeTlw7hynd5M2lZfLGU7/+pccIFzbOjQGgzzVNHiwPPUUFOTqKr0Oww0ROU9hIXD+PE9DkfacOgWsWgV8/rnssalNYiJw992ylyYy0rX1eTmGGyJyjtxcOXCYSCvKyoBNm4DPPgMyMmo/Jj4eGDIEuPdeucM2KcFwQ0SOZzQy2JB2ZGUBK1fKUFPb4GA/P+CPfwSGDpVTuH18XF8jWWG4ISLHysuTHwZEnkwI4KefgH/+U/bW1DaWpk0b4M9/Bu65R25SSW6D4YaIHCc/X+7kTeSpSkuBtWuBDz4Afv215u1+fnIMTWoqcOONcn8ncjsMN0TkGAUFDDbkuS5dAj7+GPj009p3pG/aFLj/fmDYMO7n5AEYboio4UpK5Kwo7g9FnubkSWDZMrk2TW3LFfTpAzz4INC/P8fSeBCGGyJqmIoKuY4Ngw15kv37gXfflRtXXvm76+8vx9EMHw60baumPmoQhhsisp8QMthw80vyBEIAO3cCb78N7NhR8/boaNlLk5rKU08ejuGGiOyXlSVPSRG5MyGAbduAtDRg796at7dsCTz6qFxwj9shaALDDRHZ5/JlOe2byF0JIbdGePNN4Oefa97etSswerTcvFKvd3l55DwMN0RUf0VFde90TKTatUJNcjLw+ONywT1O5dYkhhsiqh+TSc6MInI3QsixNK+/Dhw4UPP2W24BxowBunVzeWnkWgw3RFQ/mZm1r9ZKpNLevcD8+cCPP9a87ZZbgHHjgE6dXF8XKcFwQ0S2u3xZ7vRN5C6OHJGhZsuWmrfdcgswdizQubPr6yKlGG6IyDalpUBOjuoqiKSsLOCNN+Tie2az9W033QRMnCgHDJNXYrghomszm7kCMbmH/Hy5+N7y5TWXIejSRYaa5GQlpZH7YLghomvLzgbKylRXQd6sogJYvVr21ly6ZH1bq1bAM88AKSmc/UQAGG6I6FoKCwGjUXUV5M0yMoA5c+T4muqio4Hx4+Vmlr78OCML/jYQUd3MZjm2gUiFkyeBl18G0tOt2wMD5YrCI0cCwcFqaiO3xnBDRHXLyeG+UeR6xcVyq4T33gPKy61vu/de4OmngdhYNbWRR2C4IaLaFRcDubmqqyBvIgTw7bfA3LlyQ9bqEhOBZ5+Vg4aJroHhhohqEoKno8i1TpwAnn8e+O476/bYWGDyZOCOOzhYmGzGcENENV28yNlR5BplZcA77wBvv239O2cwyDE1Y8ZwXA3VG8MNEVkrLZUrERM52w8/ALNnA8ePW7f37QtMmwZcd52SssjzMdwQkbULF7hYHznX5ctyFtSaNdbtMTEy1AwaxFNQ1CAMN0RkkZcnBxITOYMQwDffAC+8IE99VtLrgb/8BZgwAQgJUVYeaQfDDRFJZjP3jiLnycyUp6Cu3ODyhhuA557j5pbkUAw3RCRdusQ1bcjxhJDbJrz0ElBQYGkPCACeegoYPpyrC5PD8TeKiORCaRxETI6WmQlMnw5s327dftNNctp38+Zq6iLNY7ghIrkxJgcRk6MIAXz+uVyMLz/f0h4aKtesGTaMA4a1KjgYiIxUXQXDDZHXKyqyPl1A1BDZ2bK3ZutW6/b+/WVvDbdN0B6dTgbXyEjA3191NQAYboi8mxBy6jeRI2zaJINN9VOcISFy24ShQ9lbozU6HRARIUONm42b0qsuAAAWL16Mli1bIiAgAElJSfjxxx+vevyCBQvQvn17BAYGIiEhAU8//TRKSkpcVC2RhuTmciViariCAmDqVGDsWOtg07cv8PXXwJ/+xGCjJT4+QKNGcpHFxo3dLtgAbtBzs3LlSkycOBFpaWlISkrCggULMGjQIBw+fBgxMTE1jv/kk08wZcoULFu2DL1798aRI0fw8MMPQ6fTYf78+QqeAZGHMpms1xohsseePcDf/w6cOWNpCwiQY2seeIChRkt8fWUvTXi4XJvIjemEUDuKMCkpCT179sSiRYsAAGazGQkJCRg/fjymTJlS4/hx48bhl19+QXp6elXbM888g507d+K7KzdcA1BaWorS0tKq63l5eUhISIDRaERYWJgTnhGRh8jKAoxG1VWQpzKZgLQ0YPFi+e9KnTsDr7wCtGqlrjZyLF9fICpKhhqFYTUvLw/h4eE2fX4rjV5lZWXYvXs3UlJSqtr0ej1SUlKQkZFR63169+6N3bt3V526+v3337Fu3TrccccdtR4/d+5chIeHV10SEhIc/0SIPE1pKYMN2e/cObk+zcKFlmDj4wOMHw98+imDjVYYDHIAeKtWcmyNB/XCKT0tlZOTA5PJhNgrRs/Hxsbi119/rfU+//d//4ecnBz07dsXQghUVFRgzJgxePbZZ2s9furUqZg4cWLV9cqeGyKvxkHEZK+NG+X+T3l5lrZmzYDXXgO6dVNWFjmQr68cUxMW5lGBpjr3PmlWi61bt2LOnDl46623sGfPHnz++edYu3Ytnn/++VqP9/f3R1hYmNWFyKvl53P/KKq/0lLgH/+QvTPVg83gwcC//81gowW+vnLz0latlJ+CaiilPTfR0dHw8fFBVlaWVXtWVhbi4uJqvc+MGTPw0EMP4dFHHwUAdO7cGYWFhRg9ejSmTZsGvZsPciJSymyW65AQ1cfJk3JTy0OHLG1BQcCsWcA993j0hyBBDg6OipKDhTXyWipNAn5+fujevbvV4GCz2Yz09HQkJyfXep+ioqIaAcbHxwcAoHhsNJH74/5RVF/r1gH33msdbG64AVizBhgyRDMfhl6pcp2aVq1kuNHQa6l8KvjEiRMxYsQI9OjRA7169cKCBQtQWFiIkSNHAgCGDx+Opk2bYu7cuQCAu+66C/Pnz0diYiKSkpJw9OhRzJgxA3fddVdVyCGiWlRUcP8osl1Zmdzs8uOPrdsffFBO8/bzU1MXOUZYmAw0Gn0dlYeb1NRUZGdnY+bMmcjMzES3bt2wfv36qkHGp06dsuqpmT59OnQ6HaZPn46zZ8+icePGuOuuu/Diiy+qegpEnuHiRe4fRbY5f17u2P3f/1raQkKAF18EbrtNXV3UMJXbJGg41FRSvs6Nq9VnnjyRZpSWynETRNfy/ffAxIly9epKN9wAvPEGwJmmnkmns/TUGAyqq7FbfT6/lffcEJEL5OSoroDcndksF+VbuNC6hy81VU79dpMNEakeNBJq7MFwQ6R1RUVAYaHqKsidFRTILRQ2b7a0+fsDzz0nBxOT5wkLk2vVeFmoqcRwQ6R17LWhqzl2TG54efy4pa15c+DNN4EOHdTVRfYJDpabWWp8TM21MNwQaVl+PlBSoroKclfp6bLHpnrP3oABcm8ojkn0LAEBMtQEBqquxC0w3BBplRDstaHamc3AW2/J3pnq/vpXuQIxF0P1HAYDEB0tZ0FRFYYbIq0yGoHyctVVkLspKgKmTAE2bLC0BQXJ3ppqmxiTm9PgqsKOxHBDpEVCyNWIiao7d06Or6m+2nDLlrIXp3VrZWVRPYWHy94aLlxbJ4YbIi3KzeU2C2Rtzx5g3Di5mGOlvn2B11/n+BpPwcHCNmO4IdIas5m9NmTtiy/kWjXVT1OOGAFMmiR3gib35u8ve2qCg1VX4jH4W02kNbm5gMmkugpyB0LIRfneesvSZjAAs2cDw4YpK4ts5OMjQ014uOpKPA7DDZGWmM3cHJOk0lJg6lRg7VpLW2QksGgR0KOHurro2ip3627UiDPX7MRwQ6Qlly+z14bkuJqxY4G9ey1trVsDb7/N/aHcHcfVOATDDZFWmEzstSG54vDo0cCZM5a23r3lxpccOOy+fH2BmBi5+zo1GMMNkVZcvixPS5H32rVLLsRnNFraUlOBGTO8do8hjxAeLntreArKYRhuiLRACOsPNPI+69bJ2U/VZ0RNmgSMGsVF3tyVwQDExspFFMmhGG6ItCA/n2NtvJUQwLvvAq++amnz85MrDt92m7q6qG46nRzc3agRg6eTMNwQaUFuruoKSAWTCXjxReDjjy1tERFy6nf37srKoqsICJC9Nf7+qivRNIYbIk9XUsKdv71Raanc0bv6HlEJCcDSpUCrVurqotrp9XLNmogI1ZV4BYYbIk/HXhvvk5cnp3r/+KOlrXNnOdW7USN1dVHtfH2BZs04vduFGG6IPJnJJMfbkPfIygIefRQ4csTSdvPNcqo3B6a6Hz8/GWy4zYVLcd4ZkSfLy5MDSsk7HD8O3H+/dbAZOlSOsWGwcT8BAfJUIYONy/EnTuTJeErKexw8CDz2mPWmqGPGABMmcMaNOwoOBuLjuXaNIgw3RJ6qsNB6TRPSrh9+kIvzFRZa2qZPBx56SF1NVLfQUCAujqFTIYYbIk/FXhvvsGmT7J2pDLK+vsBLLwF33aW0LKpDeLic6k1KMdwQeaLycuv/xZM2ff45MG2aZVuNgABg4UKgf3+1dVHtIiPlNgqkHMMNkSfKyVFdATnbhx/KBfoqhYUBaWlcnM9dNWrEafhuhOGGyNOUlHD6t5YJIUPMggWWtsaN5RYLHTooK4vqoNPJ14eL87kVhhsiT5OdrboCchYh5J5Q771naWvaFHj/faBFC3V1Ue38/OSMKG6l4HYYbog8SUEBUFysugpyBrMZeO45YMUKS1vLlsDy5fIDlNxLeDgQE8MZUW6K4YbIUwjBsTZaZTLJgcNr1ljaOnQAli3jOA534+srQ01IiOpK6CoYbog8hdEIlJWproIcrbwcmDQJWLfO0tatG/DOO7J3gNyDXg9ERckZUeytcXsMN0SewGwGLl5UXQU5WlkZ8PTTci2bSr16yQHFwcHq6iILnU4GmqgorjbsQRhuiDzBpUvy1AVpR2kpMH48sG2bpa1vX2DRIiAwUF1dZOHvDzRpAhgMqiuhemK4IXJ3ZjNXI9aa4mK5ncKOHZa2W26RC/T5+amriyy4hYJHY7ghcndGo2WFWvJ8RUXAE0/I/aIqDRoEvPoqg427iI6Wp6HIY9kcbqKionDkyBFER0cjMjISuquk2UvVd60looZhr412FBbKnbx//NHSNngw8PLLchYOqaXXy2n3HO/k8Wx+N73++usIDQ2t+vfVwg0ROUhBAXf+1oqCAuDxx4FduyxtQ4YAc+YAPj7KyqL/CQqSp6EYMjVBJ4QQqotwpby8PISHh8NoNCIsLEx1OURXd/o0F+3TgoIC4LHHgD17LG1DhwIvvMBgoxq3T/AY9fn8tmte2549e3DgwIGq61988QWGDBmCZ599FmVch4PIMUpLGWy0oLZgc999clNMBhu1AgLkthYMNppjV7h5/PHHceTIEQDA77//jtTUVAQFBWHVqlWYNGmSQwsk8lqXL6uugBqqoAAYPdo62KSmAv/4B9dMUS08HEhI4CBujbLr3XXkyBF069YNALBq1Sr0798fn3zyCZYvX45//etfjqyPyDuZTNz529MVFsoxNrt3W9pSU4HZsxlsVNLp5PYJsbGc5q1hdo2cEkLA/L+pqZs2bcLgwYMBAAkJCcjh3jdEDZebK/eSIs9UGWyqDx7+858ZbFTz8ZGzoYKCVFdCTmZXuOnRowdeeOEFpKSkYNu2bViyZAkA4Pjx44iNjXVogUReRwi5tg15puJiOd37p58sbcOGyR2/GWzU8fMDmjblasNewq532oIFC7Bnzx6MGzcO06ZNQ5s2bQAAq1evRu/evR1aIJHXKSgAKipUV0H2KCmRKw9XX8dm6FDg+ecZbFQKDJTjaxhsvIZDp4KXlJTAx8cHBjf+BeJUcHJ7nP7tmcrKZLDZvt3Sdu+9ch0bBht1QkLkqSiOr/F49fn8btBqRWVlZbhw4ULV+JtKzZs3b8jDEnmvsjIGG09UVgY8+aR1sBk8WE73ZrBRJyJCDh4mr2NXuDly5AgeeeQR7Ki+6RvkQGOdTgcTdy8msg/H2nie8nLgmWeALVssbbfdJrdU4Do26nB/KK9mV7gZOXIkfH198fXXXyM+Pp5bMRA5ghBAXp7qKqg+TCZg8mRg40ZLW0qK3ASTy/irwf2hCHaGm3379mH37t3o0KGDo+sh8l75+fLDkjyD2QxMnw6sXWtpGzAAeP11DlxVxd8faNKEP3+yL9x07NiR69kQORpPSXkOIeS+UJ9/bmnr0wdYuJAr3qoSGioX5uMYJ4KdU8FffvllTJo0CVu3bsXFixeRl5dndSGieuI+Up5DCGDePODjjy1tPXsCixfLngNyvcaN5akoBhv6H7t6blJSUgAAt956q1U7BxQT2Ym9Np5j0SJg2TLL9S5dgLQ0uZYKuZZeD8TFyeneRNXYFW62VJ8VQEQNw4HEnuO992S4qXT99cC77/LDVQVfX7niMHvLqBZ2hZv+/fs7ug4i75WfLwenkntbsUKejqrUurXswQkPV1eTtwoIkAOHOSON6tCg34yioiKcOnUKZWVlVu1dunRpUFFEXiU3V3UFdC1ffik3vayUkAC8/z7XUVEhKEj22HAJEroKu8JNdnY2Ro4ciW+++abW2znmhshG+flyPyJyX5s2AVOmWHZpj40Fli+XX8m1goNljw2DDV2DXUPLJ0yYgNzcXOzcuROBgYFYv349PvjgA7Rt2xZffvllvR9v8eLFaNmyJQICApCUlIQfq286V4vc3FyMHTsW8fHx8Pf3R7t27bBu3Tp7ngqROkIAXFLBve3YAUyYYFl/KCpK9tg0a6a0LK8UEsJgQzazq+dm8+bN+OKLL9CjRw/o9Xq0aNECAwcORFhYGObOnYs777zT5sdauXIlJk6ciLS0NCQlJWHBggUYNGgQDh8+jJha9gQpKyvDwIEDERMTg9WrV6Np06Y4efIkIiIi7HkqROpcviyX7if3tG8fMHas5TUKC5NjbFq3VlqWVwoNlbOiGGzIRnaFm8LCwqrgERkZiezsbLRr1w6dO3fGnj176vVY8+fPx2OPPYaRI0cCANLS0rB27VosW7YMU6ZMqXH8smXLcOnSJezYsaNq9/GWLVvW+filpaUoLS2tus51eMgtVFQAly6proLq8uuvwGOPAUVF8npQEPDOO3J2FLlWWJgMNkT1YNdpqfbt2+Pw4cMAgK5du+Ltt9/G2bNnkZaWhvj4eJsfp6ysDLt3765aNwcA9Ho9UlJSkJGRUet9vvzySyQnJ2Ps2LGIjY1Fp06dMGfOnDrH+cydOxfh4eFVl4SEhHo8UyInycnhDCl3dfIk8Mgjlun5BoNcoC8xUW1d3ojBhuxkV7h56qmncP78eQDArFmz8M0336B58+ZYuHAh5syZY/Pj5OTkwGQyIfaKgXmxsbHIzMys9T6///47Vq9eDZPJhHXr1mHGjBl47bXX8MILL9R6/NSpU2E0Gqsup0+ftrk+IqcoKeG6Nu4qMxMYOdIyFkqvl3tF9e6tti5vxGBDDWDXaakHH3yw6t/du3fHyZMn8euvv6J58+aIjo52WHG1MZvNiImJwTvvvAMfHx90794dZ8+exSuvvIJZs2bVON7f3x/+XOSJ3El2tuoKqDaXLgGjRgFnz1ra5swBBg5UV5O3Cg/nbDRqkHr33JSXl6N169b45ZdfqtqCgoJw44031jvYREdHw8fHB1lZWVbtWVlZiKsjscfHx6Ndu3bw8fGparv++uuRmZlZY70dIreTl8c9pNxRQQEwejRw7Jil7dlngXvvVVeTt2KwIQeod7gxGAwocdC6HH5+fujevTvS09Or2sxmM9LT05GcnFzrffr06YOjR4/CXG28wpEjRxAfHw8/7sZL7qyigr027qisDBg3DjhwwNI2diwwYoS6mrwVgw05iF1jbsaOHYuXX34ZFRUVDS5g4sSJWLp0KT744AP88ssveOKJJ1BYWFg1e2r48OGYOnVq1fFPPPEELl26hKeeegpHjhzB2rVrMWfOHIwdO7bBtRA5VVaWZb0Ucg8mE/DMM0D1CQwPPgiMH6+uJm/FYEMOZNeYm59++gnp6enYuHEjOnfujODgYKvbP//8c5sfKzU1FdnZ2Zg5cyYyMzPRrVs3rF+/vmqQ8alTp6Cvto19QkICNmzYgKeffhpdunRB06ZN8dRTT2Hy5Mn2PBUi1zAagcJC1VVQdUIAM2cCGzda2u66C5g2jeupuFpYGIMNOZROiMo1xW1X2atSl/fff9/ugpwtLy8P4eHhMBqNCAsLU10OeYPycjm9mFO/3currwJLl1quDxggd/z+3/pZ5CKcFUU2qs/nt109N+4cXojcTlYWg427WbbMOth07w4sWMBg42qVKw8TORj3iydypsuXLavckntYswZ4+WXL9fbtgbQ0IDBQXU3eqFEjeSFyArvCTatWraC7yjnp33//3e6CiDTDZOLGmO5m82Y5pqZSQgLw3nvy1Ai5hk4ne2tCQ1VXQhpmV7iZMGGC1fXy8nLs3bsX69evx9///ndH1EXk+XJz5aBVcg+7dlnv8B0dLU9PNW6stCyv4usrd/YOCFBdCWmcXeHmqaeeqrV98eLF2LVrV4MKItIEIWS4Iffw66/AmDFA5Sa6ISHAu+8CzZurrcub+PsDTZvKgEPkZHatc1OX22+/Hf/6178c+ZBEnikvj2vauIvTp4FHHwXy8+V1Pz9gyRLu8O1KQUHyFCCDDbmIQ3/TVq9ejaioKEc+JJFnunxZdQUEyP2iHn3UsjJ05UaYvXqprcubVM6I4tpB5EJ2hZvExESrAcVCCGRmZiI7OxtvvfWWw4oj8kiFhXJJf1KroAB47DHgxAlL2z/+AaSkKCvJ60READExqqsgL2RXuBkyZIjVdb1ej8aNG2PAgAHo0KGDI+oi8lzstVGvrExuoXDwoKXt6aeB++5TV5O34VRvUsiucDNr1ixH10GkDWVlXNdGNbMZmDIF2LHD0vbQQ8Djj6uryZv4+MjTUFdsy0PkSnYNKN6zZw8OVNtB94svvsCQIUPw7LPPoozd8eTN2GujlhDAnDnA2rWWtsGDgWef5ZgPV/D3lzPQGGxIMbvCzeOPP44jR44AkAv2paamIigoCKtWrcKkSZMcWiCRxzCZ5CwpUmfpUuCjjyzX+/QB5s6VA4nJucLDZbDhFhbkBux6xx85cgTdunUDAKxatQr9+/fHJ598guXLl3MqOHkvLtqn1r/+Bbz2muV6p07AwoVy6jc5j14PxMfLXb3ZO0Zuwq4xN0IImP+3EeCmTZswePBgAEBCQgJyuNw8eSOzmaekVNqyBZgxw3K9RQvgnXfkYn3kPIGBcnwNe2vIzdgVbnr06IEXXngBKSkp2LZtG5YsWQIAOH78OGJjYx1aIJFHuHyZO3+rsndvzW0V3nuPM3WcSaeTP1+ua0Zuyq7TUgsWLMCePXswbtw4TJs2DW3atAEgF/Hr3bu3QwskcntmM7daUOXYMbmtQkmJvB4cLLdVSEhQW5eWGQzy58tgQ25MJ4TjBgmUlJTAx8cHBjfuoszLy0N4eDiMRiPCuBMwOcLFi/JCrpWVBaSmAufPy+sGgww2N92kti4tCwuTi/JxgDYpUJ/Pb4duvxDAnV7J27DXRo28PLmtQmWw0emAefMYbJxFr5ehhv8hJA9hV7gxmUx4/fXX8dlnn+HUqVM11ra5dOmSQ4ojcnu5udwg09VKS4G//hX433IUAIBp04A77lBXk5b5+8vZUJx1Rh7Err7F5557DvPnz0dqaiqMRiMmTpyIoUOHQq/XY/bs2Q4ukchNcYaU65lMwN/+Bvz0k6Xt8cflCsTkeL6+QNOmDDbkcewKNx9//DGWLl2KZ555Br6+vnjggQfw7rvvYubMmfjhhx8cXSORe2KvjWsJATz/PLBxo6Vt6FC5ZxQ5nk4HNGkiAw6Rh7Er3GRmZqJz584AgJCQEBiNRgDA4MGDsbb6sudEWmUysdfG1ZYsAT791HK9f3+5yzcXjnOOuDiA4yjJQ9kVbpo1a4bz/xvI17p1a2z83/+kfvrpJ/j7+zuuOiJ3JARw7hx7bVxp1SrgjTcs17t2BRYs4OJxzhIVBYSGqq6CyG52hZt7770X6enpAIDx48djxowZaNu2LYYPH45Ro0Y5tEAit5OZCRQXq67Ce2zeDMycabnesiWQlgYEBSkrSdNCQuRCiEQezCHr3Pzwww/YsWMH2rZti7vuussRdTkN17mhBsnO5ukoV9q7F3j4YcsifY0bAytWAM2aKS1Ls4KC5ABinuojN+TydW5uuukm3FTL+hJ33nkn3n33XcTHxzvi2xCplZvLYONKV64+HBIiF+ljsHEOBhvSEKcOg//Pf/6DYnbfkxYUFgIXLqiuwntkZclF+ioXSDQYgEWLgA4dlJalWcHBcmYUgw1pBNfQJrqWsjLLSrjkfJWrD587J69Xrj6cnKy2Lq1isCENYrghuhohZLDhjt+uUVoKjB3L1YddhcGGNIrhhuhqsrLkBy45n8kE/P3vwI8/WtpGj+bqw87i4yPXsmGwIQ1iuCGqi9EoT5GQ8wkBvPgisGGDpe3ee4GJE9XVpHWNG8uAQ6RBDDdEtSkt5QBiV3r7beDjjy3Xb75ZbrXAXgXnCA7mDt+kaU4NN88++yyioqKc+S2IHM9sloNZG74EFNli9Wrg9dct17t0kasRc/Vh59DrgdhY1VUQOZXNi/h9+eWXuP3222EwGPDll19e9di7777bIcU5Axfxo2vKypKnpMj5tmyRA4grt7Jo2VLuH8X/FDlPbCwQHq66CqJ6q8/nt83hRq/XIzMzEzExMdDr6+7w0el0MLnxnjsMN3RVhYXA2bOqq/AOta0+/OmnQEKC0rI0LSiIiyCSx3LKCsXmalNhzZwWS1pkNsteG3K+ulYfZrBxHh8fno4ir+HUFYqJPEp2NlBRoboK7cvMBB55xHr14cWLufqwMxkMcmsFjmMiL2FzuFm4cKHND/rkk0/aVQyRMkVFHGfjCkajXH24csVnnQ545RWglr3pyEECAmSw4bRv8iI2j7lp1aqVbQ+o0+H3339vUFHOxDE3VIPZDJw4wV4bZyspAUaNAnbvtrTNmAE8+KC6mrQuOBiIj5czpIg8nFPG3Bw/frzBhRG5JZ6Ocr6KCrkgX/VgM2YMg40zhYXJFYiJvFCD4nxZWRkOHz6MCn4wkKcqKeHpKGcTApg9G0hPt7QNGwZMmKCqIu3z9+fgYfJqdoWboqIiPPLIIwgKCsINN9yAU6dOAQDGjx+Pl156yaEFEjkVVyF2vgULgFWrLNdvuQV47jmuPuwser08FcWfL3kxu8LN1KlT8d///hdbt25FQEBAVXtKSgpWrlzpsOKInCovzzIVmZzjo4+AtDTL9RtvlKsR+3KiptPExAB+fqqrIFLKrr8w//73v7Fy5UrcdNNN0FX738ENN9yAY8eOOaw4Iqcxm4GcHNVVaNu6dXIzzEpt28qgExioriatCwvjnlFEsLPnJjs7GzExMTXaCwsLrcIOkdu6dImDiJ1pxw5g0iTL/lxNmgDvvcdl/53Jz0/22hCRfeGmR48eWLt2bdX1ykDz7rvvIjk52TGVETlLeTlw+bLqKrRr/365X1R5ubweESFXH+YAV+fR6Tjlm6gau05LzZkzB7fffjsOHTqEiooKvPHGGzh06BB27NiBbdu2ObpGIsfKzuaO385y7BgwerRcFBGQp6DeeQdo3VptXVrXuLGcIUVEAOzsuenbty/27duHiooKdO7cGRs3bkRMTAwyMjLQvXt3R9dI5DhFRUBBgeoqtCkzU64+XNkr5usLvPkm0LWr2rq0LjRU9o4RURW7pyy0bt0aS5cudWQtRM6Xna26Am3KzZX7RZ07J6/rdMDLLwP9+iktS/P8/Hi6j6gWdocbk8mENWvW4JdffgEAdOzYEffccw98OcWT3JXRCJSWqq5Ce4qK5GrDR49a2qZNAwYPVleTN+A4G6I62ZVEfv75Z9x9993IzMxE+/btAQAvv/wyGjdujK+++gqdOnVyaJFEDWY2Axcvqq5Ce8rKgPHjgb17LW1//Svw0EPqavIWMTEcZ0NUB7si/6OPPoobbrgBZ86cwZ49e7Bnzx6cPn0aXbp0wejRox1dI1HDXb7Mqd+OZjIBkycD331naUtNBZ58Ul1N3iIsjNPqia7Crp6bffv2YdeuXYiMjKxqi4yMxIsvvoiePXs6rDgih6io4NRvRxMCeOEFuVBfpdtuA2bN4rL/zhYSwnE2RNdgV89Nu3btkJWVVaP9woULaNOmTYOLInKoixflaSlynIULgU8+sVzv0wd45RXAx0ddTd4gNJT7RhHZwOZwk5eXV3WZO3cunnzySaxevRpnzpzBmTNnsHr1akyYMAEvv/yyM+slqp/SUu767WgffAC89Zbleteucso39zNyLgYbIpvphLBtNTO9Xm+1tULl3Srbql83mUyOrtNh8vLyEB4eDqPRiDDuwaJ9Z85YFpSjhluzBpgyxXK9TRvgn/8Eqp2iJicICwPi4lRXQaRUfT6/bR5zs2XLlgYXVpfFixfjlVdeQWZmJrp27Yo333wTvXr1uub9VqxYgQceeAD33HMP/v3vfzutPvJQhYUMNo60aZOc4l2paVNg2TIGG2djsCGqN5vDTf/+/Z1SwMqVKzFx4kSkpaUhKSkJCxYswKBBg3D48OFaN+esdOLECfztb39DPy4SRrURggv2OVJGBjBhgpwhBQDR0cD773Ngq7Mx2BDZxebTUlcqKSnB/v37ceHCBZivGKx599132/w4SUlJ6NmzJxYtWgQAMJvNSEhIwPjx4zGlevd3NSaTCTfffDNGjRqF7du3Izc31+aeG56W8hK5ucCFC6qr0Ib9+4ERIyy9YGFhwEcfAR06qK1L6xhsiKw45bRUdevXr8fw4cORk5NT47b6jLkpKyvD7t27MXXq1Ko2vV6PlJQUZGRk1Hm/f/zjH4iJicEjjzyC7du3X/V7lJaWorTaqrR5eXk21UYezGTign2OcuQI8Nhj1hthvv02g42zMdgQNYhdU8HHjx+P++67D+fPn4fZbLa61GcwcU5ODkwmE2Kv6NqOjY1FZmZmrff57rvv8N5779m8r9XcuXMRHh5edUlISLC5PvJQFy9aTp+Q/U6eBEaNkr1gAGAwyFlRN96otCzNY7AhajC7wk1WVhYmTpxYI5Q4W35+Ph566CEsXboU0dHRNt1n6tSpMBqNVZfTp087uUpSqqyMU78d4fx5YORIy7glvR549VVuhOls4eEMNkQOYNdpqWHDhmHr1q1o3bp1g755dHQ0fHx8aiwImJWVhbha3uDHjh3DiRMncNddd1W1VY738fX1xeHDh2vU5O/vD3/uv+I9srPlYGKy38WLwMMPA2fPWtpeeEGuQEzOExkJNG6sugoiTbAr3CxatAj33Xcftm/fjs6dO8NgMFjd/qSNe8v4+fmhe/fuSE9Px5AhQwDIsJKeno5x48bVOL5Dhw44cOCAVdv06dORn5+PN954g6ecvF1BgZz+TfYzGuWpqBMnLG3TpgF/+pOykrxCVJScgUZEDmFXuPn000+xceNGBAQEYOvWrVaL++l0OpvDDQBMnDgRI0aMQI8ePdCrVy8sWLAAhYWFGDlyJABg+PDhaNq0KebOnYuAgIAaO45HREQAAHci92ZCADk53D+qoQoKgNGjgV9/tbRNmAAMH66sJK8QHS3DDRE5jF3hZtq0aXjuuecwZcoU6PV2DdupkpqaiuzsbMycOROZmZno1q0b1q9fXzWe59SpUw3+HqRhJSVAZqYca0P2Ky4GnngC2LfP0vboo8CYMcpK8goMNkROYdc6N1FRUfjpp58aPOZGBa5zoyEXLwKXLnGMTUOVlclg8913lrb77wdmz+Y+Rs7EWVFE9VKfz2+7ukRGjBiBlStX2lUckUNkZclww2DTMOXlwNNPWwebe+8FZs1isHGmwECu7kzkRHadljKZTJg3bx42bNiALl261BhQPH/+fIcUR1SrCxc43dsRTCa5CeamTZa2226TM6N4Kth5DAagSROGRyInsivcHDhwAImJiQCAgwcPWt2m4xuWnCknx7KoHNnPbAamTwe+/trSdsstwCuvAL52/VkgW+j1csNRHx/VlRBpml1/xZy5QzhRnS5dkhdqGCGA554DPv/c0tanD/DGG4Cfn7q6vEF8PH/GRC7QoL7no0ePYsOGDSguLgYA2LkHJ9G15ebKXhtqGCGAF18EVqywtPXoASxaBHCxS+eKjgaCg1VXQeQV7Ao3Fy9exK233op27drhjjvuwPnz5wEAjzzyCJ555hmHFkiEkhLLNgBkPyGAefPkjt6VEhPlRphBQerq8gbBwZzyTeRCdoWbp59+GgaDAadOnUJQtT+KqampWL9+vcOKI4LZLPc5Yq9gwwgBLFgALFtmaevcGVi6FAgJUVaWVzAY5OkoInIZu8bcbNy4ERs2bECzZs2s2tu2bYuTJ086pDAiAHLKd3m56io835tvAmlpluvXXw+89x4QGqquJm+g08mZUZx9RuRSdr3jCgsLrXpsKl26dImbVJLjGI1Afr7qKjzfokXA4sWW6+3ayR6c8HB1NXmL2FiOZSJSwK5w069fP3z44YdV13U6HcxmM+bNm4dbbrnFYcWRFysrk+vZUMMsXix7bSq1aQMsX87xH64QESFXISYil7PrtNS8efNw6623YteuXSgrK8OkSZPw888/49KlS/j+++8dXSN5GyE4zsYRliwBFi60XG/dGvjgA6BRI3U1eYvQUCAmRnUVRF7Lrp6bTp064fDhw+jbty/uueceFBYWYujQodi7d69H7jdFbkQI4OxZoLRUdSWeLS1NDiCudN11MthERysryWsEBXHPKCLF7F6KNCAgAAMHDkTXrl1hNpsBAD/99BMA4O6773ZMdeRdhADOnQOKilRX4tkWL7busWnZUgabxo2VleQ1AgK4tQKRG7Ar3Kxfvx4PPfQQLl26VGPhPp1OB5PJ5JDiyMucPw8UFqquwrMtWmQ9xqZlS+DDD3mKxBX8/OTWCpwZRaScXe/C8ePH489//jPOnTsHs9lsdWGwIbucPw8UFKiuwnMJIXtrqgebVq3kgn3cfdr5/P2BZs24ZxSRm7Cr5yYrKwsTJ05ELP9okiNkZXHKd0NULtBXfR2b666TPTY8FeV8ERHy58xTUURuw66em2HDhmHr1q0OLoW80uXLcj0bso8Qcifv6sGmTRvZY8Ng41x6vVx5OCaGwYbIzeiEHbtdFhUV4b777kPjxo3RuXNnGAwGq9uffPJJhxXoaHl5eQgPD4fRaEQY16BQq7BQzowi+1Rugll9r6i2bTnd2xUCAmSwueJvHxE5T30+v+06LfXpp59i48aNCAgIwNatW6Gr9r8WnU7n1uGG3ERZmRxnQ/Yxm4HZs4GVKy1t118vVx7mAn3OFRAgx9dw4DCR27Ir3EybNg3PPfccpkyZAj3f4FRfJpPssfnfEgJUTyYTMG0asGaNpa1zZ+Ddd+X4D3KeyoHD/LtH5NbsCjdlZWVITU1lsKH6q1x9mJth2qe8HJg0CVi3ztKWmCh39+YmmM7FYEPkMex6l44YMQIrq3eHE9mCi/Q1TGkpMH68dbDp1Yu7e7uCnx+nehN5ELt6bkwmE+bNm4cNGzagS5cuNQYUz58/3yHFkYaYzfJUVHGx6ko8U2EhMHYskJFhaevbVy7aFxiori5vYDAw2BB5GLvCzYEDB5CYmAgAOHjwoNVtOk6JpCtVVHC/qIbIywNGjwb27rW0DRwIzJ8vexTIeXx85KrDvnbvVENECtj1jt2yZYuj6yCtKi8HzpzhGBt7XbwIPPoocOiQpe3uu4G5c/mB62x6vQw2DJBEHod/Hcl5Cgrk6sPcksM+Z88Co0YBJ05Y2u6/H5g1i4NanU2nkxtgBgSoroSI7MBwQ45nMgHZ2fJ0Ctnn6FEZbLKyLG2jRsmZUjz163yxsUBQkOoqiMhODDfkWIWF8gO5okJ1JZ5r/37gsceA3FxL2zPPyDYGG+dr3Bjg6uVEHo3hhhxDCODCBe4T1VA7dshZUZXT5XU6uRLx/fcrLctrNG4MREaqroKIGojhhhquvFwuzFdSoroSz7Z2LTB5smXwtcEAzJsH3HGH2rq8RUwMV3gm0giGG2qYwkIgM5ODhhvqgw+AOXMs1wMDgTffBPr1U1eTN2GwIdIUhhuyjxDApUtyqjLZTwjgtdfk9gmVIiKAd94BunZVVpZXiY0FwsNVV0FEDsRwQ/VXXCzH13BRvoYpLwdmzLDeALNpU7kB5nXXqavLm8TFcfAwkQYx3JDtOMXbcQoKgKeeAr77ztLWrp0MNrGx6uryFjqdDDbck4tIkxhuyDZGI5CTw7E1jpCVJbdT+PVXS1vPnsBbb7EXwRUqF+gLDlZdCRE5CcMNXV1JiTwFxZlQjvHbb3K9mvPnLW233w68/DLg76+uLm+h08lTf1ygj0jTGG6odiaT7KnhujWOs3OnXMMmP9/SNmoU8Pe/czsFV/DxkT023EWdSPMYbqimoiLZs8BTUI6zZo0cPFy5ho1OB0ybBjz0kNq6vIXBwE0wibwIww1Zy82Vp6HIMcxm4I03gLQ0S5u/v5z+PXCgurq8SUCADDY+PqorISIXYbghidsnOF5JCTB1KrBunaWtUSM5cLhbN2VleZWQECA+nntyEXkZhhuSp5/OnZPr15BjXLwox9fs3Wtpa9MGePttoFkzdXV5k/BwTqsn8lIMN97MZJI9NZcvc3yNI/36K/DEEzIwVurTB1iwgFO9XYXBhsirMdx4o4oKGWiMRjkmhBxn0yY5+6lyV28ASE2Vg4kNBnV1eZOwMAYbIi/HcONNzGZ5uiQ3V46xIccRQp5yev11S5teL3f5HjGCYz5cJTRUrjxMRF6N4cZb5OfLrRMqKlRXoj3FxcD06cDXX1vaQkJk0Ln5ZnV1eZuQEAYbIgLAcKN9ZWVyFlT10yTkOGfOAOPGAb/8Ymlr0QJYsgRo3VpdXd5EpwMiI+VMNPaQEREYbrQtN1f21vAUlHNkZAATJsifc6WbbpLr2kREKCrKy/j5yd6agADVlRCRG2G40SKTCcjMBAoLVVeiTUIAH34o94OqPstsxAhg0iTAl28rl4iKYm8NEdWKf4W1pqhIBhuOrXGOoiI586n6+Bo/P+D554EhQ5SV5VV8feXCfNwjiojqwHCjFULIjS4vX1ZdiXadOAGMHw8cOWJpi4sDFi0COndWVpZXCQmR07y5lQIRXQXDjRaUlMjemrIy1ZVo16ZNclp3QYGlrWdPuTBfdLSysryGTid/zpGRqishIg/AcOPJhJDr1ly6pLoS7aqokAFm6VLr9lGjgGee4fgaV/D1BZo04aBhIrIZ/zJ7IpNJrluTm8veGmfKygImTgR27bK0BQUBc+cCt92mri5v4uMjd/T291ddCRF5EIYbT1JYCOTlyVMjnN7tXNu3y20Uqo9hat0aePNNrl/jKno9gw0R2YXhxt1VVMhAk5vLGVCuUFEhA0xamnX73XcDs2cDwcFKyvI6Op0MNjwVRUR2YLhxV0VFcmNL9tK4zrlzwN/+BuzebWnz95dTv4cN43oqrlIZbDjVm4jspFddAAAsXrwYLVu2REBAAJKSkvDjjz/WeezSpUvRr18/REZGIjIyEikpKVc93uOYzcD583JZ//x8BhtX2bABuOce62DTqhWwahVw330MNq5SOcYmKEh1JUTkwZSHm5UrV2LixImYNWsW9uzZg65du2LQoEG4cOFCrcdv3boVDzzwALZs2YKMjAwkJCTgj3/8I86ePeviyp2gqEiupZKfr7oS71FcDMycCTz5pDz9V+nuu4F//Qto315dbd4mMFDuy8VgQ0QNpBNCbddAUlISevbsiUWLFgEAzGYzEhISMH78eEyZMuWa9zeZTIiMjMSiRYswfPjwax6fl5eH8PBwGI1GhIWFNbh+h+ACfGocOiRPQx07ZmkLCgJmzeJqw64WFcX1gojoqurz+a10zE1ZWRl2796NqVOnVrXp9XqkpKQgIyPDpscoKipCeXk5oqKiar29tLQUpaWlVdfzqv/v3B1wAT7XM5mA994DFi4Eysst7TfcAMyfD7Rsqaw0r+PjI7dSYG8NETmQ0tNSOTk5MJlMiI2NtWqPjY1FZmamTY8xefJkNGnSBCkpKbXePnfuXISHh1ddEhISGly3Qwghd+w+dYrBxpXOnpUbXL72mnWwGTUKWLGCwcaVQkPlz5vBhogcTPmYm4Z46aWXsGLFCqxZswYBdUwZnTp1KoxGY9Xl9OnTLq6yFpVja3gaynWEAP79bzmW5qefLO2xscDy5XJrBT8/VdV5l8remvh47hFFRE6h9LRUdHQ0fHx8kJWVZdWelZWFuLi4q9731VdfxUsvvYRNmzahS5cudR7n7+8Pf3dZBKykRG6VUH1/InK+7Gw5aHjzZuv2O+6Q42siIpSU5ZWCg2Wg5LYVRORESntu/Pz80L17d6Snp1e1mc1mpKenIzk5uc77zZs3D88//zzWr1+PHj16uKLUhikulqdDTp1isHElIYC1a4HBg62DTUgI8MorcnwNg43rhITIPaIYbIjIyZT/lZk4cSJGjBiBHj16oFevXliwYAEKCwsxcuRIAMDw4cPRtGlTzJ07FwDw8ssvY+bMmfjkk0/QsmXLqrE5ISEhCAkJUfY8alVQIE89FRerrsT75OQA//iHXL+muj59gBdekB+y5DrBwfI0FNcLIiIXUB5uUlNTkZ2djZkzZyIzMxPdunXD+vXrqwYZnzp1Cnq9pYNpyZIlKCsrw7Bhw6weZ9asWZg9e7YrS6+dySRXFuZ2CWoIAXzxhdzcMjfX0h4UJMfVpKbyA9bVgoJkmOTPnYhcRPk6N67m1HVuhACOHuWqwqqcOyfH0PznP9btvXoBc+YA7jJTzpsEBsoVh/UePXeBiNyAx6xzo0kMNq5nMslp3K++KmeiVQoKkov0PfAAP1xVCAhgsCEiJRhuyLP98ovc2PLAAev2fv2A556TH67keuyxISKFGG7IMxUWAosWAR98IHtuKkVEAFOnyk0wOcZDjaAgGWz48yciRRhuyLMIAWzaJMfQnDtnfdtddwFTpnCPIpWCgzl4mIiUY7ghz3HihJzGvX27dXvz5sDs2XKaN6kTGgrExTHYEJFyDDfk/oqLgbQ0udll9f2gDAbgkUeAJ56Qg1dJnbAwGWyIiNwAww25LyGAdevkasLnz1vf1rs3MH060Lq1mtrIIjxcbqlAROQmGG7IPR04IMfV7Nlj3R4XJwcMDxrE0x/uICICiIlRXQURkRWGG3IvWVnAggXAmjXWawYZDMDDD8tTUMHBqqqj6iIjgcaNVVdBRFQDww25h4ICOabm/fdr7sV1661y64QWLdTURjVFRXFWGhG5LYYbUquiAli9GnjzTbnZZXVt2wLPPivH15D7aNxY9toQEbkphhtSQwi5Y/cbbwC//259W6NGwLhxwJ//DPjyV9StxMXJmVFERG6MnxzkWkIA338PzJ8P/Pyz9W0BAcDIkcCjjwIhIWrqo9rpdEB8PF8XIvIIDDfkOrt3y56anTut2/V6YMgQYMIETil2R3q9XHU4KEh1JURENmG4Iefbt0+Oqfnuu5q3DRwoQ02bNq6uimzh6yv3ifL3V10JEZHNGG7IefbvBxYurLldAgDcdBMwcSLQtavr6yLb+PkBzZpx3BMReRz+1SLH++knYMkSObbmSomJwJNPcgaUuwsMlKeifHxUV0JEVG8MN+QYlQOFlywBdu2qeXvXrsD48UDfvlxZ2N1xA0wi8nAMN9QwFRXAxo3Au+/WnP0EAF26yGndN9/MD0t3p9fLrRQ41ZuIPBzDDdmnuBj4/HNg2TLgzJmat/fqJbdKSE5mqPEEAQFyqrfBoLoSIqIGY7ih+snKAj75BFixAsjNrXl7v37AmDFAjx4uL43sFBUlF05kCCUijWC4IdscPAh88AHwzTdAebn1bT4+wB13yMX3OnRQUx/Vn6+vHFvD9WuISGMYbqhuZWXAt98C//wnsGdPzdsDA4Fhw+Sqwk2bur4+sl9wsAw2nA1FRBrEcEM1ZWUBn30GrFwJZGfXvD0uDnjwQbn3U3i46+sj++l0cuPLiAjVlRAROQ3DDUlms1xB+LPPgM2bAZOp5jFdugAPPwz88Y8ceOqJ/P1lMOVqw0SkcQw33u7CBTnr6bPPgLNna97u5yfH0/zlLzLckOfR6eSg4agoDhomIq/AcOONysqALVtkqPnPf2SvzZWaNAEeeECOqYmKcn2N5BjsrSEiL8Rw4y2EAA4dAv79b+Crr4DLl2se4+MDDBgApKbKlYQ52NRz+fjIUBoRwd4aIvI6DDdad/68DDNffAEcPVr7MU2bAkOHAvfdB8TGurY+ciydTgaaqCiGUyLyWgw3WnT5MrBhA7B2rdzEUoiax/j7y4HBf/oTkJQkl94nzxYSAkRHy3FSRERejOFGK/LzgfR0GWh27JB7PtUmMRG45x7gzju5h5AWGAxyOn5YmFyUj4iIGG48mtEoA82GDXJH7itXDq7UvLkMNHffLf9Nnk2nkzt3h4VxdWEiolow3HiarCwZaNLTgR9+qLuHpnFjOYX7jjuArl05qFQLAgJkL01oKE8jEhFdBcONuxMC+O03OXV70yZg//66j42MlONo7rxTblzJAaWez8dH9tCEhXE6NxGRjRhu3FFpKbBzJ7B1q7zUtrhepehoYOBAYNAgoGdPjrvQAp1ODg6uPO3EXjcionrhJ6G7OHkS2L5dLqq3cydQUlL3sc2ayUBz663AjTeyh0YrfHzkNO6ICL6mREQNwHCjitEox8zs2CEvp05d/fhOnYBbbgFSUoD27fm/eS3x95eBJiyMrysRkQMw3LhKcTGwZ4/sldmxA/j559q3PagUFAT07i1XDO7fH4iJcVmp5AKVp57CwznjiYjIwRhunKWoCPjvf4Eff5SBZv/+uqdqV2rXDujXT166d+dibFrk62vppeH4KCIip+BfV0e5dAn47ju5zcHu3bJnpq5p2pUaNQKSk2UPTZ8+coND0iZ/fzmbLTSUp56IiJyM4cZR/vAH2VNzNcHBckZTUpIMNO3acb0SrQsKkvs88dQTEZHLMNw4Sr9+NcNNSIjc7qBXL+Cmm4COHXkqwhsYDJa1aQwG1dUQEXkdftI6Sr9+wMqVcmp29+6yh6Z9e07p9Ra+vrJnLjSUvTRERIox3DjK0KHAsGHA0aOqKyFX8PGRISYoCAgM5OBvIiI3wnDjKL6+cqsE0ia9XoaYykDDrRCIiNwWww1RXQIC5KmmoCD5b85yIiLyCAw3RIA8zeTvL0NMYKC8cCYbEZFHYrgh7+PrK4NM9QvHzBARaQbDDWmXXm8JLtW/cgYbEZGmMdyQNhgMNXtjuMYMEZFXYrghz+LjI3tgKnthKi8cH0NERP/DcEPuSa+3DjA8pURERDZiuCG1Kgf3GgyWHhk/P25TQUREduMnCDmfTmcJL5VjYypDDE8nERGRgzHcUMPpdPJ0ka+vDC+1XYiIiFyE4cZRKiqATz8F9uwBmjQB7ryz9lMrZjNw6BBw+TIQGSl3Cm9o74Wtj1mf4379FTAagehooEsXGVB8fS0hxsfH+t+21Lh3L5CTIx8zMbHu763iuPoeS0TqqHyv8u+EZxBuYNGiRaJFixbC399f9OrVS+zcufOqx3/22Weiffv2wt/fX3Tq1EmsXbvW5u9lNBoFAGE0GhtatsWrrwoRFSWEXi+ETie/hocLMXmyEIcPWy7LlwvRu7cQ8fFCREfLr717y/bqx9XnUttj9ukjxEcfCfH770KcOCHEqVNCrFghxM03C9G0qRAxMfLrgAFCfPWVEAUFQhQXC1FaKsTGjUKkpAjRvLkQcXHy68CBQqSn2//zSU+Xj3Gtx1R1XH2PJSJ1VL5X+XdCqfp8fisPNytWrBB+fn5i2bJl4ueffxaPPfaYiIiIEFlZWbUe//333wsfHx8xb948cejQITF9+nRhMBjEgQMHbPp+Dg83r74qhMEgQ43BIISfn/wKCOHrawk4y5fLN0KjRkK0bi3E9dfLr40ayfaPPhLi+HEhTp4U4vRpIc6cEeLcOSEyM4W4cEGInBwhLl0SIjdXiLw8GUjWrhXiuutkWLn+eiG6dROiY0chYmOFaNPG8oZLT5fXY2Pl7YmJDTuuPhz9vZ3xXJzxvInI8VS+V/l3Qrn6fH7rhFC7lXVSUhJ69uyJRYsWAQDMZjMSEhIwfvx4TJkypcbxqampKCwsxNdff13VdtNNN6Fbt25IS0u75vfLy8tDeHg4jEYjwsLCGlZ8RQUQGytP8wQEWN8mBFBSIk//HDsGDBsGHDwoT1ld2YV59qw89bN+ve3dm2YzcNttwP79QNOm1ps6CmF5zHXrgDvucNxxnlBjfZ4LYFuN9XneROR4tv49ccZ7VeX3pir1+fxW+iqUlZVh9+7dSElJqWrT6/VISUlBRkZGrffJyMiwOh4ABg0aVOfxpaWlyMvLs7o4zIoVclyKwSB/2atfKtdpycsDFi0Cjh6V52d9fGoeGxUFHD4sz+Paau9eeZ9GjWruVl39MVescOxxnlBjfZ6LrTXW53kTkeOpfK/y74THURpucnJyYDKZEBsba9UeGxuLzMzMWu+TmZlZr+Pnzp2L8PDwqktCQoJjigeAkydlaq8rqev18vZjx4CyMjkFujYBAfL2nBzbv3dOjm2PefKkY4/zhBrr81xsrbE+z5uIHE/le5V/JzyO5vvPpk6dCqPRWHU5ffq04x68RQuZ2s3m2m83m+XtrVvLXpzS0tqPKymRt0dH2/69o6Nte8wWLRx7nCfUWJ/nYmuN9XneROR4Kt+r/DvhcZSGm+joaPj4+CArK8uqPSsrC3FxcbXeJy4url7H+/v7IywszOriMPffD4SHA+XlsoemOiFke3g4MHky0L49cPFi7cdduiRvT0y0/XsnJtr2mPff79jjPKHG+jwXW2usz/MmIsdT+V7l3wmPozTc+Pn5oXv37khPT69qM5vNSE9PR3Jycq33SU5OtjoeAL799ts6j3cqX1/g2Wfl15ISOcDYbJZfS0ost/v5AVOmAKGhcuBZUZE8rqhIXg8Lk7fXZyCaXm/bY/r6OvY4T6ixPs/F1ho5SJBILZXvVf6d8DxOn7t1DStWrBD+/v5i+fLl4tChQ2L06NEiIiJCZGZmCiGEeOihh8SUKVOqjv/++++Fr6+vePXVV8Uvv/wiZs2apXYquBCWdW58fOQaNz4+8vqrr1of54w1ElSuDePuNXKdGyLt4To3XsujpoIDwKJFi/DKK68gMzMT3bp1w8KFC5GUlAQAGDBgAFq2bInly5dXHb9q1SpMnz4dJ06cQNu2bTFv3jzccccdNn0vh04Fr66iQs7SOXlSjvm4//66Vyh29OqWKlf1dfcauUIxkfZwhWKvVJ/Pb7cIN67ktHBDRERETuMx69wQERERORrDDREREWkKww0RERFpCsMNERERaQrDDREREWkKww0RERFpCsMNERERaQrDDREREWkKww0RERFpSi37A2hb5YLMeXl5iishIiIiW1V+btuysYLXhZv8/HwAQEJCguJKiIiIqL7y8/MRHh5+1WO8bm8ps9mMc+fOITQ0FDqdTnU5V5WXl4eEhAScPn2a+2C5Gb427omvi/via+OePOl1EUIgPz8fTZo0gf4am5V6Xc+NXq9Hs2bNVJdRL2FhYW7/S+et+Nq4J74u7ouvjXvylNflWj02lTigmIiIiDSF4YaIiIg0heHGjfn7+2PWrFnw9/dXXQpdga+Ne+Lr4r742rgnrb4uXjegmIiIiLSNPTdERESkKQw3REREpCkMN0RERKQpDDdERESkKQw3bmDu3Lno2bMnQkNDERMTgyFDhuDw4cNWx5SUlGDs2LFo1KgRQkJC8Kc//QlZWVmKKvYOS5YsQZcuXaoWt0pOTsY333xTdTtfE/fw0ksvQafTYcKECVVtfG3UmD17NnQ6ndWlQ4cOVbfzdVHr7NmzePDBB9GoUSMEBgaic+fO2LVrV9XtQgjMnDkT8fHxCAwMREpKCn777TeFFduP4cYNbNu2DWPHjsUPP/yAb7/9FuXl5fjjH/+IwsLCqmOefvppfPXVV1i1ahW2bduGc+fOYejQoQqr1r5mzZrhpZdewu7du7Fr1y784Q9/wD333IOff/4ZAF8Td/DTTz/h7bffRpcuXaza+dqoc8MNN+D8+fNVl++++67qNr4u6ly+fBl9+vSBwWDAN998g0OHDuG1115DZGRk1THz5s3DwoULkZaWhp07dyI4OBiDBg1CSUmJwsrtJMjtXLhwQQAQ27ZtE0IIkZubKwwGg1i1alXVMb/88osAIDIyMlSV6ZUiIyPFu+++y9fEDeTn54u2bduKb7/9VvTv31889dRTQgi+X1SaNWuW6Nq1a6238XVRa/LkyaJv37513m42m0VcXJx45ZVXqtpyc3OFv7+/+PTTT11RokOx58YNGY1GAEBUVBQAYPfu3SgvL0dKSkrVMR06dEDz5s2RkZGhpEZvYzKZsGLFChQWFiI5OZmviRsYO3Ys7rzzTqvXAOD7RbXffvsNTZo0wXXXXYe//OUvOHXqFAC+Lqp9+eWX6NGjB+677z7ExMQgMTERS5curbr9+PHjyMzMtHp9wsPDkZSU5JGvD8ONmzGbzZgwYQL69OmDTp06AQAyMzPh5+eHiIgIq2NjY2ORmZmpoErvceDAAYSEhMDf3x9jxozBmjVr0LFjR74miq1YsQJ79uzB3Llza9zG10adpKQkLF++HOvXr8eSJUtw/Phx9OvXD/n5+XxdFPv999+xZMkStG3bFhs2bMATTzyBJ598Eh988AEAVL0GsbGxVvfz1NfH63YFd3djx47FwYMHrc5Tkzrt27fHvn37YDQasXr1aowYMQLbtm1TXZZXO336NJ566il8++23CAgIUF0OVXP77bdX/btLly5ISkpCixYt8NlnnyEwMFBhZWQ2m9GjRw/MmTMHAJCYmIiDBw8iLS0NI0aMUFyd47Hnxo2MGzcOX3/9NbZs2YJmzZpVtcfFxaGsrAy5ublWx2dlZSEuLs7FVXoXPz8/tGnTBt27d8fcuXPRtWtXvPHGG3xNFNq9ezcuXLiAG2+8Eb6+vvD19cW2bduwcOFC+Pr6IjY2lq+Nm4iIiEC7du1w9OhRvmcUi4+PR8eOHa3arr/++qrThpWvwZWz1zz19WG4cQNCCIwbNw5r1qzB5s2b0apVK6vbu3fvDoPBgPT09Kq2w4cP49SpU0hOTnZ1uV7NbDajtLSUr4lCt956Kw4cOIB9+/ZVXXr06IG//OUvVf/ma+MeCgoKcOzYMcTHx/M9o1ifPn1qLDFy5MgRtGjRAgDQqlUrxMXFWb0+eXl52Llzp2e+PqpHNJMQTzzxhAgPDxdbt24V58+fr7oUFRVVHTNmzBjRvHlzsXnzZrFr1y6RnJwskpOTFVatfVOmTBHbtm0Tx48fF/v37xdTpkwROp1ObNy4UQjB18SdVJ8tJQRfG1WeeeYZsXXrVnH8+HHx/fffi5SUFBEdHS0uXLgghODrotKPP/4ofH19xYsvvih+++038fHHH4ugoCDxz3/+s+qYl156SURERIgvvvhC7N+/X9xzzz2iVatWori4WGHl9mG4cQMAar28//77VccUFxeLv/71ryIyMlIEBQWJe++9V5w/f15d0V5g1KhRokWLFsLPz080btxY3HrrrVXBRgi+Ju7kynDD10aN1NRUER8fL/z8/ETTpk1FamqqOHr0aNXtfF3U+uqrr0SnTp2Ev7+/6NChg3jnnXesbjebzWLGjBkiNjZW+Pv7i1tvvVUcPnxYUbUNoxNCCJU9R0RERESOxDE3REREpCkMN0RERKQpDDdERESkKQw3REREpCkMN0RERKQpDDdERESkKQw3REREpCkMN0RERKQpDDdERESkKQw3REREpCkMN0REVygrK1NdAhE1AMMNEbmNli1bYsGCBVZt3bp1w+zZswEAOp0Ob7/9NgYPHoygoCBcf/31yMjIwNGjRzFgwAAEBwejd+/eOHbsWNX9H374YQwZMsTqMSdMmIABAwZUXR8wYADGjRuHCRMmIDo6GoMGDXLSMyQiV2C4ISKP8vzzz2P48OHYt28fOnTogP/7v//D448/jqlTp2LXrl0QQmDcuHH1ftwPPvgAfn5++P7775GWluaEyonIVXxVF0BEVB8jR47En//8ZwDA5MmTkZycjBkzZlT1tjz11FMYOXJkvR+3bdu2mDdvnkNrJSI12HNDRB6lS5cuVf+OjY0FAHTu3NmqraSkBHl5efV63O7duzumQCJSjuGGiNyGXq+HEMKqrby83Oq6wWCo+rdOp6uzzWw22/yYABAcHNyAyonInTDcEJHbaNy4Mc6fP191PS8vD8ePH3foYwLAvn37GvSYROTeGG6IyG384Q9/wEcffYTt27fjwIEDGDFiBHx8fBr8mLt27cKHH36I3377DbNmzcLBgwcdVDERuSOGGyJyG1OnTkX//v0xePBg3HnnnRgyZAhat27doMccNGgQZsyYgUmTJqFnz57Iz8/H8OHDHVQxEbkjnbjyZDQRERGRB2PPDREREWkKww0RERFpCsMNERERaQrDDREREWkKww0RERFpCsMNERERaQrDDREREWkKww0RERFpCsMNERERaQrDDREREWkKww0RERFpyv8Dk1noLeND9r0AAAAASUVORK5CYII=\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.model_selection import train_test_split"
      ],
      "metadata": {
        "id": "QEgr_H7MjUn0"
      },
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Pisahkan data training dan data test\n",
        "x_train,x_test,y_train,y_test=train_test_split(df[['umur']],df.membeli_asuransi,train_size=0.9)\n"
      ],
      "metadata": {
        "id": "DMGnbvPbjbWT"
      },
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Menampilkan Nilai Variabel Test\n",
        "x_test"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 143
        },
        "id": "rDSk731okApI",
        "outputId": "64f6320a-ba76-444b-8287-bcafc7828eed"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "    umur\n",
              "22    40\n",
              "16    25\n",
              "6     55"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-51b58ce4-9cf1-45a4-967b-579504e46de8\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>umur</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>22</th>\n",
              "      <td>40</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>16</th>\n",
              "      <td>25</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>55</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-51b58ce4-9cf1-45a4-967b-579504e46de8')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-51b58ce4-9cf1-45a4-967b-579504e46de8 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-51b58ce4-9cf1-45a4-967b-579504e46de8');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x_train"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 802
        },
        "id": "hmI0l9yckXku",
        "outputId": "8efb2edb-a9f1-4036-c5af-9269b41ab95c"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "    umur\n",
              "24    50\n",
              "17    58\n",
              "10    18\n",
              "23    45\n",
              "8     62\n",
              "1     25\n",
              "9     61\n",
              "13    29\n",
              "11    28\n",
              "15    55\n",
              "0     22\n",
              "5     56\n",
              "26    23\n",
              "4     46\n",
              "7     60\n",
              "21    26\n",
              "19    18\n",
              "18    19\n",
              "3     52\n",
              "20    21\n",
              "14    49\n",
              "12    27\n",
              "25    54\n",
              "2     47"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-92d7247b-8525-41d1-af36-293c67750701\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>umur</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>24</th>\n",
              "      <td>50</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>17</th>\n",
              "      <td>58</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>10</th>\n",
              "      <td>18</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>23</th>\n",
              "      <td>45</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8</th>\n",
              "      <td>62</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>25</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9</th>\n",
              "      <td>61</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>13</th>\n",
              "      <td>29</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>11</th>\n",
              "      <td>28</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>15</th>\n",
              "      <td>55</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>22</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>56</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>26</th>\n",
              "      <td>23</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>46</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>60</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>21</th>\n",
              "      <td>26</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>19</th>\n",
              "      <td>18</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>18</th>\n",
              "      <td>19</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>52</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>20</th>\n",
              "      <td>21</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>14</th>\n",
              "      <td>49</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>12</th>\n",
              "      <td>27</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25</th>\n",
              "      <td>54</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>47</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-92d7247b-8525-41d1-af36-293c67750701')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-92d7247b-8525-41d1-af36-293c67750701 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-92d7247b-8525-41d1-af36-293c67750701');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Import library Regresi Logistik\n",
        "from sklearn.linear_model import LogisticRegression"
      ],
      "metadata": {
        "id": "qZcsnD_akgDI"
      },
      "execution_count": 9,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Membuat Model\n",
        "model=LogisticRegression()"
      ],
      "metadata": {
        "id": "etTSCkx9k0A_"
      },
      "execution_count": 10,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Model melakukan Training\n",
        "model.fit(x_train,y_train)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 74
        },
        "id": "JcC78q81k6O5",
        "outputId": "c3665bce-0e1a-415e-9e2e-b551172f23c0"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "LogisticRegression()"
            ],
            "text/html": [
              "<style>#sk-container-id-1 {color: black;background-color: white;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-1\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>LogisticRegression()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-1\" type=\"checkbox\" checked><label for=\"sk-estimator-id-1\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">LogisticRegression</label><div class=\"sk-toggleable__content\"><pre>LogisticRegression()</pre></div></div></div></div></div>"
            ]
          },
          "metadata": {},
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Prediksi\n",
        "model.predict(x_test)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yuHFIcMVlJCp",
        "outputId": "0a422969-66c7-4a50-a9f3-7aebeda950f4"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([0, 0, 1])"
            ]
          },
          "metadata": {},
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Mengecek keakuratan model\n",
        "model.score(x_test,y_test)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-NtS2PaQlRJr",
        "outputId": "252f415c-4da1-4e0f-8be9-9c8519e30dc1"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0.0"
            ]
          },
          "metadata": {},
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Prediksi jika umur =60 Tahun\n",
        "model.predict([[60]])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eOhi1sAEll7p",
        "outputId": "d8f58526-c376-4273-9010-f0a65a52fac0"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.9/dist-packages/sklearn/base.py:439: UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names\n",
            "  warnings.warn(\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([1])"
            ]
          },
          "metadata": {},
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Prediksi jika umur =1 Tahun\n",
        "model.predict([[1]])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "icMLoHVslxjO",
        "outputId": "9f67a5ee-c0b2-4ac9-894f-f1f8df6f93e6"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.9/dist-packages/sklearn/base.py:439: UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names\n",
            "  warnings.warn(\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([0])"
            ]
          },
          "metadata": {},
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Apabila hasilnya=1 maka artinya orang tersebut membeli asuransi,namun apabila hasilnya =0 berarti tidak membeli asuransi"
      ],
      "metadata": {
        "id": "pB04xlQel7sF"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### **Kesimpulan**\n",
        "\n",
        "\n",
        "Dari implementasi diatas, bahwa model sudah belajar berdasarkan dataset\n",
        "dataasuransi.csv. Dan dilakukan input apabila umur 60, model menetapkan\n",
        "bahwa pada umur tersebut orang mau membeli asuransi. Sehingga model\n",
        "ini dapat menjadi acuan untuk perusahaan asuransi dalam menetapkan\n",
        "pasarnya ke umur yang mendekati angka 60-an. Tapi dalam praktek\n",
        "sebagai pendukung keputusan perusahaan, dibutuhkan dataset yang lebih\n",
        "kompleks.\n",
        "\n"
      ],
      "metadata": {
        "id": "Ei3Mp1uDmLM2"
      }
    }
  ]
}