import asyncio

from flet import *

from src.constants.constants import *
from src.database.databases import User
from src.ui.login.login_viewmodel import LoginViewModel


class LoginPage(Container):

    def on_ui_update(self, message):
        print("update ui= {}".format(message))
        print("serverIP= {}".format(self.view_model.serverIP))
        self.server_textfield.value = self.view_model.serverIP
        self.update()

    def did_mount(self):
        print("mount")
        self.page.pubsub.subscribe(self.on_ui_update)
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        self.loop.run_until_complete(self.view_model.searchGateway())

    def will_unmount(self):
        print("unmount")
        self.page.pubsub.unsubscribe_all()
        if self.loop:
            self.loop.close()
            self.loop = None

    def _build(self):
        page.padding = 0
        self.expand = True
        self.bgcolor = colors.WHITE
        self.alignment = alignment.center
        self.error_border = border.all(width=1, color='red')
        page.on_error = lambda e: print("Page error:", e.data)

        self.username_box = Container(
            margin=margin.only(left=10, right=10),
            alignment=alignment.center,
            content=TextField(
                border=InputBorder.NONE,
                # content_padding=padding.only(top=0, bottom=0, right=10, left=10),
                hint_style=TextStyle(
                    size=12, color='#858796'
                ),
                hint_text='Enter user name',
                cursor_color=cl_yellow,
                text_style=TextStyle(
                    size=14,
                    color='black',
                ),
                value='delight',
                disabled=True,
            ),
            border=border.only(bottom=BorderSide(width=1, color=colors.BLACK12)),
        )
        self.password_box = Container(
            margin=margin.only(left=10, right=10),
            alignment=alignment.center,
            content=TextField(
                border=InputBorder.NONE,
                # content_padding=padding.only(top=0, bottom=0, right=10, left=10),
                hint_style=TextStyle(
                    size=12, color='#858796'
                ),
                hint_text='Enter password',
                cursor_color=cl_yellow,
                text_style=TextStyle(
                    size=14,
                    color='black',
                ),
                password=True,
                can_reveal_password=True,
            ),
            # border_radius=30,
            border=border.only(bottom=BorderSide(width=1, color=colors.BLACK12)),
        )
        self.server_textfield = TextField(
                        expand=True,
                        border=InputBorder.NONE,
                        # content_padding=padding.only(top=0, bottom=0, right=10, left=10),
                        hint_style=TextStyle(
                            size=12, color='#858796'
                        ),
                        hint_text='Enter server IP',
                        cursor_color=cl_yellow,
                        text_style=TextStyle(
                            size=14,
                            color='black',
                        ),
                        value=self.view_model.serverIP
                    )
        self.server_box = Container(
            margin=margin.only(left=10, right=10),
            padding=padding.only(right=15),
            alignment=alignment.center,
            content=Row(
                controls=[
                    self.server_textfield,
                    ProgressRing(width=15, height=15, color=cl_yellow, ),
                ]
            ),
            border=border.only(bottom=BorderSide(width=1, color=colors.BLACK12)),
        )

        self.login_box = Container(
            margin=Margin(left=10, right=10, top=20, bottom=0),
            content=Row(
                alignment=MainAxisAlignment.SPACE_AROUND,
                controls=[
                    Text('Sign in', weight=FontWeight.BOLD, style=TextThemeStyle.TITLE_LARGE),
                    Container(
                        content=IconButton(icon=icons.ARROW_CIRCLE_RIGHT, icon_size=60,
                                           on_click=lambda _: (
                                               User.saveUser(password='345678', token='33434', ipaddress='localhost'),
                                               self.page.go('/group')
                                           )),
                    )
                ]
            )
        )

        self.content = Row(
            alignment=MainAxisAlignment.CENTER,
            vertical_alignment=CrossAxisAlignment.CENTER,
            controls=[
                Stack(
                    expand=True | 3,
                    controls=[
                        Container(
                            expand=True,
                            bgcolor=cl_yellow
                        ),
                        Container(
                            alignment=alignment.center,
                            content=Image(
                                src=f"/images/login_top.webp",
                                width=300,
                                height=150,
                                fit=ImageFit.COVER
                            )
                        )
                    ]
                ),
                Column(
                    expand=2,
                    alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    controls=[
                        Text(
                            value="Welcome Back!",
                            size=16,
                            color='black',
                            text_align=TextAlign.CENTER
                        ),
                        self.username_box,
                        self.password_box,
                        self.server_box,
                        self.login_box,
                        Row(
                            alignment=MainAxisAlignment.END,
                            controls=[
                                Container(
                                    padding=padding.only(bottom=0),
                                    margin=margin.only(right=20),
                                    content=
                                    Text(
                                        value='Forgot password?',
                                        style=TextThemeStyle.LABEL_SMALL
                                    ),
                                    border=border.only(bottom=BorderSide(width=1, color=colors.BLACK)),
                                )
                            ]
                        )
                    ]
                ),
            ]
        )
        return self.content

    def __init__(self, page: Page):
        super().__init__()
        print("init login page")
        self.view_model = LoginViewModel(page)
        self.loop = None
        self.page = page
