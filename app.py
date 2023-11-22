import database

MENU_PROMPT = '''\033[1;31;40m -- Bands App --

#Hello

Please choose one of these options:

1) Add a new band
2) See all bands
3) Find a band by name
4) See latest album from a band
5) Remove a band from the list
6) Exit.

Your selection: 
'''
def menu():
    connection = database.connect()
    database.createTables(connection)

    while(user_input := input(MENU_PROMPT)) != '6':
        if user_input == '1':
            name = input("Enter band name: ")
            album = input("Enter their latest album: ")
            rating = int(input('Enter your rating score of this album (0-100): '))

            database.addBand(connection, name, album, rating)
        elif user_input == '2':
            bands = database.getAllBands(connection)

            for band in bands:
                print(f'{band[1]}: {band[2]} - {band[3]}/100')
        elif user_input == '3':
            name = input('Enter band name to find: ')
            bands = database.getBandsByName(connection, name)
            try:

                for band in bands:
                    print(f'{band[1]}: {band[2]} - {band[3]}/100')
            except TypeError: print('Band not found. Check spelling.\n'
                                    '\nMaybe it is not in the database? '
                                    '\nYou can add a band to the database through the menu.')


        elif user_input == '4':
            name = input('Enter band name to find: ')

            latestAlbum = database.getLatestAlbumFromBand(connection, name)
            try:
                print(f'The latest album from {name} is: {latestAlbum[2]}')
            except TypeError: print('Band not found. Check spelling.\n'
                                    '\nMaybe it is not in the database? '
                                    '\nYou can add a band to the database through the menu.')

        elif user_input == '5':
            name = input('Enter name of band you would like to remove:')

            database.delItem(connection, name)
        else:
            print("Invalid input, please try again.")



menu()