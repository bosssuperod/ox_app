# Noughts & Crosses

To start the app create a .env file within ox_app with the following values

```MYSQL_HOST='database'
MYSQL_USER='user'
MYSQL_PASSWORD='password'
MYSQL_DB='db'
```
run `docker-compose up`

## APIs
- List all players
- Add new players
- Return player details
- Create game
- Game status

### List all players

**Definition**

 `GET /getplayers`

 **Response**

 - `200 OK` on success

 ```json
 [
   {
     "id": 1,
     "name": "Jimi Wicks",
     "victory":  2,
     "defeat": 5,
     "draw": 3
   },
   {
     "id": 2,
     "name": "Ron Weasley",
     "victory": 5,
     "defeat": 2,
     "draw": 3
   }
 ]
 ```

### Add new player

**Definition**

`POST /players`

**Arguments**

- `"id":string` a globally unique id for this user
- `"name":string` a friendly name
- `"victory": integer` a score to count all the winnings
- `"defeat": integer` a score to count all the defeat
- `"draw": integer` a score to count all the draws

**Response**

- `201 Created` on success

```json
{
  "id": 1,
  "name": "Jimi Wicks",
  "victory": 0,
  "defeat": 0,
  "draw": 0
}
```

### Return player details

**Definition**

`GET /players/<id>`

**Response**

- `404 Not Found` if the player does not exist
- `200 OK` on success

```json
{
  "id": 1,
  "name": "Jimi Wicks",
  "victory": 2,
  "defeat": 5,
  "draw": 3
}
```

### Create Game

**Definition**

`POST /game`

**Arguments**

- `"id":string` a globally unique id for the game
- `"status": string` show the current game status
- `"players": []` a list of players
- `"board": [3x3[]]`
- `"current_turn": string` 
- `"winner": string` 

**Response**

- `201 Created` on success

```json
{
  "id": "f84233cd-73f3-4ee3-9996-7979334835f8",
  "status": "in_progress",
  "players": [
    {
      "player_o_id":1
    },
    {
      "player_x_id":2
    },
  ],
  "board":[
		[0, 0, 0],
		[0, 0, 0],
		[0, 0, 0]
  ],
  "current_turn": "Jimi Wicks",
  "winner": " "
}
```
