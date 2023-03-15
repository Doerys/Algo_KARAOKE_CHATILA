"""

#Exercice1

class Player:
    def __init__(self, name, scoreSong):
        self.__pseudo = name
        self.__scoreChanson = scoreSong

    def getPseudo(self):
        return self.__pseudo

    def getScoreChanson(self, index):
        return self.__scoreChanson[index]
    
    def changeScore(self, newScore, index):
        if(newScore > self.__scoreChanson[index]):
            self.__scoreChanson[index] = newScore

    def moyenneScore(self):
        somme = 0

        for i in range (0, 5):
            somme += self.__scoreChanson[i]

        moyenne = somme / 5 
        return moyenne

    def scoreTotal(self):
        somme = 0

        for i in range (0, 5):
            somme += self.__scoreChanson[i]

        return somme
    
    def showBestChanson(self):
        for i in range (0, 5):
            meilleurScore = 0
            if (self.__scoreChanson[i] > meilleurScore):
                meilleurScore = i

        print("La meilleur chanson est la numéro", meilleurScore)

            

    def showWorstChanson(self):
        for i in range (0, 5):
            pireScore = 100
            if (self.__scoreChanson[i] < pireScore):
                pireScore = i

        print("La pire chanson est la numéro", pireScore)

    def showScores(self):
        print(self.__scoreChanson)

scoresActuels = [0, 0, 0, 0, 0]

joueur1 = Player("John", scoresActuels)

print("Le joueur est", joueur1.getPseudo())
print("Le score de", joueur1.getPseudo(), "pour la chanson 1 est", joueur1.getScoreChanson(0))

joueur1.changeScore(1,0)

print("Le score de", joueur1.getPseudo(), "pour la chanson 1 est", joueur1.getScoreChanson(0))

joueur1.changeScore(1, 1)
joueur1.changeScore(0, 2)
joueur1.changeScore(3, 3)
joueur1.changeScore(4, 4)

totalScore = joueur1.scoreTotal()

moyenneScore = joueur1.moyenneScore()

print("Le total des scores est de", totalScore, "et la moyenne est de", moyenneScore)

joueur1.showBestChanson()
joueur1.showWorstChanson()

"""

#Exercice 2

class Karaoke:
    def __init__(self, songs, players):
        self.__chansons = songs
        self.__joueurs = players
    
    def getChanson(self):
        return self.__chansons
    
    def getPlayer(self):
        return self.__joueurs
    
    def showSong(self, index):
        print("Le nom de cette chanson est", self.__chansons[index])
        return self.__chansons[index]

    def showBestScoreSong(self, indexSong):

        bestScore = 0
        for i in range (0, len(self.__joueurs)):
            scoreJoueur = self.__joueurs[i].getScoreChanson(indexSong)
            if (scoreJoueur > bestScore):
                bestScore = scoreJoueur

        return bestScore
    
    def showBestPlayer(self):

        bestScore = 0
        
        for i in range (0, len(self.__joueurs)):
            scoreJoueur = self.__joueurs[i].scoreTotal()
            if (scoreJoueur > bestScore):
                bestPlayer = self.__joueurs[i].getPseudo()

        return bestPlayer
    
    def showBestMoyenne(self):

        bestScore = 0
        
        for i in range (0, len(self.__joueurs)):
            scoreJoueur = self.__joueurs[i].moyenneScore()
            if (scoreJoueur > bestScore):
                bestPlayer = self.__joueurs[i].getPseudo()

        return bestPlayer

"""

    def addPlayer(self, newPlayer):
        self.__joueurs.append(newPlayer)
        return

    def removePlayer(self):
        if (len(self.__joueurs) > 1):
             #here, code to removePlayer
        return

    def showBestScoreGlobal(self):

        bestScore = 0
        
        for i in range (0, len(chansons)):

        for i in range (0, len(self.__joueurs) + 1):
            scoreJoueur = self.__joueurs[i].scoreTotal()
            if (scoreJoueur > bestScore):
                bestPlayer = self.__joueurs.getPseudo()

        return bestPlayer

"""


class Player:
    def __init__(self, name, scoreSong):
        self.__pseudo = name
        self.__scoreChanson = scoreSong
        self.__moyenne = 0
        self.__total = 0

    def getPseudo(self):
        return self.__pseudo

    def getScoreChanson(self, index):
        return self.__scoreChanson[index]      
    
    def changeScore(self, newScore, index):
        if(newScore > self.__scoreChanson[index]):
            self.__scoreChanson[index] = newScore

    def moyenneScore(self):
        for i in range (0, 5):
            self.__total += self.__scoreChanson[i]

        self.__moyenne = (self.__total / 5)

        return self.__moyenne

    def scoreTotal(self):
        for i in range (0, 5):
            self.__total += self.__scoreChanson[i]

        return self.__total
    
    def showBestChanson(self):
        for i in range (0, 5):
            meilleurScore = 0
            if (self.__scoreChanson[i] > meilleurScore):
                meilleurScore = i

        print("La meilleur chanson est la numéro", meilleurScore)

            

    def showWorstChanson(self):
        for i in range (0, 5):
            pireScore = 100
            if (self.__scoreChanson[i] < pireScore):
                pireScore = i

        print("La pire chanson est la numéro", pireScore)

    def showScores(self):
        print(self.__scoreChanson)

scoreChansons = [0, 0, 0, 0, 0]
nomsChansons = ["A", "B", "C", "D", "E"]

joueurs = {}

joueurs[0] = Player("John", scoreChansons)
joueurs[1] = Player("Mathis", scoreChansons)

karaoke = Karaoke(nomsChansons, joueurs)


print("Le joueur 1 est", joueurs[0].getPseudo())
print("Le joueur 2 est", joueurs[1].getPseudo())
print("Le score de", joueurs[0].getPseudo(), "pour la chanson 1 est", joueurs[0].getScoreChanson(0))

joueurs[1].changeScore(50,0)

print("Le score de", joueurs[0].getPseudo(), "pour la chanson 1 est", joueurs[0].getScoreChanson(0))

joueurs[0].changeScore(50, 1)
joueurs[0].changeScore(60, 2)
joueurs[0].changeScore(60, 3)
joueurs[0].changeScore(60, 4)

joueurs[1].changeScore(70, 1)
joueurs[1].changeScore(70, 1)
joueurs[1].changeScore(80, 2)
joueurs[1].changeScore(80, 3)
joueurs[1].changeScore(99, 4)

print("Le total des scores est de", joueurs[0].scoreTotal(), "et la moyenne est de", joueurs[0].moyenneScore())

joueurs[0].showBestChanson()
joueurs[0].showWorstChanson()

nomChanson = karaoke.showSong(3)

print("Le meilleur score pour la chanson", nomChanson, "est", karaoke.showBestScoreSong(3))


print("Le meilleur total est détenu par", karaoke.showBestPlayer())
print("La meilleure moyenne est détenue par", karaoke.showBestMoyenne())