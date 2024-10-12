import tkinter as tk
import PySimpleGUI as sg
import mysql.connector

# Connect to the MySQL database


def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="h@9a_asaas1AySDZYPHBUwVg4Z7abnCZ",
        database="precobom_db"
    )

# Function to add product


def add_product(name, quantity, price):
    conn = connect_db()
    cursor = conn.cursor()
    query = "INSERT INTO produtos (nome, quantidade, preco) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, quantity, price))
    conn.commit()
    cursor.close()
    conn.close()

# Function to update product


def update_product(product_id, name, quantity, price):
    conn = connect_db()
    cursor = conn.cursor()
    query = "UPDATE produtos SET nome = %s, quantidade = %s, preco = %s WHERE id = %s"
    cursor.execute(query, (name, quantity, price, product_id))
    conn.commit()
    cursor.close()
    conn.close()

# Function to delete product


def delete_product(product_id):
    conn = connect_db()
    cursor = conn.cursor()
    query = "DELETE FROM produtos WHERE id = %s"
    cursor.execute(query, (product_id,))
    conn.commit()
    cursor.close()
    conn.close()

# Function to display inventory


def list_products():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


# Layout of the graphical interface
layout = [
    [sg.Text("Controle de Estoque - Mercearia Preço Bom",
             size=(80, 1), justification="center", font=("Helvetica", 24))],
    [sg.Text("Nome do Produto", size=(25, 1), font=("Helvetica", 18)),
     sg.InputText(key="name", size=(30, 1), font=("Helvetica", 18))],
    [sg.Text("Quantidade", size=(25, 1), font=("Helvetica", 18)), sg.InputText(
        key="quantity", size=(30, 1), font=("Helvetica", 18))],
    [sg.Text("Preço (R$)", size=(25, 1), font=("Helvetica", 18)),
     sg.InputText(key="price", size=(30, 1), font=("Helvetica", 18))],
    [sg.Button("Adicionar Produto", font=("Helvetica", 18)),
     sg.Button("Atualizar Produto", font=("Helvetica", 18)),
     sg.Button("Excluir Produto", font=("Helvetica", 18)),
     sg.Button("Visualizar Estoque", font=("Helvetica", 18))],
    [sg.Text("ID do Produto (para Atualizar/Excluir)", size=(60, 1), font=("Helvetica", 18)),
     sg.InputText(key="product_id", size=(30, 1), font=("Helvetica", 18))],
    [sg.Multiline(size=(90, 20), key='-OUTPUT-',
                  disabled=True, font=("Helvetica", 18))]
]

# Creating the window
window = sg.Window(
    "Sistema de Controle de Estoque - Mercearia Mercearia Preço Bom", layout, size=(1200, 800))

# Event loop for the graphical interface
while True:
    event, values = window.read()

    # Close the window
    if event == sg.WINDOW_CLOSED:
        break

    # Add product
    if event == "Adicionar Produto":
        name = values["name"]
        quantity = int(values["quantity"])
        price = float(values["price"])
        add_product(name, quantity, price)

        # Calculate total value if quantity is greater than 1
        if quantity > 1:
            total_value = quantity * price
            window['-OUTPUT-'].update(
                f"Produto '{name}' adicionado com sucesso! Valor total: R$ {total_value:.2f}\n")
        else:
            window['-OUTPUT-'].update(
                f"Produto '{name}' adicionado com sucesso!\n")

    # Update product
    if event == "Atualizar Produto":
        product_id = int(values["product_id"])
        name = values["name"]
        quantity = int(values["quantity"])
        price = float(values["price"])
        update_product(product_id, name, quantity, price)
        window['-OUTPUT-'].update(
            f"Produto com ID {product_id} atualizado com sucesso!\n")

    # Delete product
    if event == "Excluir Produto":
        product_id = int(values["product_id"])
        delete_product(product_id)
        window['-OUTPUT-'].update(
            f"Produto com ID {product_id} excluído com sucesso!\n")
        # Update the product list to show the changes
        products = list_products()
        output = "Estoque Atual:\n"
        for product in products:
            price_total = product[2] * product[3]  # quantity * price
            output += f"ID: {product[0]} | Nome: {product[1]} | Quantidade: {product[2]} | Preço: R$ {
                product[3]:.2f} | Preço total do Produto: R$ {price_total:.2f}\n"
        window['-OUTPUT-'].update(output)

    # List products
    if event == "Visualizar Estoque":
        products = list_products()
        output = "Estoque Atual:\n"
        for product in products:
            price_total = product[2] * product[3]  # quantity * price
            output += f"ID: {product[0]} | Nome: {product[1]} | Quantidade: {product[2]} | Preço: R$ {
                product[3]:.2f} | Preço total do Produto: R$ {price_total:.2f}\n"
        window['-OUTPUT-'].update(output)

# Close the window
window.close()
