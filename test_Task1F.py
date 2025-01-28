def test_inconsistent_typical_range_stations():
    from floodsystem.stationdata import build_station_list
    from floodsystem.station import inconsistent_typical_range_stations
    
    # Sample data
    expected_output = ['Addlestone', 'Airmyn', 'Allerford', 'Arundel Queen St Bridge', 'Blacktoft', 'Braunton', 'Brentford', 'Broomfleet Weighton Lock', 'East Hull Hedon Road', 'Eccelsfield Morrisons', 'Fleetwood', 'Goole', 'Gravesend', 'Hedon Thorn Road Bridge', 'Hedon Westlands Drain', 'Hull Barrier Victoria Pier', 'Hull High Flaggs, Lincoln Street', "King's Lynn", 'Littlehampton', 'Paull', 'Salt end', 'Silloth Docks', 'Stone Creek', 'Templers Road', 'Topsham', 'Totnes', 'Truro Harbour', 'Weare Giffard', 'Westbrook Mill', 'Wilfholme PS', 'Wilfholme PS Hull Level']

    # Output
    # List of station names 
    stations_list = build_station_list(use_cache= True)
    
    output = inconsistent_typical_range_stations(stations_list)
    
    assert output == expected_output