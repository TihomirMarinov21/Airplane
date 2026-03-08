from nicegui import ui
from typing import List, Dict, Tuple
from classes import Person, Pilot

table = None  # reference to passenger table
passenger_data: List[Dict[str, str]] = []  # stored passenger info
taken_seats: set[Tuple[int, str]] = set()  # prevents double seat booking


def add(Plane, first_name: ui.input, last_name: ui.input, age: ui.number,
        row: ui.select, seat: ui.select, luggage: ui.select, checked: ui.select) -> None:
    """Registers a new passenger, validates input, prevents seat duplication."""

    selected_seat = (row.value, seat.value)

    # seat already taken?
    if selected_seat in taken_seats:
        ui.notify("Seat already taken!", color="red")
        return

    taken_seats.add(selected_seat)

    # remove taken seat from dropdown
    seat.options = [s for s in seat.options if (row.value, s) not in taken_seats]
    seat.update()

    ui.notify("Seat reserved!", color="green")

    # validate input fields
    if not first_name.value.strip() \
        or not last_name.value.strip()\
            or age.value is None or age.value <= 0:
        ui.notify("Please enter valid First Name, Last Name, and Age!", color="red")
        return
    Plane.passenger_count += 1

    # store passenger info
    passenger_data.append({
        "First Name": first_name.value,
        "Last Name": last_name.value,
        "Age": age.value,
        "Row": row.value,
        "Seat": seat.value,
        "Luggage": luggage.value,
        "Checked": checked.value
    })

    # reset form fields
    first_name.set_value("")
    last_name.set_value("")
    age.set_value(0)
    row.set_value("")
    seat.set_value("")
    luggage.set_value("")
    checked.set_value("")


def create_table() -> None:
    """Creates or updates the passenger table."""
    global table

    if not passenger_data:
        ui.notify("No passengers to display!", color="red")
        return

    columns = [
        {"name": "First Name", "label": "First Name", "field": "First Name"},
        {"name": "Last Name", "label": "Last Name", "field": "Last Name"},
        {"name": "Age", "label": "Age", "field": "Age"},
        {"name": "Row", "label": "Row", "field": "Row"},
        {"name": "Seat", "label": "Seat", "field": "Seat"},
        {"name": "Luggage", "label": "Luggage", "field": "Luggage"},
        {"name": "Checked", "label": "Checked", "field": "Checked"},
    ]

    if table is None:
        table = ui.table(columns=columns, rows=passenger_data).classes('table')
    else:
        table.rows = passenger_data
        table.update()


def create_crew_table() -> None:
    """Creates a table with randomly generated pilots and crew members."""

    crew_data = [
        {
            "Role": "Pilot",
            "First Name": pilot.first_name,
            "Last Name": pilot.last_name,
            "Age": pilot.age
        }
        for pilot in (Pilot() for _ in range(2))
    ] + [
        {
            "Role": "Crew",
            "First Name": person.first_name,
            "Last Name": person.last_name,
            "Age": person.age
        }
        for person in (Person() for _ in range(4))
    ]

    ui.table(
        columns=[
            {"name": "Role", "label": "Role", "field": "Role"},
            {"name": "First Name", "label": "First Name", "field": "First Name"},
            {"name": "Last Name", "label": "Last Name", "field": "Last Name"},
            {"name": "Age", "label": "Age", "field": "Age"},
        ],
        rows=crew_data
    ).classes('table')
