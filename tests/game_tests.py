import json
from rest_framework import status
from rest_framework.test import APITestCase
from raterapi.models import Category, Game


class GameTests(APITestCase):
    def setUp(self):
        """
        Create a new account and create sample category
        """
        url = "/register"
        data = {
            "username": "steve",
            "password": "Admin8*",
            "email": "steve@stevebrownlee.com",
            "address": "100 Infinity Way",
            "phone_number": "555-1212",
            "first_name": "Steve",
            "last_name": "Brownlee",
            "bio": "Love those gamez!!"
        }
        # Initiate request and capture response
        response = self.client.post(url, data, format='json')

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Store the auth token
        self.token = json_response["token"]

        # Assert that a user was created
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # SEED DATABASE WITH ONE GAME TYPE
        # This is needed because the API does not expose a /gametypes
        # endpoint for creating game types
        gamecategory = Category()
        gamecategory.label = "Board game"
        gamecategory.save()


    def test_create_game(self):
        """
        Ensure we can create a new game.
        """
        # DEFINE GAME PROPERTIES
        url = "/games"
        data = {
            "gameId": 1,
            "designer": "random",
            "description": "random description",
            "title": "Carcassone",
            "year_released": 1999,
            "num_players": 6,
            "game_image": '',
            "categoryId":1
        }

        # Make sure request is authenticated
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

        # Initiate request and store response
        response = self.client.post(url, data, format='json')

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the game was created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that the properties on the created resource are correct
        self.assertEqual(json_response["designer"], "random")
        self.assertEqual(json_response["description"], "random description")
        self.assertEqual(json_response["title"], "Carcassone")
        self.assertEqual(json_response["num_players"], 6)
        self.assertEqual(json_response["game_image"], None)
        self.assertEqual(json_response["year_released"], 1999)

    def test_get_game(self):
        """
        Ensure we can get an existing game.
        """

        # Seed the database with a game
        game = Game()
        game.designer = 'random'
        game.description = 'random description'
        game.title = "Carcassone"
        game.num_players = 6
        game.game_image = ''
        game.year_released = 1999
        game.categoryId = 1
        game.save()

        # Make sure request is authenticated
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

        # Initiate request and store response
        response = self.client.get(f"/games/{game.id}")

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the game was retrieved
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the values are correct
        self.assertEqual(json_response["designer"], "random")
        self.assertEqual(json_response["description"], "random description")
        self.assertEqual(json_response["title"], "Carcassone")
        self.assertEqual(json_response["num_players"], 6)
        self.assertEqual(json_response["game_image"], None)
        self.assertEqual(json_response["year_released"], 1999)
     
    def test_change_game(self):
        game = Game()
        game.designer = 'random'
        game.description = 'random description'
        game.title = "Carcassone"
        game.num_players = 6
        game.game_image = ''
        game.year_released = 1999
        game.categoryId = 1
        game.save()

        data = {
            "gameId": 1,
            "designer": "random",
            "description": "hola",
            "title": "Carcassone",
            "year_released": 1999,
            "num_players": 6,
            "game_image": '',
            "categoryId":1
        }

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.put(f"/games/{game.id}", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(f'/games/{game.id}')
        json_response = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)