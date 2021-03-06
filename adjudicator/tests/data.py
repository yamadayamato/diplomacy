from adjudicator.named_coast import NamedCoast
from adjudicator.territory import CoastalTerritory, InlandTerritory, \
    SeaTerritory


class Nations:
    ENGLAND = 'ENGLAND'
    FRANCE = 'FRANCE'
    GERMANY = 'GERMANY'
    ITALY = 'ITALY'
    AUSTRIA = 'AUSTRIA'
    TURKEY = 'TURKEY'
    RUSSIA = 'RUSSIA'


class Territories:

    def __init__(self, state):
        self.ADRIATIC_SEA = SeaTerritory(state, 1, 'adriatic sea',
                                         [20, 22, 11, 53, 56])
        self.AEGEAN_SEA = SeaTerritory(state, 2, 'aegean sea',
                                       [5, 73, 28, 7, 33, 11, 50])
        self.BALTIC_SEA = SeaTerritory(state, 3, 'baltic sea',
                                       [24, 6, 29, 35, 48, 51, 37])
        self.BARRENTS_SEA = SeaTerritory(state, 4, 'barrents sea', [15, 42, 75])
        self.BLACK_SEA = SeaTerritory(state, 5, 'black sea', [21, 23, 73, 28, 47, 49])
        self.GULF_OF_BOTHNIA = SeaTerritory(state, 6, 'gulf of bothnia',
                                            [3, 31, 37, 51, 75, 75])
        self.EASTERN_MEDITERRANEAN = SeaTerritory(state, 7, 'eastern mediterranean',
                                                  [2, 50, 52])
        self.ENGLISH_CHANNEL = SeaTerritory(state, 8, 'english channel',
                                            [25, 26, 12, 36, 13, 16, 43, 57])
        self.GULF_OF_LYON = SeaTerritory(state, 9, 'gulf of lyon',
                                         [39, 44, 74, 55, 18, 19])
        self.HELGOLAND_BIGHT = SeaTerritory(state, 10, 'helgoland bight',
                                            [29, 34, 35, 16])
        self.IONIAN_SEA = SeaTerritory(state, 11, 'ionian sea',
                                       [2, 1, 20, 22, 33, 41, 54, 18])
        self.IRISH_SEA = SeaTerritory(state, 12, 'irish sea', [8, 38, 13, 14, 57])
        self.MID_ATLANTIC = SeaTerritory(state, 13, 'mid atlantic',
                                         [26, 8, 32, 12, 40, 14, 74, 45, 19])
        self.NORTH_ATLANTIC = SeaTerritory(state, 14, 'north atlantic',
                                           [27, 12, 38, 13, 15])
        self.NORWEGIAN_SEA = SeaTerritory(state, 15, 'norwegian sea',
                                          [4, 27, 30, 14, 42, 16])
        self.NORTH_SEA = SeaTerritory(state, 16, 'north sea',
                                      [25, 29, 30, 8, 10, 34, 36, 15, 42, 17,
                                       58])
        self.SKAGERRAK = SeaTerritory(state, 17, 'skagerrak', [29, 16, 42, 51])
        self.TYRRHENIAN_SEA = SeaTerritory(state, 18, 'tyrrhenian sea',
                                           [9, 11, 41, 46, 54, 55, 19])
        self.WESTERN_MEDITERRANEAN = SeaTerritory(state, 19, 'western mediterranean',
                                                  [9, 13, 40, 74, 54, 18])
        self.ALBANIA = CoastalTerritory(state, 20, 'albania', None,
                                        [1, 33, 11, 67, 53],
                                        [33, 53])
        self.ANKARA = CoastalTerritory(state, 21, 'ankara', 7, [23, 5, 28, 50],
                                       [23, 28])
        self.APULIA = CoastalTerritory(state, 22, 'apulia', 5, [1, 11, 41, 46, 56],
                                       [41, 56])
        self.ARMENIA = CoastalTerritory(state, 23, 'armenia', 7, [21, 21, 49, 50, 52],
                                        [49, 21])
        self.BERLIN = CoastalTerritory(state, 24, 'berlin', Nations.GERMANY,
                                       [3, 35, 64, 48, 68], [35, 48],
                                       supply_center=True,
                                       controlled_by=Nations.GERMANY)
        self.BELGIUM = CoastalTerritory(state, 25, 'belgium', None,
                                        [61, 8, 34, 43, 66, 16],
                                        [34, 43])
        self.BREST = CoastalTerritory(state, 26, 'brest', 2, [8, 32, 13, 65, 43],
                                      [32, 43])
        self.CLYDE = CoastalTerritory(state, 27, 'clyde', 1, [30, 38, 12, 14, 15],
                                      [30, 38])
        self.CONSTANTINOPLE = CoastalTerritory(state, 28, 'constantinople', 7,
                                               [2, 21, 5, 73, 50], [21, 50])
        self.DENMARK = CoastalTerritory(state, 29, 'denmark', None,
                                        [3, 10, 35, 16, 17, 51],
                                        [35, 51])
        self.EDINBURGH = CoastalTerritory(state, 30, 'edinburgh', 1,
                                          [27, 38, 15, 16, 58],
                                          [27, 58])
        self.FINLAND = CoastalTerritory(state, 31, 'finland', None, [6, 42, 75, 51],
                                        [51])
        self.GASCONY = CoastalTerritory(state, 32, 'gascony', 2,
                                        [26, 61, 39, 13, 65, 74],
                                        [26])
        self.GREECE = CoastalTerritory(state, 33, 'greece', None, [2, 20, 73, 11, 67],
                                       [20, 73])
        self.HOLLAND = CoastalTerritory(state, 34, 'holland', None,
                                        [25, 10, 35, 16, 66],
                                        [25, 35])
        self.KIEL = CoastalTerritory(state, 35, 'kiel', 3,
                                     [3, 24, 29, 10, 34, 64, 66],
                                     [24, 29, 34])
        self.LONDON = CoastalTerritory(state, 36, 'london', 1, [8, 16, 57, 58],
                                       [57, 58])
        self.LIVONIA = CoastalTerritory(state, 37, 'livonia', 6,
                                        [3, 6, 63, 48, 75, 72], [48])
        self.LIVERPOOL = CoastalTerritory(state, 38, 'liverpool', 1,
                                          [27, 30, 12, 14, 57, 58],
                                          [27, 57])
        self.MARSEILLES = CoastalTerritory(state, 39, 'marseilles', 2,
                                           [61, 32, 9, 44, 74],
                                           [44, 74])
        self.NORTH_AFRICA = CoastalTerritory(state, 40, 'north africa', None,
                                             [13, 54, 19],
                                             [54])
        self.NAPLES = CoastalTerritory(state, 41, 'naples', 5, [22, 11, 46, 18],
                                       [22, 46])
        self.NORWAY = CoastalTerritory(state, 42, 'norway', None,
                                       [4, 31, 15, 16, 17, 75, 51],
                                       [51])
        self.PICARDY = CoastalTerritory(state, 43, 'picardy', 2, [26, 25, 61, 8, 65],
                                        [26, 25])
        self.PIEDMONT = CoastalTerritory(state, 44, 'piedmont', 5,
                                         [9, 39, 55, 69, 56],
                                         [39, 55])
        self.PORTUGAL = CoastalTerritory(state, 45, 'portugal', None, [13, 74], [74])
        self.ROME = CoastalTerritory(state, 46, 'rome', 5, [22, 41, 55, 18, 56],
                                     [41, 55])
        self.RUMANIA = CoastalTerritory(state, 47, 'rumania', None,
                                        [5, 60, 73, 62, 67, 49, 70], [49])
        self.PRUSSIA = CoastalTerritory(state, 48, 'prussia', 3, [3, 24, 37, 68, 72],
                                        [24, 37])
        self.SEVASTAPOL = CoastalTerritory(state, 49, 'sevastapol', 6,
                                           [23, 5, 63, 47, 70],
                                           [24, 47])
        self.SMYRNA = CoastalTerritory(state, 50, 'smyrna', 7, [2, 23, 21, 28, 7, 52],
                                       [28, 52])
        self.SWEDEN = CoastalTerritory(state, 51, 'sweden', None,
                                       [3, 6, 29, 31, 42, 17],
                                       [29, 31, 42])
        self.SYRIA = CoastalTerritory(state, 52, 'syria', 7, [23, 7, 50], [50])
        self.TRIESTE = CoastalTerritory(state, 53, 'trieste', 4,
                                        [1, 20, 60, 52, 69, 67, 56, 71],
                                        [20, 56])
        self.TUNIS = CoastalTerritory(state, 54, 'tunis', None, [11, 40, 18, 19],
                                      [40])
        self.TUSCANY = CoastalTerritory(state, 55, 'tuscany', 5, [9, 44, 46, 18, 56],
                                        [44, 46])
        self.VENICE = CoastalTerritory(state, 56, 'venice', 5,
                                       [1, 22, 46, 44, 53, 18, 69],
                                       [22, 53])
        self.WALES = CoastalTerritory(state, 57, 'wales', 1, [8, 12, 36, 38, 58],
                                      [36, 38])
        self.YORKSHIRE = CoastalTerritory(state, 58, 'yorkshire', 1,
                                          [30, 36, 38, 16, 57],
                                          [30, 36])
        self.BOHEMIA = InlandTerritory(state, 59, 'bohemia', 4, [62, 64, 68, 69, 71])
        self.BUDAPEST = InlandTerritory(state, 60, 'budapest', 4,
                                        [62, 47, 67, 53, 71])
        self.BURGUNDY = InlandTerritory(state, 61, 'burgundy', 2,
                                        [25, 32, 39, 64, 65, 43, 66])
        self.GALICIA = InlandTerritory(state, 62, 'galicia', 4,
                                       [59, 60, 47, 68, 70, 71, 72])
        self.MOSCOW = InlandTerritory(state, 63, 'moscow', Nations.RUSSIA,
                                      [37, 47, 49, 75, 70, 72],
                                      supply_center=True,
                                      controlled_by=Nations.RUSSIA)
        self.MUNICH = InlandTerritory(state, 64, 'munich', 3,
                                      [24, 59, 61, 35, 68, 66, 69])
        self.PARIS = InlandTerritory(state, 65, 'paris', 2,
                                     [26, 61, 32, 43, 68, 66, 69])
        self.RUHR = InlandTerritory(state, 66, 'ruhr', 3, [25, 61, 34, 35, 64])
        self.SERBIA = InlandTerritory(state, 67, 'serbia', None,
                                      [20, 60, 73, 33, 47, 53])
        self.SILESIA = InlandTerritory(state, 68, 'silesia', 3,
                                       [24, 59, 62, 64, 48, 72])
        self.TYROLIA = InlandTerritory(state, 69, 'tyrolia', 4, [59, 64, 53, 56, 71])
        self.UKRAINE = InlandTerritory(state, 70, 'ukraine', 6, [62, 63, 47, 49, 72])
        self.VIENNA = InlandTerritory(state, 71, 'vienna', 4, [59, 60, 62, 53, 69])
        self.WARSAW = InlandTerritory(state, 72, 'warsaw', 6,
                                      [62, 37, 63, 68, 48, 70])
        self.BULGARIA = CoastalTerritory(state, 73, 'bulgaria', None,
                                         [2, 5, 28, 33, 47, 67],
                                         [47, 33, 28])
        self.SPAIN = CoastalTerritory(state, 74, 'spain', None,
                                      [32, 39, 45, 9, 19, 13], [32, 45, 39])
        self.ST_PETERSBURG = CoastalTerritory(state, 75, 'st. petersburg',
                                              Nations.RUSSIA,
                                              [4, 31, 37, 63, 42],
                                              [37, 31, 42], supply_center=True,
                                              controlled_by=Nations.RUSSIA)


