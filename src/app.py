import os
import csv
import requests
from datetime import datetime

def fetch_data():
    params = {
        "format": "geojson",
        "starttime": "2025-03-30",
        "endtime": "2025-04-30",
        "minmagnitude": 4.5,
        "limit": 100,
        "orderby": "time"
    }
    response = requests.get(
        "https://earthquake.usgs.gov/fdsnws/event/1/query",
        params=params
    )
    response.raise_for_status()
    return response.json()["features"]

def save_to_csv(features, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    fieldnames = [
        "id", "time", "latitude", "longitude", "depth",
        "magnitude", "magType", "nst", "gap", "dmin", "rms",
        "felt", "cdi", "mmi", "sig", "tsunami",
        "place", "status", "type", "net", "code", "ids",
        "sources", "alert", "detail", "title"
    ]

    with open(output_path, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for feat in features:
            props = feat["properties"]
            coords = feat["geometry"]["coordinates"]
            iso_time = datetime.utcfromtimestamp(props["time"] / 1000).isoformat() + "Z"

            writer.writerow({
                "id": feat["id"],
                "time": iso_time,
                "latitude": coords[1],
                "longitude": coords[0],
                "depth": coords[2],
                "magnitude": props.get("mag"),
                "magType": props.get("magType"),
                "nst": props.get("nst"),
                "gap": props.get("gap"),
                "dmin": props.get("dmin"),
                "rms": props.get("rms"),
                "felt": props.get("felt"),
                "cdi": props.get("cdi"),
                "mmi": props.get("mmi"),
                "sig": props.get("sig"),
                "tsunami": props.get("tsunami"),
                "place": props.get("place"),
                "status": props.get("status"),
                "type": props.get("type"),
                "net": props.get("net"),
                "code": props.get("code"),
                "ids": props.get("ids"),
                "sources": props.get("sources"),
                "alert": props.get("alert"),
                "detail": props.get("detail"),
                "title": props.get("title")
            })

def get_save_data():
    features = fetch_data()

    for feat in features:
        p = feat["properties"]
        c = feat["geometry"]["coordinates"]
        t = datetime.utcfromtimestamp(p["time"] / 1000).isoformat() + "Z"
        print(f"{feat['id']} | {t} | Mag {p['mag']} ({p.get('magType')}) | "
              f"{p.get('nst','?')} stations | gap {p.get('gap','?')}° | "
              f"dmin {p.get('dmin','?')}° | rms {p.get('rms','?')} | "
              f"{c[1]},{c[0]} @ {c[2]} km | {p.get('place')}")

    output_file = "../data/earthquakes.csv"
    save_to_csv(features, output_file)
    print(f"\nDatos guardados en '{output_file}'")