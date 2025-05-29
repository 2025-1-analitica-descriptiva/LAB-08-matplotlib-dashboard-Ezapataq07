# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

def create_docs_folder():
    """
    Crea la carpeta 'docs' si no existe.
    """
    if not os.path.exists('docs'):
        os.makedirs('docs')

def load_data():
    df = pd.read_csv('files/input/shipping-data.csv')
    return df

def create_visual_for_shipping_per_warehouse(df):
    df = df.copy()
    plt.figure()
    counts = df.Warehouse_block.value_counts()
    counts.plot.bar(
        title='Shipping per Warehouse',
        xlabel='Warehouse Block',
        ylabel='Record Count',
        color='tab:blue',
        fontsize=8
    )
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.tight_layout()
    plt.savefig('docs/shipping_per_warehouse.png')
    plt.plot()
    return counts

def create_visual_for_mode_of_shipment(df):
    df = df.copy()
    plt.figure()
    counts = df.Mode_of_Shipment.value_counts()
    counts.plot.pie(
        title='Mode of Shipment',
        wedgeprops={'width': 0.35},
        colors=['tab:blue', 'tab:orange', 'tab:green'],
        # fontsize=8
    )
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.tight_layout()
    plt.savefig('docs/mode_of_shipment.png')
    plt.plot()
    return counts

def create_visual_for_average_customer_rating(df):
    df = df.copy()
    plt.figure()
    df = df[['Mode_of_Shipment','Customer_rating']].groupby('Mode_of_Shipment').describe()
    df.columns = df.columns.droplevel()
    df = df[['mean','min','max']]
    plt.barh(
        y=df.index.values,
        width=df['max'].values - 1,
        left=df['min'].values,
        height=0.9,
        color='lightgrey',
        alpha=0.8,
    )
    colors = [
        'tab:green' if x >= 3 else 'tab:orange' for x in df['mean'].values
    ]
    plt.barh(
        y=df.index.values,
        width=df['mean'].values - 1,
        left=df['min'].values,
        height=0.5,
        color=colors,
        alpha=1.0,
    )
    plt.title('Average Customer Rating by Mode of Shipment')
    plt.gca().spines['left'].set_color('grey')
    plt.gca().spines['bottom'].set_color('grey')
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.tight_layout()
    plt.savefig('docs/average_customer_rating.png')
    plt.plot()
    return df

def create_visual_for_weight_distribution(df):
    df = df.copy()
    plt.figure()
    df.Weight_in_gms.plot.hist(
        title='Shipped Weight Distribution',
        # bins=30,
        color='tab:orange',
        edgecolor='white',
    )
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.tight_layout()
    plt.savefig('docs/weight_distribution.png')
    plt.plot()
    return df

def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
    create_docs_folder()
    df = load_data()
    create_visual_for_shipping_per_warehouse(df)
    create_visual_for_mode_of_shipment(df)
    create_visual_for_average_customer_rating(df)
    create_visual_for_weight_distribution(df)

    
    return df

pregunta_01()

