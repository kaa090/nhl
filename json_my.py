import json
# file_stat = "20232024.json"
# file_stat_hb = "20232024_hb.json"
# keys = ["playerId", "skaterFullName", "positionCode", "seasonId", "gamesPlayed", "goals", "assists", "penaltyMinutes", "ppPoints", "gameWinningGoals", "shots", "hits", "blockedShots"]
file_stat = "20142024.json"
file_stat_hb = "20142024_hb.json"
file_stat_total = "stat20142024.json"

keys_player = ["skaterFullName", "positionCode"]
keys_season = ["gamesPlayed", "goals", "assists", "penaltyMinutes", "ppPoints", "gameWinningGoals", "shots", "hits", "blockedShots"]

kaa = ["J.T. Miller","Brady Tkachuk","Jake Guentzel","Adam Fox","Brock Nelson","Brandon Hagel","Nazem Kadri","Evgeni Malkin","Drew Doughty","Michael Bunting","David Perron","Ryan Hartman","Pierre-Luc Dubois","Adam Henrique","Artyom Levshunov","Jean-Gabriel Pageau","Radko Gudas","Colton Parayko","Jamie Oleksiak","Erik Gudbranson"]
thunder = ["Nikita Kucherov","William Nylander","Filip Forsberg","Brayden Point","Andrei Svechnikov","Dougie Hamilton","Mika Zibanejad","Alex DeBrincat","Jordan Kyrou","Elias Lindholm","Zach Werenski","Patrik Laine","Boone Jenner","Rickard Rakell","Jake Walman","Aaron Ekblad","Taylor Hall","Rasmus Andersson","Ryan Pulock","Cam Fowler","Olen Zellweger"]
hill = ["Quinn Hughes","Sebastian Aho","Carter Verhaeghe","Kevin Fiala","Clayton Keller","Robert Thomas","Anze Kopitar","Patrick Kane","Lucas Raymond","Teuvo Teravainen","Bryan Rust","Noah Hanifin","Jake Sanderson","Nino Niederreiter","Shayne Gostisbehere","Valeri Nichushkin","Marcus Pettersson","Justin Faulk","Tyler Myers","Josh Norris","Maxim Tsyplakov"]
dmind = ["Artemi Panarin","Sidney Crosby","Adrian Kempe","Victor Hedman","Jesper Bratt","Steven Stamkos","Noah Dobson","Jeff Skinner","Artturi Lehkonen","Logan Cooley","Pavel Buchnevich","Martin Necas","Sam Bennett","JJ Peterka","Mason McTavish","Leo Carlsson","Sean Walker","Connor Clifton","Oliver Ekman-Larsson","Keegan Kolesar","Jamie Drysdale"]
elstahl = ["Nathan MacKinnon","Jack Eichel","Brock Boeser","Ryan Nugent-Hopkins","Devon Toews","Alexis Lafreniere","Brandon Montour","Vince Dunn","Mason Marchment","Mattias Ekholm","Filip Hronek","Jake DeBrusk","Cole Perfetti","Tyler Toffoli","Gabriel Vilardi","Tyler Bertuzzi","Alex Killorn","Troy Terry","Bowen Byram","Anton Lundell","Hampus Lindholm"]
hammer = ["Chris Kreider","Aleksander Barkov","Bo Horvat","Miro Heiskanen","Alex Tuch","Timo Meier","Mark Stone","Ryan O'Reilly","Claude Giroux","Gustav Nyquist","Erik Karlsson","Viktor Arvidsson","Brady Skjei","Kris Letang","Mike Matheson","Matty Beniers","Jonathan Huberdeau","Owen Power","Kirill Marchenko","Cam York","Lane Hutson"]
ice = ["Evan Bouchard","Wyatt Johnston","Travis Konecny","Jonathan Marchessault","Jamie Benn","Frank Vatrano","Drake Batherson","Ivan Barbashev","Charlie Coyle","Travis Sanheim","Jaccob Slavin","Scott Laughton","Mikael Backlund","Neal Pionk","Matt Roy","Jacob Trouba","Niko Mikkola","Will Cuylle","Josh Anderson","Simon Benoit"]
pandora = ["Mikko Rantanen","Kirill Kaprizov","Zach Hyman","John Tavares","Josh Morrissey","Owen Tippett","Gustav Forsling","Matt Boldy","Dylan Strome","Lawson Crouse","Pavel Zacha","Thomas Harley","Joel Farabee","Chandler Stephenson","Evan Rodrigues","Darnell Nurse","K'Andre Miller","Trent Frederic","Alexander Romanov","Will Borgen","Martin Fehervary"]
pens = ["Connor McDavid","Sam Reinhart","Connor Bedard","Tage Thompson","Roope Hintz","Cole Caufield","Moritz Seider","Brock Faber","Jared McCann","Tom Wilson","Eeli Tolvanen","Cutter Gauthier","Alex Pietrangelo","Seth Jones","Thomas Chabot","Andrei Kuzmenko","Andrew Mangiapane","Matthew Knies","Esa Lindell","Chris Tanev","Mario Ferraro"]
saa = ["Alex Ovechkin","Mikhail Sergachev","Tomas Hertl","Blake Coleman","William Karlsson","Brent Burns","Oliver Bjorkstrand","Anders Lee","Tyler Seguin","Brayden Schenn","J.T. Compher","Kyle Palmieri","Dylan DeMelo","Sean Monahan","Jake McCabe","Nicholas Paul","Warren Foegele","Yegor Sharangovich","Nikita Zadorov","Erik Cernak","Matt Dumba"]
rocket = ["Leon Draisaitl","Mitchell Marner","Evander Kane","Morgan Rielly","Mats Zuccarello","Trevor Moore","Shea Theodore","Dakota Joshua","Adam Fantilli","Casey Mittelstadt","Mikael Granlund","Vladimir Tarasenko","Dylan Cozens","Alex Iafallo","Pavel Mintyukov","Jeremy Lauzon","Brenden Dillon","Martin Pospisil","Tanner Jeannot","Arber Xhekaj","Scott Mayfield"]
nuts = ["Kyle Connor","Dylan Larkin","Nick Suzuki","Charlie McAvoy","Nikolaj Ehlers","Seth Jarvis","Juraj Slafkovsky","Matt Duchene","Quinton Byfield","Philipp Kurashev","Jonathan Drouin","Conor Garland","Jakob Chychrun","Sean Durzi","Garnet Hathaway","Fabian Zetterlund","Josh Manson","Liam O'Brien","Ben Chiarot","Jake Middleton","Kyle Burroughs"]
zver = ["Auston Matthews","Cale Makar","Matthew Tkachuk","Jack Hughes","Elias Pettersson","Jason Robertson","Tim Stutzle","Rasmus Dahlin","Macklin Celebrini","Logan Stankoven","Luke Hughes","Matvei Michkov","Jordan Eberle","Trevor Zegras","Brayden McNabb","Ryan McDonagh","Ivan Provorov","Kaiden Guhle","Jack Quinn","Brandt Clarke"]
zatec = ["David Pastrnak","Roman Josi","MacKenzie Weegar","Brad Marchand","Mathew Barzal","Vincent Trocheck","Joel Eriksson Ek","John Carlson","Nico Hischier","Mark Scheifele","Nick Schmaltz","Dylan Guenther","Jake Neighbours","Max Domi","Adam Larsson","William Eklund","Nick Seeler","Braden Schneider","Nick Foligno","Andrew Peeke","Bradly Nadeau"]

