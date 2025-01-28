def test_stations_by_distance():
    from floodsystem.geo import stations_by_distance
    from floodsystem.stationdata import build_station_list
    
    # Sample data (correct)
    closest_10 = [('Cambridge Jesus Lock', 'Cambridge', 0.8402364350834995), ('Bin Brook', 'Cambridge', 2.502274086951454), ("Cambridge Byron's Pool", 'Grantchester', 4.0720438555077125), ('Cambridge Baits Bite', 'Milton', 5.115589516578674), ('Girton', 'Girton', 5.227070345811418), ('Haslingfield Burnt Mill', 'Haslingfield', 7.044388165868453), ('Oakington', 'Oakington', 7.128249171700346), ('Stapleford', 'Stapleford', 7.265694306995238), ('Comberton', 'Comberton', 7.7350743760373675), ('Dernford', 'Great Shelford', 7.993861351711722)]
    furthest_10 = [('Boscadjack', 'Wendron', 440.0026482838576), ('Gwithian', 'Gwithian', 442.05491558132354), ('Helston County Bridge', 'Helston', 443.37824966454974), ('Loe Pool', 'Helston', 445.07184458260684), ('Relubbus', 'Relubbus', 448.64944322554413), ('St Erth', 'St Erth', 449.03415711886015), ('St Ives Consols Farm', 'St Ives', 450.0734690482922), ('Penzance Tesco', 'Penzance', 456.3857579793324), ('Penzance Alverton', 'Penzance', 458.5766422710278), ('Penberth', 'Penberth', 467.53367291629183)]

    ## Running
    
    # List of station names 
    stations_list = build_station_list(use_cache= True)

    # Sort the stations as required
    Cambridge_coordinate = (52.2053, 0.1218)
    sorted_stations_by_distance = stations_by_distance(stations_list, Cambridge_coordinate)
    
    assert sorted_stations_by_distance[:10] == closest_10
    assert sorted_stations_by_distance[-10:] == furthest_10
    