class NamedCoasts:
    def __init__(self, state, territories):
        self.SPAIN_SC = NamedCoast(state, 1, 'spain sc', territories.SPAIN, [
            territories.MARSEILLES, territories.PORTUGAL,
            territories.MID_ATLANTIC,
            territories.WESTERN_MEDITERRANEAN, territories.GULF_OF_LYON
        ])
        self.SPAIN_NC = NamedCoast(state, 2, 'spain nc', territories.SPAIN, [
            territories.PORTUGAL, territories.MID_ATLANTIC, territories.GASCONY
        ])
        self.BULGARIA_EC = NamedCoast(state, 3, 'bulgaria ec', territories.BULGARIA, [
            territories.BLACK_SEA, territories.RUMANIA,
            territories.CONSTANTINOPLE,
        ])
        self.BULGARIA_SC = NamedCoast(state, 4, 'bulgaria sc', territories.BULGARIA, [
            territories.CONSTANTINOPLE, territories.AEGEAN_SEA,
            territories.GREECE
        ])
        self.ST_PETERSBURG_NC = NamedCoast(state, 5, 'st petersburg nc',
                                           territories.ST_PETERSBURG, [
                                               territories.BARRENTS_SEA,
                                               territories.NORWAY
                                           ])
        self.ST_PETERSBURG_SC = NamedCoast(state, 6, 'st petersburg nc',
                                           territories.ST_PETERSBURG, [
                                               territories.FINLAND,
                                               territories.LIVONIA,
                                               territories.GULF_OF_BOTHNIA
                                           ])
