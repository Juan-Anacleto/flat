import flet as ft

def cadastro(page: ft.Page):

    # Função para navegar para a página de cadastro
    def go_to_login(e):
        page.go("/login")  # Corrigido para usar apenas "/cadastro"

    # Configurações de estilo
    page.bgcolor = "#AC93A6"
    
    # Definição dos componentes
    setinha = ft.Icon(name=ft.icons.ARROW_BACK, size=30, color=ft.colors.WHITE)
    atrasdoP = ft.Image(src="imgs/Vector_verde_escuro.png", width=200, height=190)
    P_roxo = ft.Image(src="imgs/Proxo.png", width=200, height=190)
    title = ft.Text("Cadastre-se", font_family="PT sans", size=35, weight="bold")
    nome = ft.TextField(label="Nome Completo", color="white", bgcolor="#AC93A6", border_color="#AC93A6", width=600, border_radius=20)
    email = ft.TextField(label="E-mail", color="white", password=True, bgcolor="#AC93A6", border_color="#AC93A6", width=600, border_radius=20)
    senha = ft.TextField(label="Senha", color="white", password=True, bgcolor="#AC93A6", border_color="#AC93A6", width=600, border_radius=20)
    button = ft.ElevatedButton("Cadastrar", bgcolor="#AC93A6", color="black")
    
    # Função de evento para o botão "Entrar"
    def on_login(e):
        # Aqui você pode adicionar a lógica para o login
        print("Entrar clicado")  # Placeholder para lógica de login

    # Botão de cadastro
    txt_cadastro = ft.ElevatedButton("Já tenho Cadastro", color="#AC93A6", on_click=go_to_login)

    # Retorno da view
    return ft.View(
        route="/login",
        bgcolor = "#AC93A6",
        controls=[
            ft.Container(
                content=ft.Column(
                    [
                        ft.Container(
                            setinha,
                            bgcolor="#87A7A2",
                            border_radius=80,
                            padding=30
                        ),
                        ft.Container(
                            content=ft.Stack([
                                atrasdoP,
                                ft.Container(
                                    content=ft.Column([P_roxo])
                                )
                            ]),
                            alignment=ft.alignment.center,
                            width="100%"
                        ),
                        ft.Container(
                            content=ft.Column(
                                [
                                    title,
                                    nome,
                                    email,
                                    senha,
                                    button,
                                    txt_cadastro
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                            ),
                            alignment=ft.alignment.center,
                            border_radius=ft.border_radius.only(top_left=150, top_right=150),
                            padding=70,
                            bgcolor="white", 
                            height=500,
                            width="100%"
                        ),
                    ]
                ),
                border=ft.border.all(0, ft.colors.BLACK),
            ),
        ],
    )

        
