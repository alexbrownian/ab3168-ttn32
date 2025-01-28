def test_rivers_by_station_number(stations):
    from floodsystem.geo import rivers_by_station_numbers
    from floodsystem.stationdata import build_station_list
    
    # Sample data
    expected_output = [('Thames', 55), ('River Great Ouse', 31), ('River Avon', 30), ('River Calder', 24), ('River Aire', 21), ('River Severn', 20), ('River Derwent', 18), ('River Stour', 16), ('River Wharfe', 14), ('River Trent', 14), ('Witham', 14)]

    # List of station names 
    stations_list = build_station_list(use_cache= True)
    
    # Testing
    N = 9
    output = rivers_by_station_numbers(stations_list, N)
    
    assert expected_output == output