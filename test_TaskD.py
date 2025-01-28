import pytest
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river


def test_rivers_with_station():
    stations = build_station_list()

    # Get rivers with at least one station
    rivers = rivers_with_station(stations)

    assert len(rivers) > 0, "The number of rivers should be greater than 0"
    rivers_sorted = sorted(rivers)
    assert len(rivers_sorted) >= 10, "There should be at least 10 rivers in the dataset"
    expected_first_10 = [
        'Addlestone Bourne', 'Adur', 'Aire Washlands', 'Alconbury Brook',
        'Aldbourne', 'Aller Brook', 'Alre', 'Alt', 'Alverthorpe Beck', 'Ampney Brook'
    ]
    assert rivers_sorted[:10] == expected_first_10, "The first 10 rivers do not match the expected result"


def test_stations_by_river():
    stations = build_station_list()

    # Get the dictionary mapping rivers to stations
    river_dict = stations_by_river(stations)

    # Check that the rivers 'River Aire', 'River Cam', and 'River Thames' exist
    for river in ['River Aire', 'River Cam', 'River Thames']:
        assert river in river_dict, f"{river} should be a key in the river dictionary"

    # Check the stations on 'River Aire'
    river_aire_stations = sorted([station.name for station in river_dict['River Aire']])
    expected_river_aire_stations = [
        'Airmyn', 'Apperley Bridge', 'Armley', 'Beal Weir Bridge', 'Bingley',
        'Birkin Holme Washlands', 'Carlton Bridge', 'Castleford', 'Chapel Haddlesey',
        'Cononley', 'Cottingley Bridge', 'Ferrybridge Lock', 'Fleet Weir',
        'Gargrave', 'Kildwick', 'Kirkstall Abbey', 'Knottingley Lock',
        'Leeds Crown Point', 'Saltaire', 'Snaygill', 'Stockbridge'
    ]
    assert river_aire_stations == expected_river_aire_stations, "Stations on River Aire do not match the expected result"

    river_cam_stations = sorted([station.name for station in river_dict['River Cam']])
    expected_river_cam_stations = [
        'Cam', 'Cambridge', 'Cambridge Baits Bite', 'Cambridge Jesus Lock',
        'Dernford', 'Weston Bampfylde'
    ]
    assert river_cam_stations == expected_river_cam_stations, "Stations on River Cam do not match the expected result"

    river_thames_stations = sorted([station.name for station in river_dict['River Thames']])
    expected_river_thames_stations = [
        'Abingdon Lock', 'Bell Weir', 'Benson Lock', 'Boulters Lock', 'Bray Lock',
        'Buscot Lock', 'Caversham Lock', 'Chertsey Lock', 'Clifton Lock', 'Cookham Lock'
    ]