def read_stat():
    with open(file_stat_total, "r") as openfile:
        players = json.load(openfile)

    return players

def save_stat(players):
    json_object = json.dumps(players, indent=4)

    with open(file_stat_total, "w") as outfile:
      outfile.write(json_object)

def read_data_build_stat():
    players = {}

    with open(file_stat, "r") as openfile:
        json_stat = json.load(openfile)

    with open(file_stat_hb, "r") as openfile:
        json_stat_hb = json.load(openfile)

    for js in json_stat['data']:
        for js_hb in json_stat_hb['data']:
            if js['playerId'] == js_hb['playerId'] and js['seasonId'] == js_hb['seasonId']:
                js_all = dict(list(js.items()) + list(js_hb.items()))
                season = { key: js_all[key] for key in keys_season }

                if js['playerId'] in players.keys():
                    players[js['playerId']]['seasons'].update({js['seasonId']:season})
                else:
                    player = { key: js[key] for key in keys_player }
                    players[js['playerId']] = player
                    players[js['playerId']].update({'seasons':{js['seasonId']:season}})

    return players

def pprint(players):
    for player in players:
        print(f"{player['name']}\t{player['gp']}\t{player['g']}\t{player['a']}\t{player['pim']}\t{player['ppp']}\t{player['gwg']}\t{player['shots']}\t{player['hits']}\t{player['blocks']}\t")

def calc_stat(players_all, team):    
    players = []
    for playerId in players_all.keys():
        player = players_all[playerId]
        if player['skaterFullName'] in team:
            plrs = {'name':player['skaterFullName']}

            gp = 0
            g = 0
            a = 0
            pim = 0
            ppp = 0
            gwg = 0
            shots = 0
            hits = 0
            blocks = 0

            for seasonId in player['seasons']:
                ssn = player['seasons'][seasonId]

                gp += ssn['gamesPlayed']
                g += ssn['goals']
                a += ssn['assists']
                pim += ssn['penaltyMinutes']
                ppp += ssn['ppPoints']
                gwg += ssn['gameWinningGoals']
                shots += ssn['shots']
                hits += ssn['hits']
                blocks += ssn['blockedShots']

            g /= gp
            a /= gp
            pim /= gp
            ppp /= gp
            gwg /= gp
            shots /= gp
            hits /= gp
            blocks /= gp
            plrs.update({'gp':gp, 'g': g,'a': a,'pim': pim,'ppp': ppp,'gwg': gwg,'shots': shots,'hits': hits,'blocks': blocks})

            players.append(plrs)

    return players

players_all = read_stat()

# players_kaa = calc_stat(players_all, kaa)
# pprint(players_kaa)

# players_thunder = calc_stat(players_all, thunder)
# pprint(players_thunder)

# players_hill = calc_stat(players_all, hill)
# pprint(players_hill)
# players_dmind = calc_stat(players_all, dmind)
# pprint(players_dmind)
# players_elstahl = calc_stat(players_all, elstahl)
# pprint(players_elstahl)
# players_hammer = calc_stat(players_all, hammer)
# pprint(players_hammer)
# players_ice = calc_stat(players_all, ice)
# pprint(players_ice)
# players_pandora = calc_stat(players_all, pandora)
# pprint(players_pandora)
# players_pens = calc_stat(players_all, pens)
# pprint(players_pens)
# players_saa = calc_stat(players_all, saa)
# pprint(players_saa)
# players_rocket = calc_stat(players_all, rocket)
# pprint(players_rocket)
# players_nuts = calc_stat(players_all, nuts)
# pprint(players_nuts)
# players_zver = calc_stat(players_all, zver)
# pprint(players_zver)
players_zatec = calc_stat(players_all, zatec)
pprint(players_zatec)
