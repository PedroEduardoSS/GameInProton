from nicegui import ui
from scraping.scrap import search_games

with ui.column().classes("w-full"):
    game_name = ui.input(label='Game name', placeholder='start typing')
    result_list = ui.list().classes("w-full")

    def update_list():
        results = search_games(game_name.value)
        result_list.clear()
        ui.notify("Loading")
        with result_list:
            for name, link in results:
                with ui.row():
                    ui.link(f"{name}", link)

    ui.button("Search", on_click=update_list)

ui.run()