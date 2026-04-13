import json
import pprint
import urllib.request
from datetime import datetime, timedelta, timezone


def find_plants():
    url = "https://data.elexon.co.uk/bmrs/api/v1/reference/bmunits/all"

    with urllib.request.urlopen(url) as r:
        data = json.loads(r.read())

    # NPSHYD = non-pumped-storage hydro, PS = pumped storage
    hydro_types = ["NPSHYD", "PS"]
    hydro = [u for u in data if u.get("fuelType") in hydro_types]
    x = 0
    for u in hydro:
        print("--- Plant Num: ", x, " ---")
        print("NG BmUnit: ", u["nationalGridBmUnit"])
        print("bM Unit Name: ", u["bmUnitName"])
        print("FuelType: ", u["fuelType"])
        print("\n")
        x = x + 1

    """
    print(f"{'NGBmUnitName':25s}  {'Type':8s}  bmUnitName")

    for u in hydro:
        print(
            f"{u.get('nationalGridBmUnit', '?'):25s}  {u.get('fuelType', '?'):8s}  {u.get('bmUnitName', '?')}"
        )

    print(f"\ntotal hydro units found: {len(hydro)}")
    """


find_plants()
