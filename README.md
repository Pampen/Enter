# Enter JS- DEN KOMPLETTA GUIDEN TILL TOTAL FÖRSTRÖELSE #

Läs sakerna. Gör sakerna. Allt är bra i världen, peace out.

Felicia avsäger sig ansvar för eventuella felskrivingar och
risker för att denna kompletta guide inte är särskilt komplett.

## Få igång GIT och ladda ner filer ##
1. Skapa en ny mapp på valfri plats.
2. Öppna mappen i valfri kodmiljö.
3. Öppna terminalen i din kodmiljö.
4. Skriv:
        git clone https://github.com/Pampen/Enter.git
5. Om terminalen promptar för ett annat sätt att skriva det på:
Kopiera och kör igen med samma URL som ovan.
6. Initiera ett lokalt git-repository genom att skriva:
        git init
7. Sätt remote med:
        git remote add origin https://github.com/Pampen/Enter.git
8. Kontrollera att origin är korrekt genom att skriva:
        git remote -v
9. Skriv:
        git pull
10. Om terminalen promptar för ett annat sätt att skriva det på,
kopiera och kör om.
11. Testa att ändra något litet, t.ex lägga till ett space,
och kolla om du kan pusha.
12. EXTRA: Om git gör något skumt så att du inte kan skriva kommandon, skriv:
        :q

## Installera React.js ##

1. Öppna valfri terminal.
2. Gå till mappen som innehåller filen package.json.
3. I terminalen, skriv:
                npm install.
4. Om installationen fungerade, borde mappen "node_modules" existera i projektmappen.
5. Du behöver troligtvis bara göra det här en gång.

## Starta Server och kör programmet ##

1. Öppna en ny terminal.
2. Gå till mappen som "game.py" finns i på din dator.
3. Skriv:
        npm run flask
4. Gå till terminalen i din integrerade utvecklingsmiljö (IDE) och skriv:
	npm start
5. Nu borde både back- och frontend vara igång. Applikationen finns på localhost:3000.

##Avsluta server##
1. I terminalen som kör flask, tryck ctrl + c (WIN) eller ctrl + c (MAC)
2. I din kodmiljös terminal: tryck 