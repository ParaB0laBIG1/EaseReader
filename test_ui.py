from flet import *



class BookLoader(UserControl):
    def __init__(self, page: Page):
        super().__init__()

        self.favorites_button = IconButton(
            icon=icons.STAR_BORDER, tooltip="Add to Favorites"
        )
        
        self.put_book = IconButton(
            icon=icons.ACCESS_TIME, tooltip="Read later"
        )

        self.read_the_book = IconButton(
            icon=icons.CHECK_CIRCLE_OUTLINED, tooltip="The book is read"
        )

        self.delete_book = PopupMenuItem(
                icon=icons.DELETE, text="Delete book"
            )

        self.edit_book = PopupMenuItem(
            icon=icons.EDIT, text="Edit"
        )

        self.others_button = PopupMenuButton(
            items=[
                self.delete_book,
                self.edit_book
            ]
        )

        # self.book_loader_container = Container(
                #     alignment=alignment.center,
                #     width=350,height=200,
                #     bgcolor=colors.BLUE_GREY_700,
                #     border_radius=border_radius.all(5),
                #     content=Row(
                #         alignment=alignment.top_left,spacing=0,
                #         controls=[

                #             Container(
                #                 width=110,height=200,
                #             ),
                            
                #             Container(
                #                 width=240,height=160,
                #                 content=Column(spacing=3,
                #                     controls=[
                #                         Text(  # Name book
                #                             value=self.fb_manager.get_name_book(file_path=file_path),
                #                             weight="bold",
                #                             size=20
                #                         ),
                                        
                #                         Text( # Name author
                #                             value=self.fb_manager.get_author_name(file_path=file_path),
                #                             size=13,
                #                             color="grey"
                #                         ),

                #                         Container(
                #                             width=230, height=120, alignment=alignment.bottom_left,
                #                             content=Row(
                #                                 controls=[
                #                                     self.favorites_button,
                #                                     self.put_book,
                #                                     self.read_the_book,
                #                                     self.others_button
                #                                 ]
                #                             )
                #                         )

                #                     ]
                #                 )
                #             )
                #         ]
                #     )
                # )
            

    def build(self):
        return self.book_loader_container