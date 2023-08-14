import httpx
from prefect import flow, task
from prefect.artifacts import create_markdown_artifact


@flow()
def fetch_weathers(lat: float, lon: float):
    base_url = "https://api.open-meteo.com/v1/forecast/"
    weather = httpx.get(
        base_url,
        params=dict(latitude=lat, longitude=lon, hourly="temperature_2m"),
    )
    most_recent_temp = float(weather.json()["hourly"]["temperature_2m"][0])
    print(f"Most recent temp C: {most_recent_temp} degrees")
    print(most_recent_temp)
    mark_it_down(most_recent_temp)


@task
def mark_it_down(temp):
    markdown_report = f"""# Weather Report
    
## Recent weather

| Time        | Revenue |
|:--------------|-------:|
| Now | {temp} |
| In 1 hour       | {temp + 2} |
"""
    create_markdown_artifact(
        key="weather-report",
        markdown=markdown_report,
        description="Very scientific weather report",
    )


if __name__ == "__main__":
    fetch_weathers(38.9, -77.0)
