from flet import (
    Page,
    UserControl,
    View,
    app
)

from src.ui.login.login_page import LoginPage

# how to use table https://github.com/brandonegg/tempProbe/blob/e8febb71c5/temp_monitor/main.py


class App(UserControl):
    def __init__(self, page):
        super().__init__()
        print("init app")
        self.page = page
        self.page.title = 'ZCL'
        self.page.window_min_width = 800
        self.page.window_min_height = 640
        self.page.expand = True
        self.page.padding = 0
        self.page.update()
        self.page.on_route_change = self.on_route_change
        self.page.go('/')
        self.page.update()

    # def build(self):
    #     print("build app")
    #     self.page.on_route_change = self.on_route_change
    #     self.page.go('/')
    #     return self.page

    def on_route_change(self, route):
        page_route = {
            "/": LoginPage,
            "/login": LoginPage,
            "/device": LoginPage,
            "/group": LoginPage,
            "/schedule": LoginPage,
        }[self.page.route](self.page)

        self.page.views.clear()
        # set view fill with screen no spacing
        self.page.views.append(View(route, [page_route],
                                    padding=0,
                                    spacing=0))


async def main(page: Page):
    await page.add_async(App(page))


app(target=App, assets_dir="assets")

# class App(UserControl):
#
#     def __init__(self, page: Page):
#         super().__init__()
#         self.page = page
#         self.page.title = 'ZCL'
#         self.page.window_min_width = 800
#         self.page.window_min_height = 640
#         self.page.expand = True
#         page.padding = 0
#         self.init()
#
#     def init(self):
#         self.page.on_route_change = self.on_route_change
#         self.page.go('/')
#
#     def on_route_change(self, route):
#         page_route = {
#             "/": LoginPage,
#             "/login": LoginPage,
#             "/device": LoginPage,
#             "/group": LoginPage,
#             "/schedule": LoginPage,
#         }[self.page.route](self.page)
#
#         self.page.views.clear()
#         # set view fill with screen no spacing
#         self.page.views.append(View(route, [page_route],
#                                     padding=0,
#                                     spacing=0))
#
#
# # asyncio.run(app(target=App))
# if __name__ == "__main__":
#     app(target=App, assets_dir="assets")
