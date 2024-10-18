import flet as ft
from login import login
from cadastro import cadastro


def main(page: ft.Page):

    # Configurando a URL para suportar diferentes rotas
    page.title = "Navegação entre páginas"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Função que altera a visualização da página conforme a rota
    def route_change(route):
        page.views.clear()  # Limpa a visualização atual

        if page.route == "/login" or page.route == "/":
            page.views.append(login(page))  # Mostra a página de login

        elif page.route == "/cadastro":
            page.views.append(cadastro(page))  # Mostra a página de cadastro


        # Atualiza a página
        page.update()

    # Escuta as mudanças de rota
    page.on_route_change = route_change

    # Define a rota inicial para "/login"
    page.go("/login")

# Inicia o app Flet
ft.app(target=main)
