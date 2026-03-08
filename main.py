import asyncio
from nicegui import ui
from classes import Airplane
from ui_elements import add, create_crew_table, create_table

p1 = Airplane()


def create_ui() -> None:
    """Builds the entire NiceGUI interface."""

    with ui.card().tight() as card:
        with ui.card_section().classes('card'):

            # altitude display
            height_label = ui.label("Plane's current height in meters:").classes('label')
            height_counter = ui.label().classes('label')

            # altitude slider (bound to airplane altitude)
            height = ui.slider(min=p1.z, max=1000, value=p1.z).classes('slider')
            height.bind_value_from(p1, 'z')
            height_counter.bind_text_from(height, 'value')

            # flight control buttons
            ui.button("START", on_click=lambda: asyncio.create_task(p1.start(height_label)),color="#87CEED").classes('button')

            ui.button("LAND", on_click=lambda: asyncio.create_task(p1.land  (height_label)),color="#87CEED").classes('button')

            # passenger count display
            passenger_count_label = ui.label(f"Passenger count: {p1.passenger_count}").classes('label')
            passenger_count_label.bind_text_from(p1, 'passenger_count')

            # crew table
            create_crew_table()

            # registration dialog
            with ui.dialog() as dialog:
                with ui.card().classes('card'):
                    first_name = ui.input('Firstname', validation={'Too short': lambda v: len(v) > 2})
                    last_name = ui.input('Lastname', validation={'Too short': lambda v: len(v) > 2})
                    age = ui.number('Age', validation={'Invalid': lambda v: v > 0})
                    row = ui.select(list(range(1, 11)), label="Row").classes('w-64')
                    seat = ui.select(['A', 'B', 'C', 'D', 'E', 'F'], label="Seat").classes('w-64')
                    luggage = ui.select(["small (0-5kg)", "medium (6-10kg)", "large (11-25kg)"], label="Luggage").classes('w-64')
                    checked = ui.select(["yes", "no"], label="Checked").classes('w-64')

                    with ui.row():
                        ui.button("add", on_click=lambda: add(p1, first_name, last_name, age, row, seat, luggage, checked),color="#87CEED").classes('button')
                        ui.button('Exit', on_click=dialog.close, color="red").classes('button')

            ui.button('Register', on_click=dialog.open, color="#87CEED").classes('button')

            ui.button("show Registration", on_click=create_table, color="#87CEED").classes('button')


# custom CSS
ui.add_head_html("""
<style>
    body {
        background-image: url("https://wallpaperaccess.com/full/1264507.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 15px;
        padding-top: 15px;
    }
    .slider {
        width: 200px;
        height: 20px;
        padding-right: 15px;
    }
    .table {
        padding: 7px;
        margin: 12px;
        border: 5px solid #87CEED;
        font-style: italic;
    }
    table th {
        font-size: 20px;
        font-weight: bold;
    }
    table td {
        font-size: 18px;
    }
    .button {
        margin: 10px;
        border-radius: 15px;
        color: white;
    }
    .card {
        border: 15px solid #87CEED;
        padding: 85px;
        height: auto;
        width: auto;
    }
    .label {
        font-style: italic;
        font-weight: bold;
        font-size: 20px;
    }
</style>
""")

create_ui()
ui.run()
