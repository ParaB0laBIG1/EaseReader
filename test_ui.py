from flet import *


def main(page: Page):
    # window settings

    page.window_width = 800
    page.window_height = 600
    page.window_center()
    page.title = "EaseReader"
    
    def items(count):
        items = []
        for i in range(1, count + 1):
            items.append(
                Container(
                    content=Text(value=str(i)),
                    alignment=alignment.center,
                    width=300,
                    height=100,
                    bgcolor=colors.AMBER,
                    border_radius=border_radius.all(5),
                )
            )
        return items
    
    row = Row(
        wrap=True,
        spacing=10,
        run_spacing=10,
        controls=items(100),
        width=page.window_width,
    )

    page.add(
        Column(
            [
                Text(
                    "Change the row width to see how child items wrap onto multiple rows:"
                ),
            ]
        ),
        row,
    )

    page.update()


if __name__ == '__main__':

    app(target=main)