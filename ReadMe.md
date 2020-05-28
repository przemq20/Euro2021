# EURO 2021

Euro 2021 jest projektem umożliwiającym tworzenie własnej bazy turniejów sportowych. 

## Słowem wstępu
Do implementacji wykorzystaliśmy zmodyfikowany schemat ze strony [vertabelo.com]( https://www.vertabelo.com/blog/what-do-the-olympic-games-uefa-euro-2016-football-matches-and-databases-have-in-common/. )

Wykorzystana została darmowa baza danych PostgreSQL na serwerze [www.elephantsql.com](https://www.elephantsql.com/) 


Modele w aplikacji zostały zaimplementowane przy użyciu języka Python z wykorzystaniem flask, SQLalchemy oraz graphene.

## Instalacja

```bash
pip3 install -r requirements.txt
```
W pliku instance/config.py należy uzupełnić dane dostępowe do własnej bazy PostgreSQL.

## Przykład działania
Przykład działania konsoli GraphQL można zobaczyć [tutaj](http://euro2021.przemq20.ct8.pl/graphql). 

Przykładowa kwerenda:
``` 
{
  allPlayers {
    edges {
      node {
        firstName
        lastName
        matchesInfo {
          match {
            schedule {
              team1 {
                teamName
              }
              team2 {
                teamName
              }
            }
          }
        }
      }
    }
  }
}
```

Dodatkowo w celu przykładowego wykorzystania została napisana prosta aplikacja webowa z wykorzystaniem frameworka Angular. 

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