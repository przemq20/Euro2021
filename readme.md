
# EURO 2021

Euro 2021 jest projektem umożliwiającym tworzenie własnej bazy turniejów sportowych. 

## Słowem wstępu
Do implementacji wykorzystaliśmy zmodyfikowany schemat ze strony [schemat bazy dla zawodów sportowych]( https://www.vertabelo.com/blog/what-do-the-olympic-games-uefa-euro-2016-football-matches-and-databases-have-in-common/. )


![Schemat](https://i.ibb.co/QJXtdkY/groups.png)

Wykorzystana została darmowa baza danych PostgreSQL na serwerze [www.elephantsql.com](https://www.elephantsql.com/) 

Modele w aplikacji zostały zaimplementowane przy użyciu języka Python z wykorzystaniem flask, SQLalchemy oraz graphene.

# GraphQL
![The power of GraphQL directives - {Callstack} Blog](https://cdn-images-1.medium.com/max/960/1*TUzarF1NBCpga-8ahqzNHw.png)

GraphQL jest coraz popularniejszym sposobem udostępniania API. Zapewnia dostęp do danych w postaci grafu. Jego struktura zapytań opartych na JSON-ie pozwala na ograniczenie liczby danych przesyłanych z serwera do klientów docelowych. Pozwala bezproblemowo wysyłać wiele zapytań naraz oraz tworzyć zapytania kaskadowe. Eliminując częsty problem w REST-cie z zapytaniami n+1.

[Strona projektu GraphQL]([https://graphql.org/](https://graphql.org/))

[Dokumentacja](http://www.test.przemq20.ct8.pl/doc/index.html)

## Instalacja

```bash
pip3 install -r requirements.txt
```
W pliku instance/config.py należy uzupełnić dane dostępowe do własnej bazy PostgreSQL.

## Przykład działania
Przykład działania konsoli GraphQL można zobaczyć [tutaj](http://euro2021.przemq20.ct8.pl/graphql). 

Przykładowa kwerenda, zwracająca imię i nazwisko zawodnika wraz nazwą jego zespoły oraz wszystkimi meczami tej drużyny:
``` 
{
  allPlayers {
    edges {
      node {
        firstName
        lastName
        teams {
          teamName
        }
        currentTeam{
          scheduledMatches{
            team1{
              teamName
            }
            team2{
              teamName
            }
          }
        }
      }
    }
  }
}

```
![enter image description here](https://i.ibb.co/WPtD08k/Adnotacja-2020-05-28-193034.jpg)
Dodatkowo w celu przykładowego wykorzystania tej technologii została napisana prosta aplikacja webowa z wykorzystaniem frameworka Angular. 

[Repozyturium na githubie](https://github.com/XertDev/Euro2021-website)

 [Strona www](http://test.przemq20.ct8.pl/)

## Wykorzystane technologie:
- Python 3.6 
    - Flask
    - SQLAlchemy
    - psycopg2
    - graphene
    - graphene-sqlalchemy
    - Flask-GraphQL
    - flask_sqlalchemy
    - flask-cors
    - flask-admin
- Angular 
    - Angular CLI
    - Material design
## Twórcy
- Michał Jakubek
- Przemysław Lechowicz
