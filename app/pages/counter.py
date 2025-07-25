import flet as ft # type: ignore
from fletx.core import ( # type: ignore
    FletXPage
)
from fletx.navigation import navigate # type: ignore

from ..controllers.counter import CounterController
from ..components import MyReactiveText


class CounterPage(FletXPage):
    ctrl = CounterController()
    
    def build(self):
        return ft.Column(
            spacing = 10,
            expand = True,
            alignment = ft.MainAxisAlignment.CENTER,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            controls = [
                ft.Container(
                    height = 100
                ),
                ft.Image(
                    src = 'logo.png',
                    fit = ft.ImageFit.CONTAIN,
                    width = 120,
                    height = 120
                ),
                ft.Text('🚀 powered by FletX 0.1.3',color = ft.Colors.GREY_600),
                ft.Text('Python version 3.12', color = ft.Colors.GREY_600),
                ft.Container(
                    expand = True,
                    alignment = ft.alignment.center,
                    content = ft.Column(
                        alignment = ft.MainAxisAlignment.CENTER,
                        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                        controls = [
                            ft.Text(
                                "My RoutingApp Counter",
                                size = 20,
                                weight = ft.FontWeight.BOLD
                            ),
                            MyReactiveText(
                                value = '0',
                                rx_text = self.ctrl.count, # Auto update when count changes
                                size = 100, 
                                weight = ft.FontWeight.BOLD
                            ),
                            ft.ElevatedButton(
                                "Increment",
                                on_click=lambda e: self.ctrl.count.increment()  # Auto UI update
                            ),
                            ft.ElevatedButton(
                                "See page 1",
                                on_click=lambda e: navigate('/page1')  # Auto UI update
                            )
                        ]
                    )
                ),
                ft.Container(
                    height = 100,
                    content = ft.Text('Thanks for choosing FletX'),
                ),
            ]
        )